from dataclasses import dataclass
from typing import Self

from lib.models.geo.LatLng import LatLng


@dataclass
class GeoBounds:
    sw: LatLng
    ne: LatLng

    def merge(self, other: Self) -> Self:
        return GeoBounds(
            sw=LatLng(min(self.sw.lat, other.sw.lat), min(self.sw.lng, other.sw.lng)),
            ne=LatLng(max(self.ne.lat, other.ne.lat), max(self.ne.lng, other.ne.lng)),
        )
