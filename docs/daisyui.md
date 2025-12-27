# CSS - DaisyUI, Tailwind

In this guide the folder my app is just called `server`, whenever it is used, replace it with your app folder. This is the folder that contains the `main.py`(normally) file that has the `app = FastAPI()` variable in it. We've highlighted where you need to do changes.

## 1. Download and setup tailwind cli

DaisyUI has a quick setup that is easy to follow.

[https://daisyui.com/docs/install/standalone/](https://daisyui.com/docs/install/standalone/)

This also downloads the daisyui mjs file and creates `input.css` and `output.css` files. You can just delete the `output.css` file for now.


## 2. Make a tailwind setup file

This fils should be in the root of your project folder with the name `input.css`

If you got one in step 1, just make sure it looks something like below.

```css hl_lines="1 7"
@import "tailwindcss" source("./server");

@source not "./tailwindcss";
@source not "./daisyui{,*}.mjs";

@plugin "./daisyui.mjs" {
  themes: cupcake;
}
```

replace `"./server"` with the name of your app folder

!!! tip
    You can change the theme to the one you like, just replace `cupcake` with a name you find [in this list](https://daisyui.com/docs/themes/)


## 3 Compile the new tailwind to use

```sh
./tailwindcss -i ./input.css -o ./server/static/css/server.css
```

!!! note
    Change `server` with the name of your app. The folder that contains tha main.py that has the wsgi app variable.

!!! tip
    add `-m` flag to minify the css output

If that doesn't work try to make the tailwind file executable with:

```sh
chmod +x tailwindcss
```

If that doesnt work follow this guide and try again, try to figure it out and post an update with the fix or the issue at the [issue tracker](https://github.com/thomasborgen/hypermedia/issues)


## 4. Add static file handler to the FastAPI app

in `main.py` add the following, making sure to  change `server` with your app folders name first

```python 
app.mount("/static", StaticFiles(directory="server/static/"), name="static")
```

## 5. Add the script tag to load the css in your base html.

```python hl_lines="12 21"
def get_base() -> Element:
    """Create the base page."""
    return ElementList(
        Doctype(),
        Html(
            Head(
                Meta(charset="UTF-8"),
                Meta(
                    name="viewport",
                    content="width=device-width, initial-scale=1.0",
                ),
                Link(rel="stylesheet", href="/static/css/server.css"),
                Title("Server - home"),
                slot="head",
            ),
            Body(
                Header(),
                Main(id="main", slot="main")
            ),
            lang="no-nb",
            data_theme="cupcake",  # type: ignore
        ),
    )
```

Change `/static/css/server.css` if you chose a different folder structure.

Change the `cupcake` part of `data_theme="cupcake"` to whichever theme you want.
