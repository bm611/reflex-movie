import reflex as rx


def render_movie_details(State) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(
                src=State.current_movie_details["bg_image"],
                class_name="rounded-3xl w-full max-w-screen-lg mx-auto",
            ),
            rx.vstack(
                rx.text(
                    f"Runtime: {State.current_movie_details['runtime']} mins",
                    class_name="text-black-300",
                ),
                rx.text(
                    f"Budget: ${State.current_movie_details['budget']}",
                    class_name="text-black-300",
                ),
                rx.text(
                    f"Rating: {State.current_movie_details['rating']}",
                    class_name="text-black-300",
                ),
                class_name="space-y-2 w-full",
            ),
            class_name="w-full max-w-7xl px-4 sm:px-8 space-y-6",
        ),
        class_name="w-full",
    )
