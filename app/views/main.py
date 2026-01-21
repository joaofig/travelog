from nicegui import ui

from app.views.map import map_panel
from app.views.trip import trip_view


def main_view():
    with ui.splitter(value=30).classes("w-full h-screen p-0") as splitter:
        with splitter.before:
            trip_view()

        with splitter.after:
            map_panel()
