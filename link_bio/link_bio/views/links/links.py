import reflex as rx
from link_bio.components.link_button import link_button


def links() -> rx.Component:
    return rx.box(
        rx.vstack(
            link_button("YouTube","tutoriales cada semana", "https://www.youtube.com/@davidarias113", "youtube"),
            link_button("Twitch","directos cada dia", "https://www.twitch.tv/", "twitch"),
            link_button("Discord","anuncios diarios", "https://discord.com/", "disc"),
            link_button(
                "instagram",
                "las ultimas noticias",
                "https://www.instagram.com/davidartavia911/?hl=es-es",
                "instagram",
            ),
            align_items="center",
            width="100%",
        ),
        width="100%",
    )
