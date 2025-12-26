# Hypermedia

Hypermedia is a pure python library for working with `HTML`. Hypermedia's killer feature is that it is composable through a `slot` concept. Because of that, it works great with `</> htmx` where you need to respond with both __partials__ and __full page__ html.

Hypermedia is made to work with `FastAPI` and `</> htmx`, but can be used by anything to create HTML.

___
![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fthomasborgen%2Fhypermedia%2Fmain%2Fpyproject.toml)
___

**Documentation
[Stable](https://thomasborgen.github.io/hypermedia/) |
[Source Code](https://github.com/thomasborgen/hypermedia) |
[Task Tracker](https://github.com/thomasborgen/hypermedia/issues)**

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
```

output

```html
<div>Hello <b>world!</b></div>
```

## Composability with slots

```python
from hypermedia import Html, Body, Div, Menu, H1, Div, Ul, Li

base = Html(
    Body(
        Menu(slot="menu"),
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
        <div>
            <div>Some content</div>
        </div>
    </body>
</html>
```

# Documentation

Head over to our [documentation](https://thomasborgen.github.io/hypermedia)
