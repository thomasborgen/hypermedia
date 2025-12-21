# HTMX

## The Concept

The core concept of HTMX is that we add event listeneres directly onto the html elements, when triggered htmx sends a request to the server, the server responds with HTML, and that we can choose with a CSS selector which part of the page will be updated with the HTML response from the server.

This means that we want to return snippets of HTML, or `partials`, as they are also called.

## The Problem

The problem is that we need to differentiate if it's HTMX that called an endpoint for a `partial`, or if the user just navigated directly to it and needs the `whole page` back in the response.

## The Solution

HTMX provides an `HX-Request` header that is always true. We can check for this header to know if it's an HTMX request or not.

___

In __hypermedia__ we've chosen to implement that check in a `@htmx` decorator for fastAPI. The decorator expects `partial` and optionally `full` arguments in the endpoint definition. These must be resolved by FastAPI's dependency injection system.

These can be read about in the [fastapi](/hypermedia/fastapi) section.

```python
from hypermedia.fastapi import htmx, full
```

The `partial` argument is a function that returns the partial HTML.
The `full` argument is a function that needs to return the whole HTML, for example on first navigation or a refresh.

!!! note
    `partial` and `full` arguments needs to be wrapped in `Depends` so that the full function's dependencies are resolved! Hypermedia ships an extra `full` wrapper, which is basically just making the function lazily loaded. The `full` wrapper _must_ be used, and the `@htmx` decorator will call the lazily wrapped function to get the full HTML page __only when needed__.

