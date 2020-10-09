import postura as cap
import posturaCabeza as pCa
import numpy as np

import cv2 
def leer_video():
    captura = cv2.VideoCapture('datos\Elevator Pitch 1.mp4')
    fps = captura.get(cv2.CAP_PROP_FPS)
    i = round(fps/4)
    print (i)
    while (True): 
        ret, imagen = captura.read()
        if(i == 1):
            i = round(fps/4)
            if ret == True:
                datos = cap.postura_imagenes(imagen, 0)
                img = cap.postura_imagenes(imagen, 1)

                #cv2.imshow('video',  img)
                print(cap.clasificador(datos))
                if cv2.waitKey(25) == ord('s'):
                    break
            else: break
        else:
            i -= 1

    captura.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    
    #img = cv2.imread("ejemplo.jpeg", cv2.COLOR_BGR2RGB)
    # show imag
    #datos = cap.postura_imagenes(img)
    #print(datos["Nariz"][0])
    #key = cv2.waitKey(15)
    leer_video()
