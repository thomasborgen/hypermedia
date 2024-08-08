# Version history

| Change | Bumps |
| - | - |
| Breaking | major |
| New Feature | minor |
| otherwise | patch |


## Latest Changes

### Internal

* Document how to add attributes with symbols like dash and period.

## Version 4.0.0

### Breaking

Instead of having to use `text` and `composed_text` keywords you can now write text like this:

```python
Div("My text", Bold("My bold text"), "Tail")
```

* Removes `text` argument.
* Removes `composed_text` argument.

### Features

* The direct `*args` are now is a list of `Element | str`. This is basically exactly how `composed_text` worked, If we have a string child, we escape it, otherwise we call the child Elements `.dump()`. This should be a lot smoother to work with and read.

## Version 3.0.0

### Breaking

* Rename `htmx.py` to `fastapi.py`. The decorators were only for fastAPI. If we support django or flask, then they should get their own versions. This change facilitates for that so we don't have to have a breaking change further down the line.
* Don't expose `@htmx` and `@full` decorators directly from `hypermedia`, but require them to be imported from `hypermedia.fastapi`. 

### Housekeeping

* Readme file: Add features section, improve examples

## Version 2.2.0

### Features

* Escape all text by default.
* Add `composed_text` property that takes a list of strings or Elements and dumps that. This can be used to render strings with inline elements like `<br>`, `<i>` or `<b>`. used like: `composed_text=["regular", Italic(text="italic"), Bold(text="bold"), "regular"]`

### Internal

* Test elements with custom dump override like `Docstring` and `Comment` for string escaping.
* Add tests to composed_text.

## Version 2.1.2

* Expose models directly in `__init__` file for typing/extension purposes.
* #11 Ignore `None` valued attributes. This makes for easier programming.
* Properly Type attributes (an elements kwargs) `str | bool | None`.
* Improve test coverage.


## Version 2.1.1

### Fix

* Expose Path, Rect, Rectangle, Circle, Ellipse, Line, Polyline and Polygon Elements directly in `__init__` file.

## Version 2.1.0

### Features

* Added Path, Rect, Rectangle, Circle, Ellipse, Line, Polyline and Polygon Elements for when constructing and manipulating an SVG.

## Version 2.0.1

### Fix

* Now return partial render if full is not available. Consider if we should raise an exception instead.
* Protocol Typing for the FastAPI Request did not work as expected. Fall back to Any for now.

## Version 2.0.0 - Single quotes!

### Breaking

* rename base_models.py -> models.py
* Use single quotes for attribute values.

### Feature

* Using single quotes for attributes lets us support `hx-vals`, since it expects a doubled quoted json string.


### Fix

* Rename `hr`->`Hr`, add alias `HorizontalRule` and export both in `__init__.py`

## Version 1.0.0 - Hypermedia released

Hypermedia is an opinionated way to work with HTML in python and FastAPI. Hypermedia is designed to work with htmx.

### Features

* Composable Html generation with slots.
* Typed
* Works with FastAPI, and any other web framework.
* Works with HTMX
