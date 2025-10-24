from UI import LabeledInput, Card, Center, Label, INIT_THEME, Button
from library.formHandler import Variable, Group
from backend import ControlAuth

def signup():
    pass

form_variables = [
    Variable("name", ""),
    Variable("email", ""),
    Variable("password", ""),
    Variable("confirm", ""),
]
errs_variables = [
    Variable("name", ""),
    Variable("email", ""),
    Variable("password", ""),
    Variable("confirm", ""),
]

form = Group(form_variables)
errs = Group(errs_variables)
inputs_and_labels = [
    [
        dict(
            name = dict(
                text = "Name *",
                clas = "text-lg font-bold",
            )
        ),
        dict(
            name = dict(
                placeholder = "Dispaly name...",
                model = form.name,
            )
        ),
    ],
    [
        dict(
            email = dict(
                text = "Email *",
                clas = "text-lg font-bold",
            )
        ),
        dict(
            email = dict(
                placeholder = "Email...",
                model = form.email,
            )
        ),
    ],
    [
        dict(
            password = dict(
                text = "Password *",
                clas = "text-lg font-bold",
            )
        ),
        dict(
            password = dict(
                placeholder = "Password...",
                password = True,
                password_toggle_button = True,
                clas="mb-2",
                model = form.password,
            ),
            confirm = dict(
                placeholder = "Confirm...",
                password = True,
                password_toggle_button = True,
            )
        ),
    ]
]

async def create():
    INIT_THEME()
    with Center(clas="w-full h-full"):
        with Card("max-w-md w-full h-fit flex flex-col"):
            Label("Sign Up", "w-full border-b-2 text-2xl font-bold text-center")
            for i in inputs_and_labels:
                LabeledInput(*i)
            Label("", "w-full border-1")
            Button("Create Account", lambda:(), "w-full")