from nicegui import ui

from app.views.trip import trip_view


def main_view():
    with ui.splitter(value=30).classes("w-full h-screen p-0") as splitter:
        with splitter.before:
            trip_view()

        with splitter.after:
            ui.label("Right Panel").classes("text-center")
