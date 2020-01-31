import arcade

arcade.open_window(800, 600, "Drawing Example")

#background colour
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

#drawing state initiates
arcade.start_render()


#Field
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.FOREST_GREEN)

#base for the house
arcade.draw_rectangle_filled(345, 321, 500, 370, arcade.color.PERU)

#top of the house
arcade.draw_rectangle_filled(345, 438, 500, 175, arcade.color.COCOA_BROWN)

#roof
arcade.draw_rectangle_filled(182, 539, 100, 70, arcade.color.BROWN)

#door
arcade.draw_rectangle_filled(345, 200, 90, 134, arcade.color.BLACK)

#door handle
arcade.draw_circle_filled(367,237, 5, arcade.color.YELLOW)

#window 1
arcade.draw_rectangle_outline(182, 400, 100, 70, arcade.color.BROWN)

#window 2
arcade.draw_rectangle_outline(520, 400, 100, 70, arcade.color.BROWN)

#window 1 glass(vertical)
arcade.draw_rectangle_filled(183, 400, 3, 70, arcade.color.BLACK)

#window 1 glass(horizontal)
arcade.draw_rectangle_filled(181, 400, 100, 3, arcade.color.BLACK)

#window 2 glass(vertical)
arcade.draw_rectangle_filled(522, 400, 3, 70, arcade.color.BLACK)

#window 2 glass(horizontal)
arcade.draw_rectangle_filled(520, 400, 100, 3, arcade.color.BLACK)

#sun
arcade.draw_circle_filled(682, 539, 60, arcade.color.YELLOW)

#flagstand
arcade.draw_rectangle_filled(632, 200, 10, 179, arcade.color.GRAY)

#flag
arcade.draw_rectangle_filled(643, 320, 33, 70, arcade.color.GREEN)

#flag white
arcade.draw_rectangle_filled(674, 320, 33, 70, arcade.color.WHITE)

#flag green 
arcade.draw_rectangle_filled(705, 320, 33, 70, arcade.color.GREEN)






arcade.finish_render()


arcade.run()