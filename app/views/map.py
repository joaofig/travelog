from nicegui import ui

from lib.controls.LeafletMap import LeafletMap
from lib.models.geo.GeoBounds import GeoBounds
from lib.models.geo.LatLng import LatLng
from lib.tasks.managed import ManagedTasks


async def setup_map(m: LeafletMap) -> None:
    await m.initialized()

    m.fit_bounds(
        bounds=GeoBounds(
            LatLng(42.2203052778, -83.8042902778),
            LatLng(42.3258, -83.674),
        )
    )


def map_view():
    # main_splitter = ui.splitter(horizontal=True, value=70)
    # main_splitter.classes("w-full h-full")

    draw_control = {
        "position": "topleft",
        "draw": {
            "polygon": True,
            "polyline": False,
            "rectangle": True,
            "circle": True,
            "marker": False,
            "circlemarker": False,
        },
        "edit": False,
    }

    m = (
        LeafletMap(
            draw_control=draw_control,
            hide_drawn_items=True,
        )
        .classes("h-full w-full")
    )
    ManagedTasks().create(setup_map(m))
    return m


def map_panel():
    main_splitter = ui.splitter(horizontal=True, value=70)
    main_splitter.classes("w-full h-full")

    with main_splitter:
        with main_splitter.before:
            leaflet = map_view()

        with main_splitter.after:
            ui.label("Bottom Panel").classes("text-center")
