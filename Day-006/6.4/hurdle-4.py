def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if right_is_clear():
        turn_right()
        move()
        turn_right()    
    elif wall_in_front():
        turn_left()
    elif wall_on_right():
        while(wall_on_right == True):
            move()
    else:
        move()
    
while (at_goal() != True):
    if front_is_clear():
        move()
        jump()        
    else:
        jump()
    
    
   
    