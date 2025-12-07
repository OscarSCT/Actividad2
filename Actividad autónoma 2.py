import turtle                           #La libreria turtle ayuda a construir la interfaz gráfica
import time                             #Para obtener el tiempo
import random                           #Para usar numeros random

posponer = 0.1
puntaje = 0
maxPuntaje = 0

#Configuración
window = turtle.Screen()                #Crea una ventana nueva
window.title('Snake')                   #Titulo
window.bgcolor("#C28BC1")             #Color de fondo
window.setup(width=600,height=600)      #Dimención de pantalla
window.tracer(0)                        #Hace que la animación sea mas simple

#Cabeza de la serpiente
cabeza = turtle.Turtle()                #Crea un objeto
cabeza.speed(1)                         #Se muestra al inciar
cabeza.shape('square')                  #Se le asigna una forma, por defecto se toma 20x20 pixeles
cabeza.color("#1AFF00")               #Color a la cabeza
cabeza.penup()                          #Elimina el rastro del objeto
cabeza.goto(1,0)                        #Centra el objeto
cabeza.direction = 'stop'               #Asigna direccion, en este caso estatico

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('turtle')
comida.color("#2DC1D1")
comida.penup()
comida.goto(0,100)

#Texto para el puntaje
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write('Puntaje:0     Máximo puntaje: 0', align='center', font=('Courier', 20, 'normal'))

#Cuerpo de la serpiende
cuerpo = []                             #Una lista que almacena cada segmento
colores = [(109,160,104),(104,142,160)]


                                        #bibliografía librería Turtle
                                        #https://docs.python.org/es/3.13/library/turtle.html
