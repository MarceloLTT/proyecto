# .............JUEGO DE LA VIBORITA..............
import turtle
import time
import random

posponer = 0.11

# CREANDO LA PANTALLA
pantalla = turtle.Screen()
pantalla.title("Juego de la Viborita")
pantalla.bgcolor("black")
pantalla.setup(width = 600, height = 600)
pantalla.tracer(0)

# CREANDO LA CABEZA 
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

# CREANDO LA COMIDA
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

# CREANDO EL CUERPO CON UNA LISTA
cuerpo = []

# MOVIMIENTOS DE LA VIBORA CON FUNCIONES
def arriba():
      cabeza.direction = "up"
def abajo():
      cabeza.direction = "down"
def derecha():
      cabeza.direction = "right"
def izquierda():
      cabeza.direction = "left"

def movimiento():
      if cabeza.direction == "up":
            y = cabeza.ycor()
            cabeza.sety(y + 20)

      if cabeza.direction == "down":
            y = cabeza.ycor()
            cabeza.sety(y - 20)

      if cabeza.direction == "right":
            x = cabeza.xcor()
            cabeza.setx(x + 20)

      if cabeza.direction == "left":
            x = cabeza.xcor()
            cabeza.setx(x - 20)
# MOVIMIENTO CON EL TECLADO
pantalla.listen()
pantalla.onkeypress(arriba, "Up")
pantalla.onkeypress(abajo, "Down")
pantalla.onkeypress(derecha, "Right")
pantalla.onkeypress(izquierda, "Left")
      
while True:
      pantalla.update()

      #COLISIONES CON LOS BORDES
      if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #
            for nuevo_cuerpo in cuerpo:
                  nuevo_cuerpo.goto(1000,1000)

            #Linpiar la lista (CUERPO)
            cuerpo.clear()
            

      if cabeza.distance(comida) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            comida.goto(x,y)

            #SEGMENTOS DEL CUERPO
            nuevo_cuerpo = turtle.Turtle()
            nuevo_cuerpo.speed(0)
            nuevo_cuerpo.shape("square")
            nuevo_cuerpo.color("grey")
            nuevo_cuerpo.penup()
            #GUARDANDO LOS SEGMENTOS DEL CUERPO EN LA LISTA (CUERPO)
            cuerpo.append(nuevo_cuerpo)

      # MOVIMIENTO DEL CUERPO
      totalSeg = len(cuerpo)
      for index in range(totalSeg -1, 0, -1):
            X = cuerpo[index -1].xcor()
            y = cuerpo[index -1].ycor()
            cuerpo[index].goto(x,y)

      if totalSeg > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            cuerpo[0].goto(x,y)
      

      movimiento()

      # COLISIONES CON EL CUERPO
      for nuevo_cuerpo in cuerpo:
            if nuevo_cuerpo.distance(cabeza) < 20:
                  time.sleep(1)
                  cabeza.goto(0,0)
                  cabeza.direction ="stop"

                  #
                  for nuevo_cuerpo in cuerpo:
                        nuevo_cuerpo.goto(1000,1000)

                  cuerpo.clear()
                  
      time.sleep(posponer)
      
