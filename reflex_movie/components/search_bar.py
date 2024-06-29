import reflex as rx


def search():
    return rx.hstack(
        rx.input(
            class_name="w-full px-2 py-2 border rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        ),
        rx.button(
            "Search",
            class_name="inline-flex items-center justify-center rounded-xl bg-amber py-3 px-6 font-dm text-base font-medium text-white shadow-xl shadow-amber-400/75 transition-transform duration-200 ease-in-out hover:scale-[1.02]",
        ),
        class_name="py-10 flex justify-center mx-auto",
    )
