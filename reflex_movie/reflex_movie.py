"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex_movie.components.search_bar import search
from reflex_movie.components.nav import nav
from reflex_movie.components.movie_card import movie_card, movie_grid
from reflex_movie.api.endpoints import get_popular

from rxconfig import config
from typing import Dict, List


class State(rx.State):
    """The app state."""

    movies: List[Dict[str, str]] = [
        {
            "name": movie["original_title"],
            "release_date": movie["release_date"],
            "poster": f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}",
        }
        for movie in get_popular()
    ]


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        # nav bar
        nav(),
        # search bar
        search(),
        # display popular movies
        rx.heading("Popular Movies", class_name="text-left font-bold"),
        movie_grid(State.movies),
        # rx.unordered_list(rx.foreach(State.movies, lambda item: rx.list_item(item))),
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
