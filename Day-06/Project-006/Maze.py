def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def jump():
    if right_is_clear():
        turn_right()
    while front_is_clear():
        move()
        if right_is_clear():
            turn_right()
            move()    
    while (front_is_clear() != True):
        turn_right()
    if wall_on_right():
        turn_left()
        turn_right()
    else:
        turn_right()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()