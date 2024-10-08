# Hypermedia

Hypermedia is a pure python library for working with `HTML`. Hypermedia's killer feature is that it is composable through a `slot` concept. Because of that, it works great with `</> htmx` where you need to respond with both __partials__ and __full page__ html.

Hypermedia is made to work with `FastAPI` and `</> htmx`, but can be used by anything to create HTML.

## Features

* Build __HTML__ with python classes
* __Composable__ templates through a __slot__ system
* Seamless integration with __</> htmx__
* Fully typed and __Autocompletion__ for html/htmx attributes and styles
* Opinionated simple decorator for __FastAPI__
* Unlike other template engines like Jinja2 we have full typing since we never leave python land.

## The Basics

All html tags can be imported directly like:

```python
from hypermedia import Html, Body, Div, A
```

Tags are nested by adding children in the constructor:

```python
from hypermedia import Html, Body, Div

Html(Body(Div(), Div()))
```

Add text to your tag:

```python
from hypermedia import Div

Div("Hello world!")
```

use `.dump()` to dump your code to html.


```python
from hypermedia import Bold, Div

Div("Hello ", Bold("world!")).dump()

# outputs
# '<div>Hello <b>world!</b></div>'
```

## Composability with slots

```python
from hypermedia import Html, Body, Div, Menu, Header, Div, Ul, Li

base = Html(
    Body(
        Menu(slot="menu"),
        Header("my header", slot="header"),
        Div(slot="content"),
    ),
)

menu = Ul(Li(text="main"))
content = Div(text="Some content")

base.extend("menu", menu)
base.extend("content", content)

base.dump()

# outputs
# '<html><body><menu><ul><li>main</li></ul></menu><header>my header</header><div><div>Some content</div></div></body></html>'
```

## Attribute names with special characters

Most `html` and `</>htmx` attributes are typed and has Aliases where needed. That means that most of the time you won't have to think about this and it should _just work_.

The attribute name output rules are:

1. Any attribute that does not have an Alias will have any underscores (`_`) changed to hyphens (`-`).
2. Any attribute that is prefixed with `$` will be outputted as is without the first `$`.

ie

```python
# Is a specified attribute(typed) with an Alias:
Div(on_afterprint="test")  # <div onafterprint='test'></div>

# Unspecified attribute without Alias:
Div(data_test="test")  # <div data-test='test'></div>

# Spread without $ prefix gets its underscores changed to hyphens:
Div(**{"funky-format_test.value": True})  # <div funky-format-test.value></div>

# Spread with $ prefix
Div(**{"$funky-format_test.value": True})  # <div funky-format_test.value></div>
Div(**{"$funky-format_test.value": "name"})  # <div funky-format_test.value='name'></div>
```

Note: About the </> HTMX attributes. [The documentation](https://htmx.org/attributes/hx-on/) specifies that all hx attributes can be written with all dashes. Because of that Hypermedia lets users write hx attributes with underscores and Hypermedia changes them to dashes for you.

```python

Div(hx_on_click='alert("Making a request!")')
# <div hx-on-click='alert("Making a request!")'></div>
# Which is equivalent to:
# <div hx-on:click='alert("Making a request!"'></div>

Div(hx_on_htmx_before_request='alert("Making a request!")')
# <div hx-on-htmx-before-request='alert("Making a request!")'></div>

# shorthand version of above statement
Div(hx_on__before_request='alert("Making a request!")')
# <div hx-on--before-request='alert("Making a request!")'></div>
```

# HTMX

## The Concept

The core concept of HTMX is that the server responds with HTML, and that we can choose with a CSS selector which part of the page will be updated with the HTML response from the server.

This means that we want to return snippets of HTML, or `partials`, as they are also called.

## The Problem

The problem is that we need to differentiate if it's HTMX that called an endpoint for a `partial`, or if the user just navigated to it and needs the `whole page` back in the response.

## The Solution

HTMX provides an `HX-Request` header that is always true. We can check for this header to know if it's an HTMX request or not.

We've chosen to implement that check in a `@htmx` decorator. The decorator expects `partial` and optionally `full` arguments in the endpoint definition. These must be resolved by FastAPI's dependency injection system.

```python
from hypermedia.fastapi import htmx, full
```

The `partial` argument is a function that returns the partial HTML.
The `full` argument is a function that needs to return the whole HTML, for example on first navigation or a refresh.

> Note: The `full` argument needs to be wrapped in `Depends` so that the full function's dependencies are resolved! Hypermedia ships a `full` wrapper, which is basically just making the function lazily loaded. The `full` wrapper _must_ be used, and the `@htmx` decorator will call the lazily wrapped function to get the full HTML page when needed.

> Note: The following code is in FastAPI, but could have been anything. As long as you check for HX-Request and return partial/full depending on if it exists or not.

```python
def render_base():
    """Return base HTML, used by all full renderers."""
    return ElementList(Doctype(), Body(slot="body"))


def render_fruits_partial():
    """Return partial HTML."""
    return Div(Ul(Li("Apple"), Li("Banana"), Button("reload", hx_get="/fruits")))


def render_fruits():
    """Return base HTML extended with `render_fruits_partial`."""
    return render_base().extend("body", render_fruits_partial())


@router.get("/fruits", response_class=HTMLResponse)
@htmx
async def fruits(
    request: Request,
    partial: Element = Depends(render_fruits_partial),
    full: Element = Depends(full(render_fruits)),
) -> None:
    """Return the fruits page, partial or full."""
    pass
```

That's it. Now we have separated the rendering from the endpoint definition and handled returning partials and full pages when needed. Doing a full refresh will render the whole page. Clicking the button will make a htmx request and only return the partial.

What is so cool about this is that it works so well with FastAPI's dependency injection.

## Really making use of dependency injection


```python
fruits = {1: "apple", 2: "orange"}

def get_fruit(fruit_id: int = Path(...)) -> str:
    """Get fruit ID from path and return the fruit."""
    return fruits[fruit_id]

def render_fruit_partial(
    fruit: str = Depends(get_fruit),
) -> Element:
    """Return partial HTML."""
    return Div(fruit)

def render_fruit(
    partial: Element = Depends(render_fruit_partial),
):
    return render_base().extend("content", partial)

@router.get("/fruits/{fruit_id}", response_class=HTMLResponse)
@htmx
async def fruit(
    request: Request,
    partial: Element = Depends(render_fruit_partial),
    full: Element = Depends(full(render_fruit)),
) -> None:
    """Return the fruit page, partial or full."""
    pass
```

Here we do basically the same as the previous example, except that we make use of FastAPI's great dependency injection system. Notice the path of our endpoint has `fruit_id`. This is not used in the definition. However, if we look at our partial renderer, it depends on `get_fruit`, which is a function that uses FastAPI's `Path resolver`. The DI then resolves (basically calls) the fruit function, passes the result into our partial function, and we can use it as a value!

__This pattern with DI, Partials, and full renderers is what makes using FastAPI with HTMX worth it.__

In addition to this, one thing many are concerned about with HTMX is that since we serve HTML, there will be no way for another app/consumer to get a fruit in JSON. But the solution is simple:

Because we already have a dependency that retrieves the fruit, we just need to add a new endpoint:

```python
@router.get("/api/fruit/{fruit_id}")
async def fruit(
    request: Request,
    fruit: str = Depends(get_fruit),
) -> str:
    """Return the fruit data."""
    return fruit
```

Notice we added `/api/` and just used DI to resolve the fruit and just returned it. Nice!
