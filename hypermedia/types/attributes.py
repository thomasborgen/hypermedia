from typing import Annotated, Literal, Protocol, TypedDict

from hypermedia.types.styles import CSSProperties


class URLType(Protocol):
    """Protocol for URL-like types."""

    def __str__(self) -> str:
        """Url types must implement `__str__`."""


class Alias(str):
    """Alias type for attributes."""


class Attrs(TypedDict, total=False):
    """Attributes of an element."""


class NoAttrs(TypedDict):
    """Placeholder for element with no attributes."""


class HypermediaAttrs(Attrs, total=False):
    """Attributes for hypermedia elements."""

    slot: str | None


class HtmlAttrs(HypermediaAttrs, total=False):
    """Common attributes for HTML elements."""

    id: str
    accesskey: str
    class_: Annotated[str, Alias("class")]
    classes: Annotated[list[str], Alias("class")]  # merged with class_
    contenteditable: Literal["true", "false"]
    dir: Literal["ltr", "rtl", "auto"]
    draggable: Literal["true", "false"]
    enterkeyhint: Literal[
        "enter", "done", "go", "next", "previous", "search", "send"
    ]
    hidden: Literal["true", "false"]
    inert: bool
    inputmode: Literal[
        "none", "text", "search", "tel", "url", "email", "numeric", "decimal"
    ]
    lang: str
    popover: bool
    spellcheck: Literal["true", "false"]
    style: CSSProperties
    tabindex: int
    title: str
    translate: Literal["yes", "no"]


class HtmxAttrs(Attrs, total=False):
    """
    HTMX attributes for HTML elements.

    See: https://htmx.org/
    """

    hx_get: Annotated[URLType, Alias("hx-get")]
    hx_post: Annotated[URLType, Alias("hx-post")]
    hx_put: Annotated[URLType, Alias("hx-put")]
    hx_delete: Annotated[URLType, Alias("hx-delete")]
    hx_patch: Annotated[URLType, Alias("hx-patch")]

    hx_on: Annotated[str, Alias("hx-on")]
    hx_include: Annotated[str, Alias("hx-include")]
    hx_confirm: Annotated[str, Alias("hx-confirm")]
    hx_trigger: Annotated[
        Literal["load", "click", "dblclick", "hover", "focus" "blur"] | str,
        Alias("hx-trigger"),
    ]
    hx_target: Annotated[
        Literal["this", "next", "previous"] | str, Alias("hx-target")
    ]
    hx_select: Annotated[str, Alias("hx-select")]
    hx_select_oob: Annotated[str, Alias("hx-select-oob")]
    hx_swap: Annotated[
        Literal[
            "innerHTML",
            "outerHTML",
            "beforebegin",
            "afterbegin",
            "beforeend",
            "afterend",
            "delete",
            "none",
        ]
        | str,
        Alias("hx-swap"),
    ]
    hx_swap_oob: Annotated[Literal["true", "false"], Alias("hx-swap-oob")]
    hx_vals: Annotated[str, Alias("hx-vals")]  # TODO: dict
    hx_sync: Annotated[str, Alias("hx-sync")]
    hx_boost: Annotated[Literal["true", "false"], Alias("hx-boost")]
    hx_indicator: Annotated[str, Alias("hx-indicator")]
    hx_push_url: Annotated[
        Literal["true", "false"] | str, Alias("hx-push-url")
    ]
    hx_history: Annotated[Literal["false"], Alias("hx-history")]
    hx_history_elt: Annotated[str, Alias("hx-history-elt")]
    hx_ext: Annotated[str, Alias("hx-ext")]
    hx_disable: Annotated[bool, Alias("hx-disable")]
    hx_disabled_elt: Annotated[str, Alias("hx-disabled-elt")]
    hx_disinherit: Annotated[str, Alias("hx-disinherit")]
    hx_encoding: Annotated[str, Alias("hx-encoding")]
    hx_headers: Annotated[str, Alias("hx-headers")]  # TODO: dict
    hx_params: Annotated[Literal["*", "none"] | str, Alias("hx-params")]
    hx_preserve: Annotated[bool, Alias("hx-preserve")]
    hx_prompt: Annotated[str, Alias("hx-prompt")]
    hx_replace_url: Annotated[URLType, Alias("hx-replace-url")]
    hx_request: Annotated[str, Alias("hx-request")]
    hx_validate: Annotated[Literal["true", "false"], Alias("hx-validate")]
    hx_ws: Annotated[str, Alias("hx-ws")]
    hx_sse: Annotated[str, Alias("hx-sse")]

    # Extensions
    ws_connect: Annotated[str, Alias("ws-connect")]
    ws_send: Annotated[str, Alias("ws-send")]
    sse_connect: Annotated[str, Alias("sse-connect")]
    sse_send: Annotated[str, Alias("sse-send")]
    sse_swap: Annotated[str, Alias("sse-swap")]


