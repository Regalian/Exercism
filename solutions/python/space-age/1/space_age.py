from typing import Callable, ClassVar

from enum import Enum


class ErrorMsg(Enum):
    INVALID_PLANET = "Invalid planet '{planet}'. Valid planets are: {valid_planets}"
    NO_SUCH_METHOD = "'{class_name}' object has no attribute '{name}'"


class SpaceAge:
    """Class representing a space age."""

    ORBITAL_PERIODS: ClassVar[dict[str, float]] = {
        "earth": 1,
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }
    DIGITS: ClassVar[int] = 2
    EARTH_YEAR_SECONDS: ClassVar[float] = 365.25 * 24 * 60 * 60

    def __init__(self, seconds: int):
        """Initialize a SpaceAge object with the given number of Earth seconds.

        Args:
            seconds (int): The number of Earth seconds to represent as a space age.
        """

        self.method_cache: dict[str, Callable[[], float]] = {}
        self.seconds = seconds

    def __getattr__(self, name: str, /) -> Callable[[], float]:
        """Dynamically handle on_<planet> calls"""
        if name in self.method_cache:
            return self.method_cache[name]
        if name.startswith("on_"):
            planet = name[3:]
            if planet in self.ORBITAL_PERIODS:
                self.method_cache[name] = lambda: round(
                    self.seconds
                    / (self.EARTH_YEAR_SECONDS * self.ORBITAL_PERIODS[planet]),
                    self.DIGITS,
                )
                return self.method_cache[name]
            else:
                raise AttributeError(
                    ErrorMsg.INVALID_PLANET.value.format(
                        planet=planet,
                        valid_planets=", ".join(self.ORBITAL_PERIODS.keys()),
                    )
                )
        # For non-planet attributes, give a generic error
        raise AttributeError(
            ErrorMsg.NO_SUCH_METHOD.value.format(
                class_name=self.__class__.__name__, name=name
            )
        )
