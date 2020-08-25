import turtle
import calendar

luc_turtle = turtle.Turtle()
luc_turtle.forward(100)
luc_turtle.right(90)
luc_turtle.forward(100)
luc_turtle.right(90)
luc_turtle.forward(100)
luc_turtle.right(90)
luc_turtle.forward(100)

print('')

print(calendar.weekheader(4))
print('')

print(calendar.firstweekday())
print('')

print(calendar.month(2020, 8, 4))
print(calendar.calendar(2020))
