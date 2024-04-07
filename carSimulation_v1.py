#Solution from Leetcode

from dataclasses import dataclass
from typing import Optional, List, Tuple

@dataclass
class Light:
  x: int
  y: int
  is_green: bool = True

@dataclass
class Road:
  x: Optional[int]
  y: Optional[int]

  @property
  def is_vertical(self):
    return self.y is None

@dataclass
class Car:
  x: int
  y: int
  direction: int    # 0 => increasing y, 1 => increasing x, 2 => decreasing y, 3 => decreasing x

class Map:
  roads: List[Road] # technically unused after __init__
  lights: List[Light]
  city_limits_min: Tuple[int, int]
  city_limits_max: Tuple[int, int]

  def __init__(self, roads: List[Road], city_limits_min: Tuple[int, int], city_limits_max: Tuple[int, int]):
    self.lights = []
    for r1 in roads:
      for r2 in roads:
        if r1.is_vertical and not r2.is_vertical:
          self.lights.append(Light(r1.x, r2.y))
    self.roads = roads
    self.city_limits_min = city_limits_min
    self.city_limits_max = city_limits_max

  def simulate_car(self, car: Car):
    time_count = 0
    while self.city_limits_min[0] <= car.x <= self.city_limits_max[0] and self.city_limits_min[1] <= car.y <= self.city_limits_max[1]:
      time_count += 1
      if not any((light.x, light.y) == (car.x, car.y) and not light.is_green for light in self.lights):
        if car.direction == 0: car.y += 1
        if car.direction == 1: car.x += 1
        if car.direction == 2: car.y -= 1
        if car.direction == 3: car.x -= 1
      for light in self.lights:
        light.is_green = not light.is_green
    return time_count

# testing using the given case
J = Road(1, None)
A = Road(None, 1)
B = Road(None, 2)

m = Map([J, A, B], (0, 0), (2, 3))
assert m.simulate_car(Car(1, 0, 0)) == 6