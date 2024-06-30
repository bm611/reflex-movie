"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from reflex_movie.components.search_bar import search
from reflex_movie.components.nav import nav
from reflex_movie.components.movie_card import movie_grid
from reflex_movie.components.movie_details import render_movie_details
from reflex_movie.components.search_details import render_search_results
from reflex_movie.api.endpoints import (
    get_popular,
    get_movie_details,
    get_search_results,
)

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

    current_movie_details: Dict[str, str] = {}

    @rx.var
    def get_movie_id(self) -> str:
        return self.router.page.params.get("movie_id", "")

    def fetch_movie_details(self) -> None:
        movie_id = self.get_movie_id
        if movie_id:
            movie = get_movie_details(movie_id)
            self.current_movie_details = {
                "bg_image": f"https://image.tmdb.org/t/p/original/{movie['backdrop_path']}",
                "runtime": movie["runtime"],
                "budget": movie["budget"],
                "rating": movie["vote_average"],
            }
        else:
            self.current_movie_details = {}

    @rx.var
    def get_search_query(self) -> str:
        return self.router.page.params.get("query", "")

    def fetch_search_details(self):
        if self.get_search_query:
            print("flag", self.get_search_query)
            movies: List[Dict[str, str]] = [
                {
                    "name": movie["original_title"],
                    "release_date": movie["release_date"],
                    "poster": f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}",
                    "movie_id": movie["id"],
                }
                for movie in get_search_results(self.get_search_query)
            ]


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
            class_name="w-full max-w-7xl p-6 space-y-4",
        ),
        width="100%",
    )


@rx.page(route="/movie/[movie_id]", on_load=State.fetch_movie_details)
def display_details() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            nav(),
            render_movie_details(State),
            class_name="w-full max-w-7xl p-4 space-y-4",
        )
    )


@rx.page(route="/search/[query]", on_load=State.fetch_search_details)
def display_search_details() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            # nav bar
            nav(),
            # search bar
            search(),
            rx.heading(State.get_search_query),
            rx.heading("Search Results", class_name="text-center mb-4 font-bold"),
            # movie_grid(State.movies),
            rx.logo(),
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
