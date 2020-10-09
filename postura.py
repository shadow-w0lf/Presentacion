import sys
import os
import numpy 
from sys import platform
import argparse
import cv2

dir_path = os.path.dirname(os.path.realpath(__file__))
try:
    # Change these variables to point to the correct folder (Release/x64 etc.)
    sys.path.append(dir_path + '/openpose/python/openpose/Release')
    os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/openpose/x64/Release;' +  dir_path + '/openpose/bin;'
    import pyopenpose as op
except ImportError as e:
    print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
    raise e

# Flags
parser = argparse.ArgumentParser()
parser.add_argument("--no_display", default=False, help="Enable to disable the visual display.")
args = parser.parse_known_args()

# Custom Params (refer to include/openpose/flags.hpp for more parameters)
params = dict()
params["model_folder"] = "openpose/models/"

# Starting OpenPose
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()

class postura:
    def ordenar(datos):
        lista = {\
            'Nariz': None, 
            'Cuello' : None,
            'R_Hombro': None,
            'R_Codo': None,
            'R_muneca': None,
            'L_Hombro': None,
            'L_Codo': None,
            'L_muneca': None,
            'C_pelvis': None,
            'R_pelvis': None,
            'R_Rodilla': None,
            'R_Tobillo': None,
            'L_pelvis': None,
            'L_Rodilla': None,
            'L_Tobillo': None,
            'R_ojo': None,
            'L_ojo': None,
            'R_oreja': None,
            'L_oreja': None
        }
        keys = lista.keys()
        i = 0
        if ( datos.size > 1):
            for key in keys:

                lista[key] = datos[0,i,:2]
                i += 1
        return lista

    def postura_imagenes(imagen):
        datum = op.Datum()
        datum.cvInputData = imagen
        opWrapper.emplaceAndPop([datum])
        return postura.ordenar(datum.poseKeypoints)

   
        