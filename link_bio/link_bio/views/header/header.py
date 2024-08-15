import reflex as rx

def header()-> rx.Component:
    return(
        
        rx.vstack(
            rx.center(
                
             rx.avatar(variant="soft", high_contrast=True,fallback="DV", color_scheme="red", size="xl", name="David", radius="full"),
             rx.text("HOLA MI NOMBRE ES DAVID ARTAVIA"),
             rx.text("Soy estudiante de la carrera de informatica empresarial de la UCR, mi objetivo es ser desarrollador fullstack"),
             direction="column",
             justify="center",
             align="center",
             spacing="2",
            ),
            spacing="2",
        )
    )