def turn_right():
    turn_left()
    turn_left()
    turn_left()
      

while not at_goal(): 
    if front_is_clear() and right_is_clear():
        turn_right()
        move()
    if right_is_clear():
        turn_right()
    if front_is_clear():
        move()   
    if wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and right_is_clear() and not at_goal():
        turn_right()
        move()
    elif wall_on_right() and front_is_clear():
        move()
    elif at_goal():
        break
    else:
        move()
    

        

    

