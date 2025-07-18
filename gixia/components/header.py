import reflex as rx
from gixia.states.base_state import BaseState
from gixia.components.login import login_button


def header() -> rx.Component:
    return rx.hstack(
        rx.spacer(),
        rx.cond(
            BaseState.user_name,
            rx.link(
                rx.button(
                    BaseState.user_name,
                    background_color="transparent",
                    border="none",
                    color=rx.color_mode_cond(
                        light="black",
                        dark="white",
                    ),
                    cursor="pointer",
                ),
                href="/profile",
                is_external=False,
            ),
            login_button(),
        ),
        rx.color_mode.button(),
        spacing="2",
    )