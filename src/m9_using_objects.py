"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Jacob Ritenour.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()
def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(400, 400)

    center_point = rg.Point(160, 160)
    circle = rg.Circle(center_point, 150)
    circle.fill_color = 'red'
    circle.attach_to(window)

    center_point2 = rg.Point(200, 200)
    circle2 = rg.Circle(center_point2, 100)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(500, 500)

    circ_x = 200
    circ_y = 200
    rect_x_init = 100
    rect_y_init = 50
    rect_x_final = 300
    rect_y_final = 100

    circle = rg.Circle(rg.Point(circ_x, circ_y), 75)
    circle.fill_color = 'blue'
    circle.attach_to(window)

    rectangle = rg.Rectangle(rg.Point(rect_x_init, rect_y_init), rg.Point(rect_x_final, rect_y_final))
    rectangle.attach_to(window)

    window.render()
    window.close_on_mouse_click()

    print(circle.outline_thickness)
    print(circle.fill_color)
    print(circle.center)
    print(circ_x)
    print(circ_y)
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(rectangle.get_center())
    print((rect_x_final + rect_x_init)/2)
    print((rect_y_final + rect_y_init)/2)

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.

    window = rg.RoseWindow(500, 500)
    start1 = rg.Point(300, 300)
    end1 = rg.Point(425, 50)
    line = rg.Line(start1, end1)
    line.color = 'blue'
    line.attach_to(window)

    thicc_line = rg.Line(rg.Point(350, 300), rg.Point(475, 300))
    thicc_line.thickness = 10
    thicc_line.attach_to(window)

    window.render()
    window.close_on_mouse_click()
    print('-----------------')
    print('thick line coordinates:')
    print(thicc_line.get_midpoint())
    print((thicc_line.start.x + thicc_line.end.x)/2)
    print((thicc_line.start.y + thicc_line.end.y)/2)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
