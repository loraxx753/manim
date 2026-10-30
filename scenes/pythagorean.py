from manim import *


def square_outward(p1, p2, inside_point, **kwargs):
    """Square on p1→p2 on the side opposite inside_point (outside the triangle)."""
    edge = p2 - p1
    n1 = rotate_vector(edge, PI / 2)
    n2 = rotate_vector(edge, -PI / 2)
    mid = (p1 + p2) / 2
    normal = n1 if np.dot(n1, inside_point - mid) < 0 else n2
    return Polygon(p1, p2, p2 + normal, p1 + normal, **kwargs)


class PythagoreanTheorem(Scene):
    """Right triangle with side squares revealing a^2 + b^2 = c^2."""

    def construct(self):
        scale = 0.55
        A = LEFT * 1.5 + DOWN * 1.2
        B = A + RIGHT * 3 * scale
        C = A + UP * 4 * scale
        inside = (A + B + C) / 3

        triangle = Polygon(A, B, C, color=WHITE, stroke_width=4)
        right_angle = RightAngle(Line(A, B), Line(A, C), length=0.28, color=YELLOW)

        label_a = MathTex("a").next_to(Line(A, B), DOWN, buff=0.12)
        label_b = MathTex("b").next_to(Line(A, C), LEFT, buff=0.12)
        mid_c = (B + C) / 2
        edge_c = C - B
        n_c = rotate_vector(edge_c, PI / 2)
        if np.dot(n_c, inside - mid_c) > 0:
            n_c = -n_c
        label_c = MathTex("c").move_to(mid_c + normalize(n_c) * 0.35)

        square_kwargs = dict(fill_opacity=0.4, stroke_width=2)
        square_a = square_outward(A, B, inside, color=BLUE, **square_kwargs)
        square_b = square_outward(C, A, inside, color=GREEN, **square_kwargs)
        square_c = square_outward(B, C, inside, color=RED, **square_kwargs)

        eq = MathTex("a^2", "+", "b^2", "=", "c^2")
        eq[0].set_color(BLUE)
        eq[2].set_color(GREEN)
        eq[4].set_color(RED)
        eq.to_edge(UP)

        self.play(Create(triangle), Create(right_angle))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.play(FadeIn(square_a), FadeIn(square_b))
        self.play(FadeIn(square_c))
        self.play(Write(eq))
        self.wait(1.5)
