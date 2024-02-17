"""althea/althea.py"""

import reflex as rx


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    """Home Page"""
    return rx.center(
        rx.vstack(
            rx.heading("Althea", size="9"),
            rx.input(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)
