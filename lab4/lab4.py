import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def draw_textstage1():

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

def draw_electrode(x, y):
    # Draw BottomElectrode
    arcade.draw_circle_filled( x,  y , 75, arcade.color.RED)

    # Draw TopElectrode
    arcade.draw_parabola_filled(x - 37.5, y - 75, 37.5 + x, 75, arcade.color.WHITE)

def draw_textbox2():

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

def draw_koffing(x, y):
    # Draw KoffingBody
    arcade.draw_circle_filled(450, y, 85, arcade.color.PURPLE)

    # Draw KoffingEye1
    arcade.draw_parabola_filled(410, 20 + y, 430, 15, arcade.color.WHITE)

    # Draw KoffingEye2
    arcade.draw_parabola_filled(470, 20 + y, 490, 15, arcade.color.WHITE)

    # Draw KoffingEyeLine1
    arcade.draw_parabola_outline(410, 20 + y, 430, 15, arcade.color.BLACK, 2)

    # Draw KoffingEyeLine2
    arcade.draw_parabola_outline(470, 20 + y, 490, 15, arcade.color.BLACK, 2)

    # Draw KoffingPupil1
    arcade.draw_circle_filled(420, 42 + y, 4, arcade.color.BLACK)

    # Draw KoffingPupil2
    arcade.draw_circle_filled(480, 42 + y, 4, arcade.color.BLACK)

    # Draw KoffingMouth
    arcade.draw_parabola_filled(420, 50 + y, 480, -35, arcade.color.PINK)

    # Draw KoffingFang1
    arcade.draw_triangle_filled(400, 15 + y, 420, y + 15, 410 , y - 5, arcade.color.WHITE)

    # Draw KoffingFang2
    arcade.draw_triangle_filled(480, 15 + y, 500 , y + 15, 490, y - 5, arcade.color.WHITE)

    # Draw KoffingCircle
    arcade.draw_ellipse_outline(450, y - 40, 25, 15, arcade.color.WHITE, 5)

    # Draw KoffingX1
    arcade.draw_line(440, y - 75, 460, y - 55, arcade.color.WHITE, 3)

    # Draw KoffingX2
    arcade.draw_line(460, y - 75, 440, y - 55, arcade.color.WHITE, 3)

def draw_textbox3():
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

def draw_koffinggas(x, y):
    # Draw KoffingGas1
    arcade.draw_circle_filled(550 + x, 70 + y, 20, arcade.color.DARK_JUNGLE_GREEN)

    # Draw KoffingGas2
    arcade.draw_circle_filled(575 + x,  y - 30, 15, arcade.color.DARK_JUNGLE_GREEN)

    # Draw KoffingGas3
    arcade.draw_circle_filled(350 + x, 40 + y, 20, arcade.color.DARK_JUNGLE_GREEN)

    # Draw KoffingGas4
    arcade.draw_circle_filled(340 + x,  y - 40, 15, arcade.color.DARK_JUNGLE_GREEN)

    # Draw KoffingGas5
    arcade.draw_circle_filled(440 + x, 100 + y, 10, arcade.color.DARK_JUNGLE_GREEN)

def draw_battletext(x, y):
    # Draw Textbox
    arcade.draw_rectangle_filled(x, y, 250, 50, arcade.color.WHITE)

    # Draw Outline 
    arcade.draw_rectangle_outline(x, y, 250, 50, arcade.color.BLACK, 5)

    # Write Text 
    arcade.draw_text("Electrode used Take Down!", x - 100, y, arcade.color.BLUE, 15)

    #Draw Textbox2
    arcade.draw_rectangle_filled(x + 320, y, 250, 50, arcade.color.WHITE)

    # Draw Outline2 
    arcade.draw_rectangle_outline(x + 320, y, 250, 50, arcade.color.BLACK, 5)

    # Write Text 2
    arcade.draw_text("Koffing dodged it by using Fly!", x + 210, y, arcade.color.BLUE, 15)
    

def on_draw(delta_time):
    arcade.start_render()

    draw_textstage1()
    draw_textbox2()
    draw_textbox3()
    
    draw_electrode(on_draw.electrode1_x, on_draw.electrode1_y)
    on_draw.electrode1_x +=2
    on_draw.electrode1_y +=2

    draw_koffing(450, on_draw.koffing1_y)
    on_draw.koffing1_y +=1.7

    draw_koffinggas(0, on_draw.koffinggas1_y)
    on_draw.koffinggas1_y +=1.7

    draw_battletext(on_draw.battletext1_x, 40)
    on_draw.battletext1_x +=-3


on_draw.electrode1_x = 188
on_draw.electrode1_y = 260
on_draw.koffing1_y = 480
on_draw.koffinggas1_y = 480
on_draw.battletext1_x = 600

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.YELLOW_GREEN)

    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()