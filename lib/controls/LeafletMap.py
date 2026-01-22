from typing import Self, Dict, Union

from nicegui import ui

from lib.models.geo.GeoBounds import GeoBounds


class LeafletMap(ui.leaflet):
    def __init__(
            self,
            draw_control: Union[bool, Dict] = False,
            hide_drawn_items: bool = False,
            options=None,
            **kwargs):
        if not options:
            options = {}

        ui.leaflet.__init__(
            self,
            draw_control=draw_control,
            hide_drawn_items=hide_drawn_items,
            options=options,
            **kwargs,
        )
        # self.add_control(ui.leaflet.zoom_control())
        # self.add_control(ui.leaflet.fullscreen_control())
        # self.add_control(ui.leaflet.scale_control())

    def invalidate_size(self, animate: bool = False) -> Self:
        self.run_map_method("invalidateSize", animate)
        return self

    def fit_bounds(self, bounds: GeoBounds, options: Dict | None = None) -> Self:
        bounds_list = [[bounds.sw.lat, bounds.sw.lng], [bounds.ne.lat, bounds.ne.lng]]
        self.run_map_method("fitBounds", bounds_list, options)
        return self

    def zoom_in(self) -> Self:
        self.run_map_method("zoomIn")
        return self

    def zoom_out(self) -> Self:
        self.run_map_method("zoomOut")
        return self
