from UI import LabeledInput, Card, Center, Label, INIT_THEME, Button
from lib.formHandler import Variable, Form

variables = [
    Variable("identifier", ""),
    Variable("password", ""),
]
form = Form(variables)

inputs_and_labels = [
    [
        dict(
            email = dict(
                text = "Email/Password *",
                clas = "text-lg font-bold",
            )
        ),
        dict(
            email = dict(
                placeholder = "Your email or name...",
                model = form.identifier,
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
        )
    ]
]

async def create():
    INIT_THEME()
    with Center(clas="w-full h-full"):
        with Card("max-w-md w-full h-fit flex flex-col"):
            Label("Login", "w-full border-b-2 text-2xl font-bold text-center")
            for i in inputs_and_labels:
                LabeledInput(*i)
            Label("", "w-full border-1")
            Button("Login", lambda:(), "w-full")