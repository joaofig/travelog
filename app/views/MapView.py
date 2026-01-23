from nicegui import ui, binding

from lib.controls.LeafletMap import LeafletMap
from lib.models.geo.GeoBounds import GeoBounds
from lib.models.geo.LatLng import LatLng
from lib.tasks.managed import ManagedTasks


@binding.bindable_dataclass
class MapView:
    _map: LeafletMap

    def __init__(self):
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

        self._map = (
            LeafletMap(
                draw_control=draw_control,
                hide_drawn_items=True,
            )
            .classes("h-full w-full")
        )
        ManagedTasks().create(self.setup_map())

    async def setup_map(self) -> None:
        await self._map.initialized()

        self._map.fit_bounds(
            bounds=GeoBounds(
                LatLng(42.2203052778, -83.8042902778),
                LatLng(42.3258, -83.674),
            )
        )