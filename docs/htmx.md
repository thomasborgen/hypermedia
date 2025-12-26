# HTMX

## The Concept

The core concept of HTMX is that we add event listeneres directly onto the html elements, when triggered htmx sends a request to the server, the server responds with HTML, and that we can choose with a CSS selector which part of the page will be updated with the HTML returned from the server.

This means that we have 3 concepts to consider.

1. A full refresh, or first visit should return the whole html doc
2. A htmx request to a page should only update spesific concent, no need for header/menu/footer.
3. A htmx request can be a simple item in a list

Anything that is not the full html document is what we'll refer to as `partials` in hypermedia.

## The Problem

The problem is that we need to differentiate if it's HTMX that called an endpoint for a `partial`, or if the user just navigated directly to it and needs the `whole page` back in the response.

## The Solution

HTMX provides an `HX-Request` header that is always true. We can check for this header to know if it's an HTMX request or not.

___

In __hypermedia__ we've chosen to implement that check in a `@htmx` decorator for fastAPI. The decorator expects `partial` and optionally `full` arguments in the endpoint definition. These must be resolved by FastAPI's dependency injection system.

!!! info
    I'm all for letting people use this with django, flask, tornado so feel free to make a PR for decorators for web frameworks.

```python
from hypermedia.fastapi import htmx, full
```

The `partial` argument is a function that returns the partial HTML.
The `full` argument is a function that needs to return the whole HTML, for example on first navigation or a refresh.

!!! note
    `partial` and `full` arguments needs to be wrapped in `Depends` so that the full function's dependencies are resolved! Hypermedia ships an extra `full` wrapper, which is basically just making the function lazily loaded. The `full` wrapper _must_ be used, and the `@htmx` decorator will call the lazily wrapped function to get the full HTML page __only when needed__.

```python
@router.get("", response_class=HTMLResponse)
@htmx
async def fruits(
    request: Request,
    partial: Annotated[Element, Depends(render_fruits_partial)],
    full: Annotated[Element, Depends(full(render_fruits))],
) -> None:
    """Return the fruits page, partial or full."""
```


## HTMX usage

Using htmx is very straight forward. And all htmx attributes are fully typed and will work with autocompletion.

!!! note
    Since we can't use '-' in variable names and parameters all htmx attributes are written with underscore instead. ie: `hx-get` -> `hx_get`


To make a button that does a request to /fruits and puts the returned html into the `<main>` element:

```python
from hypermedia import Button

Button("Fruits", hx_get="/fruits", hx_target="main")
```

!!! hint
    `"main"` will replace the contents of the `<main>` element. replace `"main"` with a css selector like `"#body"` to replace that instead.

To make a div do a put update request to the fruit and take the returned html and replace itself. us target `"this"` This is very usefull for sending an update and have the server respond with the html for the new state (changed background color, new text/numbers). 

```python
from hypermedia import Div

Div("Banana", hx_put="/fruits/banana/set-eaten", hx_target="this")
```


## Setup HTMX in your project

All we need to do is add a script tag in the head that points to htmx

```python
from hypermedia import Script

Script(
    src="https://unpkg.com/htmx.org@2.0.0",
    integrity="sha384-wS5l5IKJBvK6sPTKa2WZ1js3d947pvWXbPJ1OmWfEuxLgeHcEbjUUA5i9V5ZkpCw",
    crossorigin="anonymous",
)
```

Here is a full example of a standard base with htmx added.

```python
def base() -> Element: 
    return ElementList(
        Doctype(),
        Html(
            Head(
                Title("My page"),
                Meta(charset="UTF-8"),
                Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                Meta(name="mobile-web-app-capable", content="yes"),
                slot="head",
            ),
            Main(id="main", slot="main"),
            Script(
                src="https://unpkg.com/htmx.org@2.0.0",
                integrity="sha384-wS5l5IKJBvK6sPTKa2WZ1js3d947pvWXbPJ1OmWfEuxLgeHcEbjUUA5i9V5ZkpCw",
                crossorigin="anonymous",
            ),
            Script(src="https://unpkg.com/htmx-ext-preload@2.0.0/preload.js"),
            Script(src="/static/auto_playback.js"),
            slot="html",
            lan="en",
        ),
    )
```

### Htmx settings

Here are good default settings that helps with common issues

```python
htmx_config = {
    "defaultSwapStyle": "innerHTML",
    "globalViewTransitions": True,
    "history": False,
    "refreshOnHistoryMiss": True,
    "allowNestedOobSwaps": True,
    "historyCacheSize": 0,
}
```

Add this to your header with the Meta tag:

```python
Meta(name="htmx-config", content=json.dumps(htmx_config)),
```


### Vary header

One unfortunate thing is how back navigation is handled, if the browser issues the back navigation, it believes the last request is what should be returned and that is often a htmx partial. To prevent this we can set up a middleware that assigns a `Vary` header. This tells the browser to treat the history differently based on what did the requests.

```python
@app.middleware("http")
async def add_vary_accept_header(  # type: ignore
    request: Request,
    call_next,
) -> Response:
    """Add the vary accept header.

    This allows the browser to cache the responses based on caller,
    which should prevent the browser from caching htmx responses as a full page
    """
    response: Response = await call_next(request)
    response.headers["Vary"] = "Accept"
    return response
```


### Non standard htmx attributes

Some of the htmx attributes would be a lot of work to map out, so in those cases you can replace both `:` and `-` with `_` and it should work

[The documentation](https://htmx.org/attributes/hx-on/) specifies that all hx attributes can be written with all dashes. Because of that Hypermedia lets users write hx attributes with underscores and Hypermedia changes them to dashes for you.

```python
from hypermedia import Div

Div(hx_on_click='alert("Making a request!")')
# <div hx-on-click='alert("Making a request!")'></div>
# Which is equivalent to:
# <div hx-on:click='alert("Making a request!"'></div>

Div(hx_on_htmx_before_request='alert("Making a request!")')
# <div hx-on-htmx-before-request='alert("Making a request!")'></div>

# shorthand version of above statement with double underscore
Div(hx_on__before_request='alert("Making a request!")')
# <div hx-on--before-request='alert("Making a request!")'></div>
```
