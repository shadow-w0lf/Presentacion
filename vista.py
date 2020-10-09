import cv2 as cv
class vista:

    def Mostrar(imagen):
        cv.imshow('video',  imagen)
    
    def Escribir(imagen, texto):
        # Write some Text
        font = cv.FONT_HERSHEY_SIMPLEX 
  
        # org 
        org = (50, 50) 
        
        # fontScale 
        fontScale = 1
        
        # Blue color in BGR 
        color = (255, 0, 0) 
        
        # Line thickness of 2 px 
        thickness = 2
        cv.putText(imagen, texto, org, font,  fontScale, color, thickness, cv.LINE_AA)
        return imagen
    def colocarPunto(img, punto):
        cv.circle(img, (punto[0], punto[1]), 12, (255, 0, 0), -1)
    #cargar datos