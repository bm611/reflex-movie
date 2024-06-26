"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.heading(
            "Movie Flix",
            class_name="text-3xl md:text-4xl underline lg:text-5xl font-bold text-center text-amber-400 leading-tight mt-4 mb-4",
        ),
        # search bar
        rx.hstack(
            rx.input(
                class_name="w-full px-2 py-2 border rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            ),
            rx.button("Search"),
            class_name="py-10 flex max-w-sm justify-center mx-auto",
        ),
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
