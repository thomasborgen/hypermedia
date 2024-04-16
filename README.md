# Hypermedia

hypermedia is a pure python library for working with html. hypermedias killer feature is that it is html code is composable through `slot` concept. Because of that, it works great with HTMX partials and full page reloads.

Hypermedia is made to work with FastAPI and HTMX. but can be used by any web server.


Here are some basics:

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
from hypermedia import Html, Body, Div

Html(text="Hello world!")
```

use `.dump()` to dump your code to html.


```python
from hypermedia import Html, Body, Div

Html(text="Hello world!").dump()

# outputs
# '<html>hello world</html>'
```

## Composability with slots

```python
from hypermedia import Html, Body, Div, Menu, Header, Div, Ul, Li

base = Html(
    Body(
        Menu(slot="menu"),
        Header(slot="header", text="my header"),
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


# With FastAPI:

coming


## Using dependency injection.
