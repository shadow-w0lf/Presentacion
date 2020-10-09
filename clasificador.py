from postura import postura
from keras.models import Sequential, load_model
import tensorflow as tf
import numpy as np

class Clasificador:
    def toModelo(self, vector):
        lista = []
        lista = [np.linalg.norm(vector["R_muneca"] - vector["L_muneca"]) ,
            np.linalg.norm(vector["R_muneca"] - vector["R_Hombro"]) ,
            np.linalg.norm(vector["R_muneca"] - vector["Cuello"]) ,
            np.linalg.norm(vector["R_muneca"] - vector["R_pelvis"]) ,
            np.linalg.norm(vector["R_muneca"] - vector["C_pelvis"]) ,
            np.linalg.norm(vector["R_Codo"] - vector["R_Hombro"]) ,
            np.linalg.norm(vector["R_Codo"] - vector["Cuello"]) ,
            np.linalg.norm(vector["R_Codo"] - vector["R_pelvis"]) , 
            np.linalg.norm(vector["R_Codo"] - vector["C_pelvis"]) , # DERECHO
            np.linalg.norm(vector["L_muneca"] - vector["L_Hombro"]) , 
            np.linalg.norm(vector["L_muneca"] - vector["Cuello"]) ,
            np.linalg.norm(vector["L_muneca"] - vector["L_pelvis"]) , 
            np.linalg.norm(vector["L_muneca"] - vector["C_pelvis"]) , 
            np.linalg.norm(vector["L_Codo"] - vector["L_Hombro"]) ,
            np.linalg.norm(vector["L_Codo"] - vector["Cuello"]) , 
            np.linalg.norm(vector["L_Codo"] - vector["L_pelvis"]) , 
            np.linalg.norm(vector["L_Codo"] - vector["C_pelvis"])]
        return lista
    def clasificarPostura(self, puntos):
        model = load_model('modelo/Postura.h5')
        #print(clasificador.toModelo(puntos))
        prediction = model.predict(tf.constant([self.toModelo(puntos)]))
        return prediction
        
    def posturaPersona(self,img):
        pos = postura.postura_imagenes(img)

        return self.clasificarPostura(pos), pos