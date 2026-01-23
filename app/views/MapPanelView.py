from nicegui import ui, binding

from app.views.MapView import MapView


@binding.bindable_dataclass
class MapPanelView():
    def __init__(self):
        super().__init__()

        # map_view = MapView()

        main_splitter = ui.splitter(horizontal=True, value=70)
        main_splitter.classes("w-full h-full")

        with main_splitter:
            with main_splitter.before:
                map_view = MapView()

            with main_splitter.after:
                ui.label("Bottom Panel").classes("text-center")
