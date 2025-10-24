from nicegui import ui

def Label(
        text: str = "", 
        clas: str|None = "", 
        props: str|None = "",
        styles: str|None = "",
        config: dict|None = None
    ):
    if not config: config = {}
    return ui.label(text=text, **config).classes(clas).props(props).style(styles)

def Header(
        clas: str|None = "", 
        props: str|None = "",
        styles: str|None = "",
        config: dict|None = None
    ):
    if not config: config = {}
    return ui.header(**config).classes(clas).props(props).style(styles)

def Footer(
        clas: str|None = "", 
        props: str|None = "",
        styles: str|None = "",
        config: dict|None = None
    ):
    if not config: config = {}
    return ui.footer(**config).classes(clas).props(props).style(styles)

def Card(
        clas: str|None = "", 
        props: str|None = "",
        styles: str|None = "",
        align: str|None = None
    ):
    return ui.card(align_items=align).classes(clas).props(props).style(styles)

def Link(
        text: str = "",
        link: str = "",
        new_tab: bool = False,
        clas: str|None = "", 
        props: str|None = "",
        styles: str|None = "",
    ):
    return ui.link(text, link, new_tab).classes(
        "hover:underline text-white"
    ).classes(clas).props(props).style(styles)

def LinkBtn(
        text: str = "",
        link: str = "",
        new_tab: bool = False,
        clas: str|None = "", 
        props: str|None = "",
        styles: str|None = "",
    ):
    return ui.link(text, link, new_tab).classes(
        "px-3 py-2 text-white rounded-md no-underline shadow-sm bg-btn transition-all duration-200"
        ).classes(clas).props(props).style(styles)

def Input(
        clas: str|None = "", 
        props: str|None = "",
        styles: str|None = "",
        model = None,
        **kwargs
    ):
    inp = ui.input(**kwargs).props("dense outlined").classes(clas).props(props).style(styles)
    if model:
        inp.bind_value_to(model, 'value')
    return inp

def Button(
        text: str = "", 
        on_click = lambda: (),
        clas: str|None = "", 
        props: str|None = "",
        styles: str|None = "",
        config: dict|None = None
    ):
    if not config: config = {}
    return ui.button(text=text, on_click=on_click, **config).classes(clas).props(props).style(styles)
