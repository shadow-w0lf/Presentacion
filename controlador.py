import cv2
import numpy as np

from cuadro import Cuadro 
from vista import vista

import csv
from facial_emotion_recognition import EmotionRecognition

class Controlador:
    def __init__(self):
        self.cuadro = Cuadro()

    def Activida(self, video):
        captura = cv2.VideoCapture("datos/01.mp4")
        er = EmotionRecognition(device='gpu', gpu_id=0)
        #archivo = open("posturas.csv", 'w')
        #writer = csv.writer(archivo, delimiter=',')

        fps = captura.get(cv2.CAP_PROP_FPS)
        print(fps)
        i = round(fps/3)
        print (i)
        while (True): 
            ret, imagen = captura.read()
            if(i== 0):
                i = round(fps/3)
                if ret == True:
                    pos, vector= self.cuadro.mostrar(imagen)
                    imagen = er.recognise_emotion(imagen, return_type='BGR')
                    imagen = vista.Escribir(imagen,  self.cuadro.ToClase(np.argmax(pos)))
                    cv2.imshow('video',  imagen)
                    if cv2.waitKey(25) == ord('s'):
                        break
                else: break
            else:
                i -= 1

        captura.release()
        cv2.destroyAllWindows()

    