# Version history

| Change | Bumps |
| - | - |
| Breaking | major |
| New Feature | minor |
| otherwise | patch |


## Latest Changes


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