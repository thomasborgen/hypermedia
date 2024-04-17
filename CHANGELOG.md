# Version history

| Change | Bumps |
| - | - |
| Breaking | major |
| New Feature | minor |
| otherwise | patch |


## Latest Changes


### Breaking

* rename base_models.py -> models.py
* Use single quotes for attribute values.

### Feature

* Using single quotes for attributes lets us support `hx-vals`, since it expects a doubled quoted json string.


### Fix

* Rename `hr`->`Hr`, add alias `HorizontalRule` and export both in `__init__.py`

## Version 1.0.0 Hypermedia released

Hypermedia is an opinionated way to work with HTML in python and FastAPI. Hypermedia is designed to work with htmx.

### Features

* Composable Html generation with slots.
* Typed
* Works with FastAPI, and any other web framework.
* Works with HTMX
