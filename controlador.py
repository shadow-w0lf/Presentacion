import cv2
import numpy as np

from cuadro import Cuadro 
from vista import vista

import csv
from facial_emotion_recognition import EmotionRecognition

class Controlador:
    _cuadro = None
    _er = EmotionRecognition
    def __init__(self):
        self.cuadro = Cuadro()
        self.er = EmotionRecognition(device='gpu', gpu_id=0)

    def Activida(self):
        
        captura = cv2.VideoCapture("datos/1.mp4")
        fps = captura.get(cv2.CAP_PROP_FPS)
        i = round(fps/3)
        while (True): 
            ret, imagen = captura.read()
            if(i== 0):
                i = round(fps/3)
                if ret == True:
                    pos, vector= self.cuadro.mostrar(imagen)
                    d = er.recognise_emotion(imagen, return_type='BGR')
                    cv2.imshow('video',  imagen)
                    if cv2.waitKey(25) == ord('s'):
                        break
                else: break
            else:
                i -= 1

        captura.release()
        cv2.destroyAllWindows()

    