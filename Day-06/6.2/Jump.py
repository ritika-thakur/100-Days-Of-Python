def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# For the fixed goal challenge.
for i in range(0, 6):
    jump()
    

# For the random goal challenge.
while(at_goal() != True):
    jump()