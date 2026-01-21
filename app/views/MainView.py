from nicegui import ui

from app.views.TripView import TripView


class MainView:
    def __init__(self):
        with ui.splitter(value=30).classes("w-full h-screen p-0") as splitter:
            with splitter.before:
                TripView()

            with splitter.after:
                ui.label("Right Panel").classes("text-center")