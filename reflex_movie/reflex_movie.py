"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .components.search_bar import search
from .components.nav import nav

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        # nav bar
        nav(),
        # search bar
        search(),
        # reflex logo footer
        rx.logo(),
        class_name="",
    )


style = {
    "font_family": "Monaspace Krypton",
    "font_size": "16px",
}

app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="amber",
    ),
    stylesheets=[
        "/fonts/myfonts.css",
    ],
    style=style,
)
app.add_page(index)
