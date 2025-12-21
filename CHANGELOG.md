# Version history

| Change | Bumps |
| - | - |
| Breaking | major |
| New Feature | minor |
| otherwise | patch |


## Latest Changes

## Version 5.4.0

### Features

* Allow None values through and skip them.
* Allow primitives through without having to cast them to str first.
* Add Decimal as an allowed primitive.

### Internal

* Run tests on python 3.14

## Version 5.3.4

### Features

* Add `capture` attribute to input element with the allowed values `"user"` and `"environment"`
* Add `dialog` as a posible value to a forms `method` attribute

###  Internal 

* Migrate dependency manager to uv.
* Remove safety check that now requires login


## Version 5.3.3

* Fixes bug with svg element dumping. (#48)[https://github.com/thomasborgen/hypermedia/issues/48]

## Version 5.3.2

* Fixes `style` attribute rendering.

## Version 5.3.1

* Adds `lang` as an attribute to the `Html` element.

## Version 5.3.0

### Feature

* Adds `SafeString` type as a wrapper around the normal `str` class. This can be used to tell hypermedia not to `html.escape` the string in any element.


```python
Div("this is always escaped")
Div(SafeString("This will not be escaped"))
```

* Hypermedia is now cachable - All calls to `.dump()` now returns a `SafeString`. This means that caching a dumped element is now possible because we won't call `html.escape` on it again.

```python
@lru_cache()
def stylesheets() -> SafeString:
    return ElementList(
        Link(
            rel="stylesheet",
            href="/static/css/normalize.css",
            type="text/css",
        ),
        Link(
            rel="stylesheet",
            href="/static/css/simple.min.css",
            type="text/css",
        )
    ).dump()

def base():
    """
    Once `stylesheets()` is called once, it will always use the cached String in subsequent
    calls to `base()`
    """
    return ElementList(
        Doctype(),
        Html(
            Head(
                Meta(charset="UTF-8"),
                stylesheets(),
                slot="head",
            ),
            Body(...)
            lan="en",
        ),
    )
```

* `Script` and `Style` elements wraps input in `SafeString` by default.

```python
Script("This is wrapped in `SafeString` by default")
Style("This is wrapped in `SafeString` by default")
```


## Version 5.2.0

### Feature

* Can now use hyperscript with the `_` attribute that renders as: `_='value'`

### Fix

* Fix missing Alias for the `for_` attribute. It now renders correctly as `for='value'`


## Version 5.1.0

### Fix

* Calling `dump()`, more specifically `render_attributes()` popped out `class_` and `classes` attributes from the element. So subsequent calls would be missing the attributes. [PR](https://github.com/thomasborgen/hypermedia/pull/32)


## Version 5.0.0

### Breaking

We need a way to handle html attributes like `hx-on:click` or `any_weird.format`. At the same time I want it to be easy to add attributes. I've decided to let all kwargs added normally like `data_test` where no `Alias` is defined will have its underscores replaced with hyphens. Any kwarg that has a `$` prefix, will be outputted as is minus the `$`. This kwarg can only have been added by spreading a dict into the constructor, so we can assume that it is done on purpose.

* Any attribute that does not have an Alias will have any underscores (`_`) changed to hyphens (`-`).
* Any attribute that is prefixed with `$` will be outputted as is without the first `$`.

ie

```python
# Is a specified attribute(typed) with an Alias:
Div(on_afterprint="test")  # <div onafterprint='test'></div>
# Unspecified attribute without Alias:
Div(data_test="test")  # <div data-test='test'></div>
# Spread without $ prefix gets its underscores changed to hyphens.
Div(**{"funky-format_test.value": True})  # <div funky-format-test.value></div>
# Spread with $ prefix
Div(**{"$funky-format_test.value": True})  # <div funky-format_test.value></div>
Div(**{"$funky-format_test.value": "name"})  # <div funky-format_test.value='name'></div>
```

### Feature

* `classes` and `class_` attributes are now merged. 

```python
def test_class_and_classes_are_combined() -> None:
    element = TestElement(class_="three", classes=["one", "two"])

    assert element._render_attributes() == " class='one two three'"
```

## Version 4.1.0

### Feature

Added types for html elements and their attributes. The type system is taken from [Ludic.](https://github.com/getludic/ludic). It is just so incredibly good. This gives us autocomplete support for everything.

* Types html elements and attributes.

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
