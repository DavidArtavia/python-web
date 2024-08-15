from enum import Enum
import reflex as rx

# constants
MAX_WIDTH = "600px"


# sizes
class Size(Enum):
    SMALL = "0.5em"  # em toma el tamano de fuente generico de la aplicacion
    DEFAULT = "1em"
    MEDIUM = "0.8em"
    BIG = "2em"


# Styles que afectan los elementos globalmente
BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
    },
    rx.link: {"text_decoration": "none", "_hover": {}},
}

# un diccionario de propiedades con un estilo propio
button_title_style = dict(
    font_size=Size.DEFAULT.value,
)
button_body_style = dict(
    font_size=Size.MEDIUM.value,
)
