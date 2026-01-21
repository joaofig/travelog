from nicegui import ui


class TripView(ui.column):
    def __init__(self):
        super().__init__()
        ui.label("Left Panel").classes("text-center")
