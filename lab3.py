import arcade
arcade.open_window(600, 600, "Drawing Example")
arcade.set_background_color(
    arcade.color.YELLOW_GREEN

)
arcade.start_render()

# Draw Textbox One
arcade.draw_rectangle_filled(200, 140, 200, 50, arcade.color.WHITE)

# Draw Outline One
arcade.draw_rectangle_outline(200, 140, 200, 50, arcade.color.BLACK, 5)

# Write Text One
arcade.draw_text("What will Electrode do?", 110, 140, arcade.color.BLUE, 15)

# Draw Textbox Two
arcade.draw_rectangle_filled(450, 150, 240, 100, arcade.color.WHITE)

# Draw Outline Two
arcade.draw_rectangle_outline(450, 150, 240, 100, arcade.color.BLACK, 5)

# Write Text Two
arcade.draw_text("FIGHT             BAG", 335, 155, arcade.color.BLUE, 25)

# Write Text TwoTwo
arcade.draw_text("POKéMON    RUN", 335, 115, arcade.color.BLUE, 25)

# Draw Stage1
arcade.draw_parabola_filled(135, 140, 250, 35, arcade.color.DARK_GREEN)

# Draw BottomElectrode
arcade.draw_circle_filled(188, 260 , 75, arcade.color.RED)

# Draw TopElectrode
arcade.draw_parabola_filled(150.5, 185, 225.5, 75, arcade.color.WHITE)

# Draw NameBox1
arcade.draw_rectangle_filled(450, 300, 240, 100, arcade.color.WHITE)

# Draw OutlineNameBox1
arcade.draw_rectangle_outline(450, 300, 240, 100, arcade.color.BLACK, 5)

# Draw HP1
arcade.draw_rectangle_filled(450, 275, 160, 20, arcade.color.GREEN)

# Draw HP1Outline
arcade.draw_rectangle_outline(450, 275, 160, 20, arcade.color.BLACK, 2)

# Draw Text1
arcade.draw_text("Electrode    Lv50", 350, 300, arcade.color.BLUE, 25)

# Draw Text2
arcade.draw_text("114/114 HP", 460, 255, arcade.color.BLUE, 10)

# Draw Stage2
arcade.draw_ellipse_filled(450, 400, 275, 75, arcade.color.DARK_GREEN)

# Draw KoffingBody
arcade.draw_circle_filled(450, 480, 85, arcade.color.PURPLE)

# Draw KoffingEye1
arcade.draw_parabola_filled(410, 500, 430, 15, arcade.color.WHITE)

# Draw KoffingEye2
arcade.draw_parabola_filled(470, 500, 490, 15, arcade.color.WHITE)

# Draw KoffingEyeLine1
arcade.draw_parabola_outline(410, 500, 430, 15, arcade.color.BLACK, 2)

# Draw KoffingEyeLine2
arcade.draw_parabola_outline(470, 500, 490, 15, arcade.color.BLACK, 2)

# Draw KoffingPupil1
arcade.draw_circle_filled(420, 522, 4, arcade.color.BLACK)

# Draw KoffingPupil2
arcade.draw_circle_filled(480, 522, 4, arcade.color.BLACK)

# Draw KoffingMouth
arcade.draw_parabola_filled(420, 530, 480, -35, arcade.color.PINK)

# Draw KoffingFang1
arcade.draw_triangle_filled(400, 495, 420, 495, 410, 475, arcade.color.WHITE)

# Draw KoffingFang2
arcade.draw_triangle_filled(480, 495, 500, 495, 490, 475, arcade.color.WHITE)

# Draw KoffingCircle
arcade.draw_ellipse_outline(450, 440, 25, 15, arcade.color.WHITE, 5)

# Draw KoffingX1
arcade.draw_line(440, 405, 460, 425, arcade.color.WHITE, 3)

# Draw KoffingX2
arcade.draw_line(460, 405, 440, 425, arcade.color.WHITE, 3)

# DrawTextbox2
arcade.draw_rectangle_filled(150, 500, 225, 100, arcade.color.WHITE)

# DrawTextbox2 Outline
arcade.draw_rectangle_outline(150, 500, 225, 100, arcade.color.BLACK, 5)

# DrawHP2
arcade.draw_rectangle_filled(150, 475, 160, 20, arcade.color.GREEN)

# DrawHP2 Outline
arcade.draw_rectangle_outline(150, 475, 160, 20, arcade.color.BLACK, 2)

# Draw HP2 Text
arcade.draw_text("145/145 HP", 160, 452, arcade.color.BLUE, 10)

# Draw KoffingText
arcade.draw_text("Koffing     Lv50", 50, 510, arcade.color.BLUE, 25)

# Draw IntenseBottomGrayBar
arcade.draw_rectangle_filled(300, 40, 600, 85, arcade.color.GRAY)

# Draw IntenseTopGrayBar
arcade.draw_rectangle_filled(300, 600, 600, -35, arcade.color.GRAY)

# Draw KoffingGas1
arcade.draw_circle_filled(550, 550, 20, arcade.color.DARK_JUNGLE_GREEN)

# Draw KoffingGas2
arcade.draw_circle_filled(575, 450, 15, arcade.color.DARK_JUNGLE_GREEN)

# Draw KoffingGas3
arcade.draw_circle_filled(350, 520, 20, arcade.color.DARK_JUNGLE_GREEN)

# Draw KoffingGas4
arcade.draw_circle_filled(340, 440, 15, arcade.color.DARK_JUNGLE_GREEN)

# Draw KoffingGas5
arcade.draw_circle_filled(440, 580, 10, arcade.color.DARK_JUNGLE_GREEN)


arcade.finish_render()
arcade.run()