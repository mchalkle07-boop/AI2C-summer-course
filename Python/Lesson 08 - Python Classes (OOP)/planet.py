class Planet():
    def __init__(self, 
                 name: str, 
                 coordinates: tuple[float, float, float], 
                 danger: int, 
                 resources: float, 
                 atmosphere: str
                 ):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere
#overwrite __str__?
    def __str__(self) -> str:
        # pass
        return (
        f"Planet {self.name} is at Coordinates: ({self.coordinates[0]}, {self.coordinates[1]}, {self.coordinates[2]}), "
        f"Danger: {self.danger}, Resources: {self.resources}, Atmosphere: {self.atmosphere}"
        )

#overwrite built-in methhod to calculate distance between two planets
    # def __sub__(self, p1_coordinates: tuple[float, float, float], p2_coordinates: tuple[float, float, float]):
    #     self.planet1 = p1_coordinates
    #     self.planet2 = p2_coordinates
    #     return p1_coordinates - p2_coordinates

    def __sub__(self, other) -> float:
        if not isinstance(other, Planet):
            raise TypeError("Must only subtract planets")
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates

        return ((x1 - y2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** (1/2)


if __name__ == "__main__":
# Planets:
    earth = Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earthish")
    mars = Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin Boi"),
    jupiter = Planet("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Boi"),
    saturn = Planet("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gassey Boi"),
    Uranus = Planet("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Vanilla Ice"),
    neptune = Planet("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Vanilla Ice"),
    pluto = Planet("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Let it go, let it go"),
    eris = Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Do you want to build a snowman?!"),
    kepler = Planet("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like, but no proof"),
    proxima = Planet("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown, actually the honest answer")

