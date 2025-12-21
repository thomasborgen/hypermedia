# Hypermedia

A fully typed Python HTML Renderer with a focus on __composability__ of elements. All html tags available with autocompletion for all the tags attributes. A perfect companion for __htmx__ and ships with __FastAPI__ integration.



## Showcase

=== "python"

    ```python title="views/index.py"
    --8<-- "index/showcase.py:snippet"
    ```

    1. This function is usually placed in `commons.py` or similar since it will be used by all view files.


=== "full(user="John Doe").dump()"

    ```html hl_lines="10 14-17"
    <html>

    <head>
        <title>Welcome to test.com</title>
    </head>

    <body>
        <header>
            <!-- (1) -->
            <div>John Doe<button hx-post='/logout'>log out</button></div>
        </header>
        <main>
            <!-- (2) -->
            <div>
                <h1>Welcome</h1>
                <p>Lorem ipsum...</p>
            </div>
        </main>
        <footer></footer>
    </body>

    </html>
    ```

    1. Base was extended with result from `user_header(user: str)` function because a user was logged in!
    2. This part is rendered by the `partial()` function.

=== "partial().dump()"

    ```html
    <div>
        <h1>Welcome</h1>
        <p>Lorem ipsum...</p>
    </div>
    ```


## Why use Hypermedia

If the above example intrigues you then that should be more than enough to give `hypermedia` a go. 

Other reasons for __hypermedia__:

* You need to create html with Python
* You want to create html snippets and weave them together.
* You think __HTMX__ makes a lot of sense.
* Html attributes? yes. Every html element have autocompletion for their specific attributes.
* Jinja? tired of not being able to use your types and models? __hypermedia__ never leaves python land, so you keep it all!
* You want to make a website with __FastAPI__ - `hypermedia` ships with special decorator for __FastAPI__


## Goal

To make it easy to write a webapplication in python.

## Why

This was just the way we wanted to write html with python. We didn't want to have jinja files were we lost all typing and autocompletion from our python project. And we felt that existing solutions didn't do `composability` the way we wanted to do it. Especially with regards to working with `htmx` with partials and full pages.

## Contributing


Add issues, ask good questions. Come with good suggestions <3

[check the contibuting section](/hypermedia/contributing)

## Installation

Package is on pypi. Use `pip`, `poetry` or `uv` to install

```sh
pip install hypermedia
```
```sh
poetry add hypermedia
```
```sh
uv add hypermedia
```


What to do next? head over to the [quickstart](/hypermedia/quickstart) section!
