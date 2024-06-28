import reflex as rx


def nav() -> rx.Component:
    return rx.box(
        rx.heading(
            "Movie Flix",
            class_name="text-3xl md:text-4xl underline lg:text-5xl font-bold text-amber-400 leading-tight",
        ),
        class_name="w-full text-center mt-8",
    )
