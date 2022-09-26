import cv2 as cv
import os
import numpy as np

#       Parametros
dir = 'RGB.png'
img = cv.imread(f'Resources/Pictures/{dir}')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#       Matriz Azul
azulBaixo = np.array([110, 0, 0])
azulAlto = np.array([255, 50, 50])
#       matriz Vermelha
vermelhoBaixo = np.array([0, 0, 110])
vermelhoAlto = np.array([50, 50, 255])
#       Matriz Verde
verdeBaixo = np.array([0, 110, 0])
verdeAlto = np.array([50, 255, 50])
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-===-==-=-=-=-=-=-=-=-=-=-=-=-=-=-
os.system('clear')



while True:
    cv.imshow('Original', img)
    key = cv.waitKey(0) & 0xFF

    if key == ord('r'):
        #print('Vermelho')
        mascaraVerm = cv.inRange(hsv, vermelhoBaixo, vermelhoAlto)
        resVerm = cv.bitwise_and(img,img, mask= mascaraVerm)
        cv.imshow('Vermelho MASC',mascaraVerm)
        cv.imshow('Vermelho RES', resVerm)
        

    elif key == ord('g'):
        #print('Verde')
        mascaraVerd = cv.inRange(img, verdeBaixo, verdeAlto)
        resVerd = cv.bitwise_and(img,img, mask= mascaraVerd)
        cv.imshow('Verde',mascaraVerd)
        cv.imshow('Verde RES', resVerd)

    elif key == ord('b'):
        #print('Azul')
        mascaraAzul = cv.inRange(img, azulBaixo, azulAlto)
        resAzul = cv.bitwise_and(img,img, mask= mascaraAzul)
        cv.imshow('Azul',mascaraAzul)
        cv.imshow('Azul RES', resAzul)
        

    elif key == ord('s'):
        cv.destroyAllWindows
        break
