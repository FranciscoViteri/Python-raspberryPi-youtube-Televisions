#Importa libreria de delay
from time import sleep
# Importa libreria os para realizar ejecucion de comandos
import os
# Importa librerias para fecha y hora
from datetime import date
from datetime import datetime
# Importa libreria de iamgen
from PIL import Image
# Importa libreria tkinter para dibujar 
from tkinter import*
import _thread
import time
from pynput import keyboard as kb

# Setea hora inicio
horaI = 17
# Setea minutos inicio
minutosI = 40
# Setea hora finaliza
horaF = 17
# Setea minutos finaliza
minutosF = 42
# inicializa tkinter
root = Tk()
# Dibuja una geometria rectangular
root.geometry("400x200")
# Configura el color de la geometria
root.configure(bg='black')
# Habilita la funcion de mostrar esssn toda la pantalla el dibujo creado
root.attributes("-fullscreen",True)
marca=0
time.sleep(3)
os.system('vcgencmd display_power 0')
def Flash_LED2():           # Thread Flash_LED2
   while True:
#     def pulsa(tecla):
#         print('Se ha pulsado la tecla ' + str(tecla))
# 
#     with kb.Listener(pulsa) as escuchador:
#         escuchador.join()# Do forever
       # Obtiene fecha y hora de la raspberry
    fecha_y_hora = datetime.now()
    # Imprime fecha y hora
    #print(fecha_y_hora)
    # Obtiene hora del reloj
    hora = fecha_y_hora.hour
    # Imprime hora
    print(hora)
    # Obtiene minutos del reloj
    minutos = fecha_y_hora.minute
    # Imprime minutos
    #print(minutos)
    # Muestra pantalla negra de tkinter
#     root.update_idletasks()
#     # Actualiza campos 
#     root.update()
    time.sleep(0.500)
    
    if(hora == horaI and minutos == minutosI):
        #Muestra videos en pantalla completa mediante aplicacion omxplayer
        os.system('vcgencmd display_power 1')# Do forever
        marca = 1
    if(hora == horaF and minutos == minutosF):
        os.system('vcgencmd display_power 0')
        marca = 0#
# Thread to flash LED3
#
def Flash_LED3():           # Thread Flash_LED3
   while True:
       
            os.system('omxplayer -o hdmi video0.mp4')
            os.system('omxplayer -o hdmi video1.mp4')
            os.system('omxplayer -o hdmi video2.mp4')
            os.system('omxplayer -o hdmi video3.mp4')
            os.system('omxplayer -o hdmi video4.mp4')
            os.system('omxplayer -o hdmi video5.mp4')
            os.system('omxplayer -o hdmi video6.mp4')
            os.system('omxplayer -o hdmi video7.mp4')
            os.system('omxplayer -o hdmi video8.mp4')
            os.system('omxplayer -o hdmi video9.mp4')
        #break
           
         
        

_thread.start_new_thread(Flash_LED2, ())
_thread.start_new_thread(Flash_LED3, ())

while True:
  pass

