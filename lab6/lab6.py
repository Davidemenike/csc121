import arcade

def draw_section_outlines():
    color = arcade.color.BLACK

    #drawing the squares at the bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, color)
    arcade.draw_rectangle_outline(450, 150, 300, 300, color)
    arcade.draw_rectangle_outline(750, 150, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, color)

    #drawing the squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, color)
    arcade.draw_rectangle_outline(450, 450, 300, 300, color)
    arcade.draw_rectangle_outline(750, 450, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, color)



def draw_section_1():
    for row in range(30):
        for column in range(30):
            pass
            x = (column * 10) + 5

            y = (row * 10) + 5
            #print(x, y)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def main():
    arcade.open_window(1200, 600, "Lab 05 - Loopy lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    draw_section_outlines()

    draw_section_1()

    arcade.finish_render()
    arcade.run()

if __name__=='__main__':
    main()
