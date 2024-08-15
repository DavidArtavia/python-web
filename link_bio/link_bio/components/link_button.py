import reflex as rx
import link_bio.styles.styles as styles


def link_button(title: str, body: str, url: str, icon_name: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(icon_name),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                ),
            ),
        ),
        href=url,
        is_external=True,
        width="100%",
    )
