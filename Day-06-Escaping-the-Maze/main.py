# This code is designed to be run in the Reeborg's World environment.
# It solves the "Maze" challenge.
# Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    """Turns the robot to the right."""
    turn_left()
    turn_left()
    turn_left()

# The main logic for escaping the maze
# This algorithm follows the right-hand wall.
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()