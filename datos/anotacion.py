import cv2
import time
import numpy as np
from PIL import Image, ImageChops
import itertools

from datetime import datetime 
video = "31.mp4"
archivo = open("31.txt", 'w')

captura = cv2.VideoCapture(video)
captura.set(cv2.CAP_PROP_FPS, int(12))
print(captura.get(cv2.CAP_PROP_FPS))
inicio = datetime.now()
i = 0
#ret, anterior = captura.read()
while (captura.isOpened()):
  ret, imagen = captura.read()
  #print(str (datetime.now() - inicio) + "  "+str(i))
  i += 1
  if ret == True:
    cv2.imshow('video', imagen)
    #print(str(captura.get(cv2.CAP_PROP_POS_MSEC)/1000))
    #time.sleep(5)
    if cv2.waitKey(1) == ord('s'):
      break
  else: break
  postura = input(str(round(captura.get(cv2.CAP_PROP_POS_MSEC)/1000, 2))+"postura ")
  emotion = str(0)
  vision = str(0)
  archivo.write(str(round(captura.get(cv2.CAP_PROP_POS_MSEC)/1000, 2)) + " Postura: " +postura+" Emotion: "+emotion+" Vision: "+ vision+ "\n")
  #anterior = imagen
captura.release()
cv2.destroyAllWindows()
archivo.close()