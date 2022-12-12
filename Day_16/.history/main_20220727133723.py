# import turtle
# timmy=turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("IndianRed3")
# timmy.fd(100)
# my_screen=turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"],"Type",["Electric","Water","Fire"])
print(table)
