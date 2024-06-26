import reflex as rx


def nav() -> rx.Component:
    return rx.heading(
        "Movie Flix",
        class_name="text-3xl md:text-4xl underline lg:text-5xl font-bold text-center text-amber-400 leading-tight mt-4 mb-4",
    )
