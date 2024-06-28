# Version history

| Change | Bumps |
| - | - |
| Breaking | major |
| New Feature | minor |
| otherwise | patch |


## Latest Changes

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
