from manim import *

class sinx(GraphScene, MovingCameraScene):

    def setup(self):
        GraphScene.setup(self)

    def construct(self):
        # Setup graph
        self.camera.frame.save_state()
        self.graph_origin = 3.5 * LEFT,
        self.x_max = round(5 * PI) + 1
        self.y_min, self.y_max = -1.5, 1.5
        self.setup_axes(animate=True)

        # Graph to be plotted
        graph = self.get_graph(lambda x: np.sin(x),
                               color = BLUE,
                               x_min = 0,
                               x_max = 5 * PI
                               )

        # Place dots
        moving_dot = Dot().move_to(graph.points[0]).set_color(ORANGE)
        dot_at_start_graph = Dot().move_to(graph.points[0])
        dot_at_end_graph = Dot().move_to(graph.points[-1])
        
        # Draw Graph
        self.wait(1)
        self.play(ShowCreation(graph), run_time = 4)
        self.wait(1)
        # Write Equation
        equation = MathTex('y = \sin(x)').move_to(5.5 * LEFT)
        self.play(Write(equation), run_time = 3)
        self.wait(1)
        # Move camera
        self.add(dot_at_end_graph, dot_at_start_graph, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear), run_time = 5)
        self.camera.frame.remove_updater(update_curve)

        # Restore position
        self.play(Restore(self.camera.frame))
        self.wait(1)