import random

class Generator:
  def __init__(self):
    pass

  def generate_lines(self, limit_w, limit_h, amount_lines:int):
    for _ in range(amount_lines):
      yield [
        (random.randint(0, limit_w), random.randint(0, limit_h)),
        (random.randint(0, limit_w), random.randint(0, limit_h))
      ]