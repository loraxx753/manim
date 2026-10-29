from manim import *


class HelloAxes(Scene):
    """Minimal axes + sine curve to prove the install works."""

    def construct(self):
        axes = Axes(
            x_range=[-PI, PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=4,
            axis_config={"include_tip": True},
        )
        labels = axes.get_axis_labels(
            x_label=Text("x", font_size=28),
            y_label=Text("y", font_size=28),
        )
        graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        graph_label = Text("y = sin(x)", font_size=36).next_to(graph, UP)

        self.play(Create(axes), Write(labels))
        self.play(Create(graph), FadeIn(graph_label))
        self.wait(1)
