# Test the example.
from tests.examples.index.showcase import full, partial


def test_full():
    assert full("John Doe") == (
        "<html>"
        "<head><title>Welcome to test.com</title></head>"
        "<body>"
        "<header>"
        "<div>John Doe<button hx-get='/logout'>log out</button></div>"
        "</header>"
        "<main><div><h1>Welcome</h1><p>Lorem ipsum...</p></div></main>"
        "<footer></footer>"
        "</body>"
        "</html>"
    )


def test_partial():
    assert partial() == ("<div><h1>Welcome</h1><p>Lorem ipsum...</p></div>")