class WindowEventAttrs(Attrs, total=False):
    """Event Attributes for HTML elements."""

    on_afterprint: Annotated[str, Alias("onafterprint")]
    on_beforeprint: Annotated[str, Alias("onbeforeprint")]
    on_beforeunload: Annotated[str, Alias("onbeforeunload")]
    on_error: Annotated[str, Alias("onerror")]
    on_hashchange: Annotated[str, Alias("onhashchange")]
    on_load: Annotated[str, Alias("onload")]
    on_message: Annotated[str, Alias("onmessage")]
    on_offline: Annotated[str, Alias("onoffline")]
    on_online: Annotated[str, Alias("ononline")]
    on_pagehide: Annotated[str, Alias("onpagehide")]
    on_pageshow: Annotated[str, Alias("onpageshow")]
    on_popstate: Annotated[str, Alias("onpopstate")]
    on_resize: Annotated[str, Alias("onresize")]
    on_storage: Annotated[str, Alias("onstorage")]
    on_unhandledrejection: Annotated[str, Alias("onunhandledrejection")]
    on_unload: Annotated[str, Alias("onunload")]


class FormEventAttrs(Attrs, total=False):
    """Event Attributes for HTML Form elements."""

    on_blur: Annotated[str, Alias("onblur")]
    on_change: Annotated[str, Alias("onchange")]
    on_contextmenu: Annotated[str, Alias("oncontextmenu")]
    on_focus: Annotated[str, Alias("onfocus")]
    on_input: Annotated[str, Alias("oninput")]
    on_invalid: Annotated[str, Alias("oninvalid")]
    on_reset: Annotated[str, Alias("onreset")]
    on_search: Annotated[str, Alias("onsearch")]
    on_select: Annotated[str, Alias("onselect")]
    on_submit: Annotated[str, Alias("onsubmit")]


class KeyboardEventAttrs(Attrs, total=False):
    """Event Attributes for Keyboard events."""

    on_keydown: Annotated[str, Alias("onkeydown")]
    on_keypress: Annotated[str, Alias("onkeypress")]
    on_keyup: Annotated[str, Alias("onkeyup")]


class MouseEventAttrs(Attrs, total=False):
    """Event Attributes for Mouse events."""

    on_click: Annotated[str, Alias("onclick")]
    on_dblclick: Annotated[str, Alias("ondblclick")]
    on_mousedown: Annotated[str, Alias("onmousedown")]
    on_mousemove: Annotated[str, Alias("onmousemove")]
    on_mouseout: Annotated[str, Alias("onmouseout")]
    on_mouseover: Annotated[str, Alias("onmouseover")]
    on_mouseup: Annotated[str, Alias("onmouseup")]
    on_wheel: Annotated[str, Alias("onwheel")]


class DragEventAttrs(Attrs, total=False):
    """Event Attributes for Drag events."""

    on_drag: Annotated[str, Alias("ondrag")]
    on_dragend: Annotated[str, Alias("ondragend")]
    on_dragenter: Annotated[str, Alias("ondragenter")]
    on_dragleave: Annotated[str, Alias("ondragleave")]
    on_dragover: Annotated[str, Alias("ondragover")]
    on_dragstart: Annotated[str, Alias("ondragstart")]
    on_drop: Annotated[str, Alias("ondrop")]


class ClipboardEventAttrs(Attrs, total=False):
    """Event Attributes for Clipboard events."""

    on_copy: Annotated[str, Alias("oncopy")]
    on_cut: Annotated[str, Alias("oncut")]
    on_paste: Annotated[str, Alias("onpaste")]


