import reflex as rx
from typing import Dict, List


def movie_card(name: str, release_date: str, poster: str) -> rx.Component:
    return rx.box(
        rx.image(src=poster, class_name="w-full h-2/3 object-cover rounded-2xl mb-4"),
        rx.text(name, class_name="font-bold mt-2 text-sm md:text-base truncate"),
        rx.text(release_date, class_name="text-gray-500 text-xs md:text-sm"),
        class_name="w-full rounded-lg overflow-hidden transition-shadow duration-300",
    )


def movie_grid(movies: List[Dict[str, str]]) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.foreach(
                movies,
                lambda movie: movie_card(
                    name=movie["name"],
                    release_date=movie["release_date"],
                    poster=movie["poster"],
                ),
            ),
            class_name="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-6",
            wrap="wrap",
        ),
        class_name="w-full",
    )
