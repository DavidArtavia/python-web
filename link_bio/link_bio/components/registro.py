import reflex as rx
from link_bio.backend import create_connection, insert_student


class RegistroState(rx.State):

    nombre: str = ""
    carne: str = ""
    plan_estudios: int = 0
    herencia_martes: int = 0
    herencia_jueves: int = 0
    asignado_martes_1: int = 0
    asignado_jueves_1: int = 0
    asignado_martes_2: int = None
    asignado_jueves_2: int = None
    asignado_martes_3: int = None
    asignado_jueves_3: int = None
    casos_asignados_mes: int = None
    total_casos_mes: int = None
    profesora_guia: str = ""

    def submit(self):
        connection = create_connection()
        if connection:
            try:
                insert_student(
                    connection,
                    self.nombre,
                    self.carne,
                    self.plan_estudios,
                    self.herencia_martes,
                    self.herencia_jueves,
                    self.asignado_martes_1,
                    self.asignado_jueves_1,
                    self.asignado_martes_2,
                    self.asignado_jueves_2,
                    self.asignado_martes_3,
                    self.asignado_jueves_3,
                    self.casos_asignados_mes,
                    self.total_casos_mes,
                    self.profesora_guia,
                )
                # Limpiar los campos después de un envío exitoso
                # self.clear_fields()

                # Mostrar notificación de éxito
                # rx.toast(
                #     title="Registro exitoso",
                #     description="El estudiante ha sido registrado correctamente.",
                #     status="success",
                #     duration=5000,  # Duración en milisegundos
                #     is_closable=True,
                # )
            except Exception as e:
                # Mostrar notificación de error si hay un problema
                rx.toast(
                    title="Error",
                    description=f"Error al registrar: {str(e)}",
                    status="error",
                    duration=500000,  # Duración en milisegundos
                    is_closable=True,
                )
            finally:
                connection.close()

    def clear_fields(self):
        self.nombre = ""
        self.carne = ""
        self.plan_estudios = 0
        self.herencia_martes = 0
        self.herencia_jueves = 0
        self.asignado_martes_1 = 0
        self.asignado_jueves_1 = 0
        self.asignado_martes_2 = None
        self.asignado_jueves_2 = None
        self.asignado_martes_3 = None
        self.asignado_jueves_3 = None
        self.casos_asignados_mes = None
        self.total_casos_mes = None
        self.profesora_guia = ""


def registro_form() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Nombre",
                        value=RegistroState.nombre,
                        on_change=RegistroState.set_nombre,
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Carné",
                        value=RegistroState.carne,
                        on_change=RegistroState.set_carne,
                        width="100%",
                    ),
                    rx.input(
                        type="number",
                        placeholder="Plan de estudios",
                        value=RegistroState.plan_estudios,
                        on_change=RegistroState.set_plan_estudios,
                        width="100%",
                    ),
                    rx.input(
                        type="number",
                        placeholder="Herencia Martes",
                        value=RegistroState.herencia_martes,
                        on_change=RegistroState.set_herencia_martes,
                        width="100%",
                    ),
                    rx.input(
                        type="number",
                        placeholder="Herencia Jueves",
                        value=RegistroState.herencia_jueves,
                        on_change=RegistroState.set_herencia_jueves,
                        width="100%",
                    ),
                    rx.input(
                        type="number",
                        placeholder="Asignado Martes 1",
                        value=RegistroState.asignado_martes_1,
                        on_change=RegistroState.set_asignado_martes_1,
                        width="100%",
                    ),
                    rx.input(
                        type="number",
                        placeholder="Asignado Jueves 1",
                        value=RegistroState.asignado_jueves_1,
                        on_change=RegistroState.set_asignado_jueves_1,
                        width="100%",
                    ),
                    rx.input(
                        type="number",
                        placeholder="Asignado Martes 2",
                        value=RegistroState.asignado_martes_2,
                        on_change=RegistroState.set_asignado_martes_2,
                        width="100%",
                    ),
                    rx.input(
                        type="number",
                        placeholder="Asignado Jueves 2",
                        value=RegistroState.asignado_jueves_2,
                        on_change=RegistroState.set_asignado_jueves_2,
                        width="100%",
                    ),
                    rx.input(
                        type="number",
                        placeholder="Casos Asignados Mes",
                        value=RegistroState.casos_asignados_mes,
                        on_change=RegistroState.set_casos_asignados_mes,
                        width="100%",
                    ),
                    rx.input(
                        type="number",
                        placeholder="Total Casos Mes",
                        value=RegistroState.total_casos_mes,
                        on_change=RegistroState.set_total_casos_mes,
                        width="100%",  # Ajuste de ancho
                    ),
                    rx.input(
                        placeholder="Profesora Guía",
                        value=RegistroState.profesora_guia,
                        on_change=RegistroState.set_profesora_guia,
                        width="100%",  # Ajuste de ancho
                    ),
                    rx.button(
                        "Enviar",
                        on_click=lambda: [
                            RegistroState.submit(),
                            rx.toast(
                                title="Registro exitoso",
                                description="El estudiante ha sido registrado correctamente.",
                                status="success",
                                duration=20000,  # Duración de la notificación en ms
                                is_closable=True,
                            )],
                        width="100%",
                        height="50px",
                        bg="purple.600",  # Cambiar color del botón a un morado similar al ejemplo
                        color="white",
                        border_radius="md",
                        _hover={
                            "bg": "purple.700"
                        },  # Cambia el color cuando pasas el mouse
                        mt="6",  # Margen superior para separar el botón de los inputs
                    ),
                    
                    spacing="4",  # Espaciado entre los inputs
                ),
                reset_on_submit=True,  # Resetea el formulario tras enviarlo
            ),
            rx.divider(),  # Línea divisora bajo el formulario
            rx.heading(
                "Results", size="md"
            ), 
        ),
        py="8",
    )
