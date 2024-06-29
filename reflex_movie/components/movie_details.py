import reflex as rx


def render_movie_details(State) -> rx.Component:
    return rx.vstack(
        rx.image(State.current_movie_details["bg_image"], class_name="rounded-3xl"),
        rx.unordered_list(
            rx.text("Runtime: ", State.current_movie_details["runtime"], " mins"),
            rx.text(
                "Budget: $",
                State.current_movie_details["budget"],
            ),
            rx.text("Rating : ", State.current_movie_details["rating"]),
        ),
        class_name="w-full max-w-7xl px-8 space-y-10",
    )