class EventAttrs(
    WindowEventAttrs,
    FormEventAttrs,
    KeyboardEventAttrs,
    MouseEventAttrs,
    DragEventAttrs,
    ClipboardEventAttrs,
    total=False,
):
    """Event Attributes for HTML elements."""


class HtmlAndEventAttrs(HtmlAttrs, EventAttrs, total=False):
    """Common HTML and event attributes."""


class GlobalAttrs(HtmxAttrs, HtmlAndEventAttrs, total=False):
    """Global attributes for HTML elements."""


class HtmlTagAttrs(HypermediaAttrs, total=False):
    """Common attributes for HTML elements."""

    xmlns: str


class MetaAttrs(HtmlAttrs, total=False):
    """Attributes for `<meta>` elements."""

    name: str
    content: str
    charset: str
    property: str


class StyleAttrs(HtmlAndEventAttrs, total=False):
    """Attributes for `<style>` elements."""

    media: str
    type: Literal["text/css"]


class ScriptAttrs(HtmlAttrs, total=False):
    """Attributes for `<script>` elements."""

    async_: bool
    crossorigin: Literal["anonymous", "use-credentials"]
    defer: bool
    integrity: str
    nomodule: bool
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    src: str
    type: str


class HeadLinkAttrs(HtmlAttrs, total=False):
    """Attributes for `<link>` elements."""

    type: str
    rel: Literal[
        "canonical",
        "alternate",
        "stylesheet",
        "icon",
        "apple-touch-icon",
        "preconnect",
    ]
    crossorigin: Literal["anonymous", "use-credentials", True]
    hreflang: str
    href: str
    integrity: str


class InputAttrs(GlobalAttrs, total=False):
    """Attributes for `<input>` elements."""

    accept: str
    alt: str
    autcomplete: Literal["on", "off"]
    autofocus: bool
    checked: bool
    dirname: str
    disabled: bool
    form: str
    formaction: str
    formenctype: Literal[
        "application/x-www-form-urlencoded",
        "multipart/form-data",
        "text/plain",
    ]
    formmethod: Literal["get", "post"]
    formnovalidate: bool
    formtarget: str
    height: int
    list: str
    max: int
    maxlength: int
    min: int
    minlength: int
    multiple: bool
    name: str
    pattern: str
    placeholder: str
    popovertarget: str
    popovertargetaction: Literal["show", "hide", "toggle"]
    readonly: bool
    required: bool
    size: int
    src: str
    step: int
    type: Literal[
        "checkbox",
        "button",
        "color",
        "date",
        "datetime-local",
        "email",
        "file",
        "hidden",
        "image",
        "month",
        "number",
        "password",
        "radio",
        "range",
        "reset",
        "search",
        "submit",
        "tel",
        "text",
        "time",
        "url",
        "week",
    ]
    value: str
    width: int


class OutputAttrs(GlobalAttrs, total=False):
    """Attributes for `<output>` elements."""

    for_: Annotated[str, "for"]
    form: str
    name: str


class OptionAttrs(GlobalAttrs, total=False):
    """Attributes for `<option>` elements."""

    disabled: bool
    label: str
    selected: bool
    value: str


class OptgroupAttrs(GlobalAttrs, total=False):
    """Attributes for `<optgroup>` elements."""

    disabled: bool
    label: str


class SelectAttrs(GlobalAttrs, total=False):
    """Attributes for `<select>` elements."""

    autofocus: bool
    disabled: bool
    form: str
    multiple: bool
    name: str
    required: bool
    size: int


class TextAreaAttrs(GlobalAttrs, total=False):
    """Attributes for `<textarea>` elements."""

    autofocus: bool
    cols: int
    dirname: str
    disabled: bool
    form: str
    maxlength: int
    name: str
    placeholder: str
    readonly: bool
    required: bool
    rows: int
    wrap: Literal["hard", "soft"]


class FieldsetAttrs(GlobalAttrs, total=False):
    """Attributes for `<fieldset>` elements."""

    disabled: bool
    form: str
    name: str


class BlockquoteAttrs(GlobalAttrs, total=False):
    """Attributes for `<blockquote>` elements."""

    cite: str


