"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.components.registro import registro_form
from link_bio.views.header.header import header
from link_bio.views.links.links import links
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
            ),
        ),
        registro_form(),
       
        footer(),
    )


app = rx.App(style=styles.BASE_STYLE)
app.add_page(index)
