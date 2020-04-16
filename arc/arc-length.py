from math import sqrt, asin, pi


class Arc:
    def __init__(self, chord, sagitta):
        self.chord = chord
        self.sagitta = sagitta

    def arc_length(self):
        self.radius = (pow(self.chord / 2, 2) +
                             pow(self.sagitta, 2)) / (2 * self.sagitta)
        self.angle = asin((self.chord / 2) / self.radius)
        self.arc_length = (self.angle * 2) * self.radius

    def show_results(self):
        print(
            f"radius: {round(self.radius, 2)}, length: {round(self.arc_length, 2)}")


arc = Arc(1.8, 0.30)
arc.arc_length()
arc.show_results()
