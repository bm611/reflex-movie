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
            "movie_id": movie["id"],
        }
        for movie in get_popular()
    ]

    @rx.var
    def get_movie_id(self) -> str:
        return self.router.page.params.get("movie_id", "")


@rx.page(route="/", title="Movie Flix")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.center(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            # nav bar
            nav(),
            # search bar
            search(),
            # display popular movies
            rx.heading("Popular Movies", class_name="text-center mb-4 font-bold"),
            movie_grid(State.movies),
            # reflex logo footer
            rx.logo(),
            class_name="w-full max-w-7xl p-4 space-y-4",
        ),
        width="100%",
    )


@rx.page(route="/movie/[movie_id]")
def display_details() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            nav(),
        )
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
