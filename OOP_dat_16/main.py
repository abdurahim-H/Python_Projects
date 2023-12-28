from turtle import Turtle, Screen
Abdu = Turtle()

Abdu.shape("turtle")
Abdu.color("Green")
Abdu.forward(100)
Abdu.left(90)
Abdu.forward(100)

print(Abdu)


my_screen = Screen()
print(my_screen.canvwidth)
print(my_screen.canvheight)

my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokeman Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eelctric", "Water", "Fire"])

table.align = "r"



print (table)

