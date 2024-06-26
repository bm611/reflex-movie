import reflex as rx


def search():
    return rx.hstack(
        rx.input(
            class_name="w-full px-2 py-2 border rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        ),
        rx.button("Search"),
        class_name="py-10 flex max-w-sm justify-center mx-auto",
    )
