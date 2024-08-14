"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.flex(
         rx.text(
                "hola mundo e"
            ),
         rx.flex(
                 rx.text(
        "This is a ",
        rx.text.strong("paragraph"),
        " element.",
        as_="p",
    ),
    rx.text(
        "This is a ",
        rx.text.strong("label"),
        " element.",
        as_="label",
    ),
    rx.text(
        "This is a ",
        rx.text.strong("div"),
        " element.",
        as_="div",
    ),
    rx.text(
        "This is a ",
        rx.text.strong("span"),
        " element.",
        as_="span",
    ),
    direction="column",
    spacing="3",
               
         ),
         
         
       
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
