from manim import *


class MathTexSmoke(Scene):
    """Prove TeX is wired up: MathTex must compile, not fall back to Text."""

    def construct(self):
        formula = MathTex(r"e^{i\pi} + 1 = 0")
        self.play(Write(formula))
        self.wait(0.5)
