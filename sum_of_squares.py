from manim import *


class SumOfSquares(Scene):
    def construct(self):
        zh = Text("��Ȼ��ƽ���͹�ʽ��֤��",gradient=(BLUE, GREEN))
        self.play(Write(zh))
        self.wait(2.5)

        text1=MathTex(
            "1^2+2^2+3^2+...+n^2=?"
        )
        self.play(ReplacementTransform(zh,text1))
        self.wait(2.5)
        self.play(FadeOut(text1))
        # framebox1 = SurroundingRectangle(text[1], buff = .1)
        # self.play(FadeOut(text1))
        # self.play(ShowCreation(framebox1))
        # self.play(
            # ReplacementTransform(framebox1,framebox2)
            # ApplyMethod(framebox1.next_to,text[2],RIGHT)
            # ApplyMethod(framebox1.next_to,text[3],LEFT) # bad
        # )
        zh2=Text("�����ǣ�",gradient=( GREEN,BLUE)).move_to(UP)
        self.play(Write(zh2))
        res=MathTex(
            "1^2+2^2+3^2+...+n^2=\\frac{n(n+1)(2n+1)}{6}"
        ).next_to(zh2,DOWN)
        self.play(Write(res))
        self.wait(2.5)
        self.play(FadeOut(zh2),FadeOut(res))
        zh3=Text("һ�ּ򵥵�֤����������������������ȥǰ����",gradient=(BLUE, GREEN))
        self.play(Write(zh3))
        self.wait(3)

        text2=MathTex(
            "n^3-(n-1)^3=n^3-(n^3-3n^2+3n-1)"
        )
        self.play(ReplacementTransform(zh3,text2))
        self.wait(3)
        self.play(ApplyMethod(text2.move_to,UP))
        # self.wait(3)

        text3=MathTex(
            "n^3-(n-1)^3=3","n^2","-3n+1"
        )
        self.play(Write(text3))
        self.wait(3)
        framebox1 = SurroundingRectangle(text3[1], buff=.1)
        self.play(ShowCreation(framebox1))
        self.play(
                    ApplyMethod(text2.move_to,UP*2),ApplyMethod(text3.move_to, UP),
                    ApplyMethod(framebox1.shift, UP)
                    )
        zh4 = Text('ע�⵽n��ƽ���� ',gradient=(BLUE, GREEN)).next_to(framebox1, DOWN) # ��
        zh5= Text("�ڵ�ʽ����ͬʱ��n��1��nȡֵ�����",gradient=(BLUE, GREEN)).next_to(zh4,DOWN)
        self.play(Write(zh4))
        self.play(Write(zh5))
        self.wait(3)

        self.play(FadeOut(text2),FadeOut(framebox1),FadeOut(zh4),FadeOut(zh5))
        self.play(ApplyMethod(text3.shift,UP*2))
        zh6=MathTex("right=","3(1^2+2^2+...+n^2)-3(1+2+...+n)+n\\times 1")
        self.wait(2)
        self.play(Write(zh6)) 
        self.wait(2)
        zh7=MathTex("=3 \\times S - 3 \\times\\frac{n(n+1)}{2} +n")
        self.play(ApplyMethod(zh6.shift,UP))
        self.play(Write(zh7))
        self.wait(2.5)
        zh8=Text("������ֻҪ������߽������",gradient=(BLUE, GREEN)).shift(DOWN)
        zh9 = Text("��������������ÿ��Ե���",gradient=(BLUE, GREEN)).next_to(zh8,DOWN)
        self.play(Write(zh8))
        self.play(Write(zh9))
        self.wait(2)
        self.play(FadeOut(zh6),FadeOut(zh7),FadeOut(zh8),FadeOut(zh9))
        zh6=MathTex("right=3 \\times S - 3 \\times\\frac{n(n+1)}{2} +n").shift(UP*2) # right equation
        self.play(GrowFromCenter(zh6))
        self.wait(1)

        zh10 = MathTex("left= [1^3+2^3+...+n^3]-[0^3+1^3+...+(n-1)^3]")
        self.play(Write(zh10))
        self.wait(2)
        # self.play(ApplyMethod(zh10.shift,UP))
        zh11=MathTex("=n^3").next_to(zh10,DOWN)
        self.play(Write(zh11))
        self.wait(2)
        zh12=MathTex("left=right") 
        self.play(FadeOut(zh10),FadeOut(zh11))
        self.play(Write(zh12))
        self.play(ApplyMethod(zh12.shift,UP))
        zh13=MathTex("n^3=3 \\times S - 3 \\times \\frac{n(n+1)}{2} +n").next_to(zh12,DOWN)
        self.play(Write(zh13))

        self.wait(2)

        zh14=Text("�����󣬿ɵý��ۣ�",gradient=(BLUE, GREEN)).next_to(zh13,DOWN)
        zh15=MathTex("S=\\frac{n(n+1)(2n+1)}{6}").next_to(zh14,DOWN)
        zh16=MathTex("1^2+2^2+3^2+...+n^2=\\frac{n(n+1)(2n+1)}{6}")
        self.play(Write(zh14))
        self.wait(2)
        self.play(Write(zh15))

        self.wait(3)
        self.play(
                    FadeOut(zh14), FadeOut(zh15),
                    FadeOut(zh13), FadeOut(zh13),
                    FadeOut(zh14), FadeOut(text3),
                    FadeOut(zh6),FadeOut(zh12)
                    )
        self.play(Write(zh16))
        self.wait(3)
        self.play(FadeOut(zh16))

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





