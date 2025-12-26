## Installation

Package is on pypi. Use `uv`, `poetry` or `pip` to install

```sh
uv add hypermedia
```

```sh
poetry add hypermedia
```

```sh
pip install hypermedia
```

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

use `.dump()` to dump your Elements to html.


```python
from hypermedia import Bold, Div

Div("Hello ", Bold("world!")).dump()
```

outputs

```html
<div>Hello <b>world!</b></div>
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

```

output

```html
<html>
    <body>
        <menu>
            <ul><li>main</li></ul>
        </menu>
        <header>my header</header>
        <div>
            <div>Some content</div>
        </div>
    </body>
</html>'
```
