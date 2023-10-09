# Created by : szymoslav, mikolaj m

from manim import *

class AbsoluteValueGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-12, 14],
            y_range=[-12, 15],
            axis_config={"color": BLUE},
        )

        graph = axes.plot(lambda x: abs((-(abs(x-2) + 6) + 18)), color=WHITE)

        graph_label = axes.get_graph_label(graph, label="f(x)")

        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(2)
