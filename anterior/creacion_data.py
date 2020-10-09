import numpy as np

import cv2 
def leer_video():
    captura = cv2.VideoCapture('ejemplo.mp4')
    captura.set(cv2.CAP_PROP_FPS, 1000)
    fps = captura.get(cv2.CAP_PROP_FPS)
    print(fps)
    i= 0
    while (captura.isOpened()):
        ret, imagen = captura.read()
        if ret == True:
            print(i)
            #cv2.imwrite('frame/'+str(i)+'.jpg', imagen)
            #cv2.imshow('video', cap.postura_imagenes(imagen, 1))
            if cv2.waitKey(30) == ord('s'):
                break
        else: break
        i+=1
    captura.release()
    cv2.destroyAllWindows()
leer_video()