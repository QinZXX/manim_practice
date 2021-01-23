from manim import *

class MyEnd(Scene):
    def construct(self):       
        th1 = Text("Made with Python", gradient=(BLUE, GREEN))
        th12 = Text("Mathematical animation engine:", gradient=(YELLOW, RED))
        th2 = Text("Manim by @Grant Sanderson", gradient=(YELLOW, RED))
        th3 = Text('Author: QinZXX', gradient=(GREEN, BLUE)).shift(DOWN * 2)
        th4 = Text("End", size=2, gradient=(GREEN, BLUE))
        self.play(Write(th1))
        self.play(ApplyMethod(th1.shift, UP * 3))
        self.play(Write(th12))
        self.play(ApplyMethod(th12.shift, UP * 1))
        self.play(Write(th2))
        self.wait(1)
        self.play(Write(th3))
        self.wait(2)
        self.play(FadeOut(th1), FadeOut(th12), FadeOut(th2), FadeOut(th3))
        self.play(Write(th4))
        self.wait(3)