class FormAttrs(GlobalAttrs, total=False):
    """Attributes for `<form>` elements."""

    accept_charset: str
    action: str
    autocomplete: Literal["on", "off"]
    enctype: Literal[
        "application/x-www-form-urlencoded",
        "multipart/form-data",
        "text/plain",
    ]
    method: Literal["get", "post"]
    name: str
    novalidate: bool
    rel: Literal[
        "external",
        "help",
        "license",
        "next",
        "nofollow",
        "noopener",
        "noreferrer",
        "opener",
        "prev",
        "search",
    ]
    target: str


class HyperlinkAttrs(GlobalAttrs, total=False):
    """Attributes for `<a>` elements."""

    download: str
    href: str
    hreflang: str
    media: str
    ping: str
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    rel: Literal[
        "alternate",
        "author",
        "bookmark",
        "external",
        "help",
        "license",
        "next",
        "nofollow",
        "noreferrer",
        "noopener",
        "prev",
        "search",
        "tag",
    ]
    target: str
    type: str


class ButtonAttrs(GlobalAttrs, total=False):
    """Attributes for `<button>` elements."""

    autofocus: bool
    disabled: bool
    form: str
    formaction: str
    formenctype: Literal[
        "application/x-www-form-urlencoded",
        "multipart/form-data",
        "text/plain",
    ]
    formmethod: Literal["get", "post"]
    formnovalidate: bool
    formtarget: str
    popovertarget: str
    popovertargetaction: Literal["show", "hide", "toggle"]
    name: str
    type: Literal["submit", "reset", "button"]
    value: str


class LabelAttrs(GlobalAttrs, total=False):
    """Attributes for `<label>` elements."""

    for_: Annotated[str, "for"]
    name: str


class TdAttrs(GlobalAttrs, total=False):
    """Attributes for `<td>` elements."""

    colspan: int
    headers: str
    rowspan: int


class ThAttrs(GlobalAttrs, total=False):
    """Attributes for `<th>` elements."""

    abbr: str
    colspan: int
    headers: str
    rowspan: int
    scope: Literal["col", "colgroup", "row", "rowgroup"]


class LiAttrs(GlobalAttrs, total=False):
    """Attributes for `<li>` elements."""

    value: int


class ImgAttrs(GlobalAttrs, total=False):
    """Attributes for `<img>` elements."""

    alt: str
    crossorigin: Literal["anonymous", "use-credentials"]
    height: int
    ismap: bool
    loading: Literal["eager", "lazy"]
    longdesc: str
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "unsafe-url",
    ]
    sizes: str
    src: str
    srcset: str
    usemap: str
    width: int


class SvgAttrs(GlobalAttrs, total=False):
    """Attributes for `<svg>` elements."""

    version: str
    xmlns: str
    height: int
    width: int
    view_box: Annotated[str, Alias("viewBox")]
    clip_path: Annotated[str, Alias("clip-path")]
    clip_rule: Annotated[str, Alias("clip-rule")]
    fill: str
    fill_rule: Annotated[str, Alias("fill-rule")]
    stroke: str
    stroke_dasharray: Annotated[str, Alias("stroke-dasharray")]
    stroke_dashoffset: Annotated[str, Alias("stroke-dashoffset")]
    stroke_linecap: Annotated[str, Alias("stroke-linecap")]
    stroke_linejoin: Annotated[str, Alias("stroke-linejoin")]
    stroke_miterlimit: Annotated[str, Alias("stroke-miterlimit")]
    stroke_opacity: Annotated[str, Alias("stroke-opacity")]
    stroke_width: Annotated[str, Alias("stroke-width")]
    transform: str


class CircleAttrs(SvgAttrs, total=False):
    """Attributes for `<circle>` elements."""

    cx: str
    cy: str
    r: str


class EllipseAttrs(SvgAttrs, total=False):
    """Attributes for `<ellipse>` elements."""

    cx: str
    cy: str
    rx: str
    ry: str
    path_length: Annotated[str, Alias("pathLength")]


class LineAttrs(SvgAttrs, total=False):
    """Attributes for `<line>` elements."""

    x1: str
    x2: str
    y1: str
    y2: str


class RectAttrs(SvgAttrs, total=False):
    """Attributes for `<rect>` elements."""

    x: str
    y: str
    rx: str
    ry: str
    path_length: Annotated[str, Alias("pathLength")]


class PathAttrs(SvgAttrs, total=False):
    """Attributes for `<path>` elements."""

    d: str


