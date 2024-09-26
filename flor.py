from turtle import *
import colorsys
import math

speed(0.25)
bgcolor("black")

# Genera los petalos
goto(0, -40)
h = 0

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(0.125, 1, 1)
        color(c)
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

# Genera la parte central de la flor
color("black")
shape("turtle")
fillcolor("brown")
phi = 137.508 * (math.pi / 180.0)

for i in range(200):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()

# Simulación de sombra en el texto
penup()
goto(2, -202)  # Posición para la sombra (ligeramente desplazada)
color("gray")  # Color de la sombra
write("I love u Ivonne", align="center", font=("Arial", 24, "bold"))

# Escribe el texto principal
goto(0, -200)  # Posición para el texto principal
color("white")  # Color del texto principal
write("I love u Ivonne", align="center", font=("Arial", 24, "bold"))

done()
