import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#arcade.open_window(800, 600, "Drawing Example")


def draw_grass():
    """Draw the background"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.FOREST_GREEN) 




#arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

#arcade.start_render()
    #background colour


    #drawing state initiates

    #Field

def draw_house(y):
    #base for the house
    arcade.draw_rectangle_filled(345, 321 + y, 500, 370, arcade.color.PERU)

    #top of the house
    arcade.draw_rectangle_filled(345, 438 + y, 500, 175, arcade.color.COCOA_BROWN)
 
    #roof
    arcade.draw_rectangle_filled(182, 539 + y, 100, 70, arcade.color.BROWN)

    #door
    arcade.draw_rectangle_filled(345, 200 + y, 90, 134, arcade.color.BLACK)

    #door handle
    arcade.draw_circle_filled(367,237 + y, 5, arcade.color.YELLOW)

    #window 1
    arcade.draw_rectangle_outline(182, 400 + y, 100, 70, arcade.color.BROWN)

    #window 2
    arcade.draw_rectangle_outline(520, 400 + y, 100, 70, arcade.color.BROWN)

    #window 1 glass(vertical)
    arcade.draw_rectangle_filled(183, 400 + y, 3, 70, arcade.color.BLACK)

    #window 1 glass(horizontal)
    arcade.draw_rectangle_filled(181, 400 + y, 100, 3, arcade.color.BLACK)

    #window 2 glass(vertical)
    arcade.draw_rectangle_filled(522, 400 + y, 3, 70, arcade.color.BLACK)

    #window 2 glass(horizontal)
    arcade.draw_rectangle_filled(520, 400 + y, 100, 3, arcade.color.BLACK)

    #sun
    arcade.draw_circle_filled(682, 539, 60, arcade.color.YELLOW)

    #flagstand
    arcade.draw_rectangle_filled(632, 200 + y, 10, 179, arcade.color.GRAY)

    #flag
    arcade.draw_rectangle_filled(643, 320 + y, 33, 70, arcade.color.GREEN)

    #flag white
    arcade.draw_rectangle_filled(674, 320 + y, 33, 70, arcade.color.WHITE)

    #flag green 
    arcade.draw_rectangle_filled(705, 320 + y, 33, 70, arcade.color.GREEN)




def draw_plane(x, y):
    #body of the plane
    #arcade.draw_rectangle_filled(200 + x, 530 + y, 220, 74, arcade.color.GRAY)
    
    arcade.draw_circle_filled(302 + x, 530 + y, 23, arcade.color.BLACK)
    arcade.draw_rectangle_filled(200 + x, 530 + y, 220, 46, arcade.color.GRAY)
                                #topwing 1             #wing2          #wing3
    arcade.draw_triangle_filled(200 + x, 590 + y, 200 + x, 552 + y, 240 + x, 552 + y, arcade.color.BLACK )


    arcade.draw_triangle_filled(200 + x, 470 + y, 200 + x, 508 + y, 240 + x, 508 + y, arcade.color.BLACK )


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()


    draw_grass() 
    draw_house(-111)
    draw_plane(on_draw.plane1_x, 0)
    #draw_plane(0, 0)

    on_draw.plane1_x += 8


on_draw.plane1_x = 150
#arcade.finish_render()

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    arcade.schedule(on_draw, 1/60)
    arcade.run()


main()