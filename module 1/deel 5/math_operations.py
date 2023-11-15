import math 

def increment(nr: float) -> float:
  return nr + 1

def decrement(nr: float) -> float:
  return nr - 1

def add(nr1: float, nr2: float) -> float:
  return nr1 + nr2

def substract(nr1: float,nr2:float) -> float:
  return nr1 - nr2

def multiply(nr1: float,nr2: float) -> float:
  return nr1 * nr2

def divide(nr1: float,nr2: float) -> float:
  if nr2 == 0:
    return None
  else:
    return nr1 / nr2

def even(nr1: int, nr2: int) -> str:
  return nr1 == nr2

def een_groter(nr1: int,nr2: int) -> str:
  return nr1 > nr2

def twee_groter(nr1: int,nr2: int) -> str:
  return nr1 < nr2

def calculate_cilinder_content (diameter: float, hoogte: float) -> float:
  return (diameter / 2) * (diameter / 2) * math.pi * hoogte

