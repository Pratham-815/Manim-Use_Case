from manim import *

class DistanceBetweenPoints(Scene):
    def construct(self):
        # Step 1: Display the problem statement
        problem_text = Text(
            "Find the distance between the points A(2, 3) and B(4, 5)."
        ).scale(0.8)  # Resize text
        
        self.play(Write(problem_text))  # Animate text appearing
        self.wait(3)  # Show for 3 seconds
        self.play(FadeOut(problem_text))  # Fade out problem text
        
        # Step 2: Create coordinate axes
        axes = Axes(
            x_range=[0, 6, 1],  # X-axis from 0 to 6
            y_range=[0, 6, 1],  # Y-axis from 0 to 6
            axis_config={"color": BLUE},
        )
        
        # Step 3: Define points
        point_A = Dot(axes.c2p(2, 3), color=RED)
        point_B = Dot(axes.c2p(4, 5), color=GREEN)

        # Step 4: Labels for points
        label_A = MathTex("A(2,3)").next_to(point_A, LEFT)
        label_B = MathTex("B(4,5)").next_to(point_B, RIGHT)

        # Step 5: Draw the right triangle
        h_line = Line(axes.c2p(2, 3), axes.c2p(4, 3), color=YELLOW)  # Horizontal line
        v_line = Line(axes.c2p(4, 3), axes.c2p(4, 5), color=YELLOW)  # Vertical line
        hypotenuse = Line(axes.c2p(2, 3), axes.c2p(4, 5), color=WHITE)  # Distance line

        # Show grid, points, and lines
        self.play(Create(axes))
        self.wait(1)
        self.play(FadeIn(point_A, point_B))
        self.play(Write(label_A), Write(label_B))
        self.wait(1)
        self.play(Create(h_line), Create(v_line))
        self.wait(1)
        self.play(Create(hypotenuse))
        self.wait(1)

        # Step 6: Display the distance formula
        formula_1 = MathTex(
            "d = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}"
        ).to_edge(UP)
        self.play(Write(formula_1))
        self.wait(2)

        # Substitute values
        formula_2 = MathTex(
            "d = \\sqrt{(4 - 2)^2 + (5 - 3)^2}"
        ).next_to(formula_1, DOWN)
        self.play(Transform(formula_1, formula_2))
        self.wait(2)

        # Calculate squared values
        formula_3 = MathTex(
            "d = \\sqrt{2^2 + 2^2}"
        ).next_to(formula_1, DOWN)
        self.play(Transform(formula_1, formula_3))
        self.wait(2)

        # Compute final step
        formula_4 = MathTex(
            "d = \\sqrt{4 + 4}"
        ).next_to(formula_1, DOWN)
        self.play(Transform(formula_1, formula_4))
        self.wait(2)

        # Final result
        formula_5 = MathTex("d = \\sqrt{8} \\approx 2.83").next_to(formula_1, DOWN)
        self.play(Transform(formula_1, formula_5))
        self.wait(3)

        # Fade out everything
        self.play(
            FadeOut(axes, point_A, point_B, label_A, label_B, h_line, v_line, hypotenuse, formula_1)
        )
