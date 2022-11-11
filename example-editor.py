# example.py

from manim import *

# or: from manimlib import *
from manim_editor import *


class Example(Scene):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        self.play(GrowFromCenter(circle))
        self.next_section(type=PresentationSectionType.NORMAL)

        self.wait()
        self.next_section(type=PresentationSectionType.COMPLETE_LOOP)

        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)

        self.next_section(type=PresentationSectionType.NORMAL)

        self.play(dot.animate.move_to(ORIGIN))

        self.next_section(type=PresentationSectionType.NORMAL)

        self.wait()