class PolylineAttrs(SvgAttrs, total=False):
    """Attributes for `<polyline>` elements."""

    points: str


class PolygonAttrs(SvgAttrs, total=False):
    """Attributes for `<polygon>` elements."""

    points: str
    path_length: Annotated[str, Alias("pathLength")]


class IframeAttrs(GlobalAttrs, total=False):
    """Attributes for `<iframe>` elements."""

    allow: str
    allowfullscreen: bool
    allowpaymentrequest: bool
    height: int
    frameborder: str
    loading: Literal["eager", "lazy"]
    name: str
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    sandbox: Literal[
        "allow-forms",
        "allow-pointer-lock",
        "allow-popups",
        "allow-same-origin",
        "allow-scripts",
        "allow-top-navigation",
    ]
    src: str
    srcdoc: str
    scrolling: str
    width: int


class ColAttrs(GlobalAttrs, total=False):
    """Attributes for `<col>` elements."""

    span: int


class DelAttrs(GlobalAttrs, total=False):
    """Attributes for `<del>` elements."""

    cite: str
    datetime: str


class InsAttrs(GlobalAttrs, total=False):
    """Attributes for `<ins>` elements."""

    cite: str
    datetime: str


class AreaAttrs(GlobalAttrs, total=False):
    """Attributes for `<area>` elements."""

    alt: str
    coords: str
    download: str
    href: str
    ping: str
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    rel: str
    shape: Literal["rect", "circle", "poly", "default"]
    target: str


class SourceAttrs(GlobalAttrs, total=False):
    """Attributes for `<source>` elements."""

    media: str
    sizes: str
    src: str
    srcset: str
    type: str


class AudioAttrs(GlobalAttrs, total=False):
    """Attributes for `<audio>` elements."""

    src: str
    preload: Literal["auto", "metadata", "none"]
    autoplay: bool
    controls: bool
    loop: bool
    muted: bool
    mediagroup: str


class BaseAttrs(GlobalAttrs, total=False):
    """Attributes for `<base>` elements."""

    href: str
    target: str


class CanvasAttrs(GlobalAttrs, total=False):
    """Attributes for `<canvas>` elements."""

    width: int
    height: int


class DataAttrs(GlobalAttrs, total=False):
    """Attributes for `<data>` elements."""

    value: str


class DetailsAttrs(GlobalAttrs, total=False):
    """Attributes for `<details>` elements."""

    open: bool


class DialogAttrs(GlobalAttrs, total=False):
    """Attributes for `<dialog>` elements."""

    open: bool


class EmbedAttrs(GlobalAttrs, total=False):
    """Attributes for `<embed>` elements."""

    height: int
    src: str
    type: str
    width: int


class MapAttrs(GlobalAttrs, total=False):
    """Attributes for `<map>` elements."""

    name: str


class MeterAttrs(GlobalAttrs, total=False):
    """Attributes for `<meter>` elements."""

    form: str
    high: int
    low: int
    max: int
    min: int
    optimum: int
    value: int


class ObjectAttrs(GlobalAttrs, total=False):
    """Attributes for `<object>` elements."""

    data: str
    form: str
    height: int
    name: str
    type: str
    typemustmatch: bool
    usemap: str
    width: int


class OlAttrs(GlobalAttrs, total=False):
    """Attributes for `<ol>` elements."""

    reversed: bool
    start: int
    type: Literal["1", "a", "A", "i", "I"]


class ProgressAttrs(GlobalAttrs, total=False):
    """Attributes for `<progress>` elements."""

    max: int
    value: int


class QAttrs(HtmlAttrs, total=False):
    """Attributes for `<q>` elements."""

    cite: str


class TimeAttrs(GlobalAttrs, total=False):
    """Attributes for `<time>` elements."""

    datetime: str


class TrackAttrs(GlobalAttrs, total=False):
    """Attributes for `<track>` elements."""

    default: bool
    kind: Literal[
        "subtitles", "captions", "descriptions", "chapters", "metadata"
    ]
    label: str
    src: str
    srclang: str


class VideoAttrs(GlobalAttrs, total=False):
    """Attributes for `<video>` elements."""

    autoplay: bool
    controls: bool
    height: int
    loop: bool
    muted: bool
    poster: str
    preload: Literal["auto", "metadata", "none"]
    src: str
    width: int
