import os
import cv2 as cv

os.system('cls')
#       Parametros
CTE = 1  # Constante
keybuffer = 0
arquivo = 'RGB2.png'  # ->Arquivo a ser carregado

#       Carregando imagem RGB
imagem = cv.imread(f'Resources/Pictures/{arquivo}')
#       Transformando/Segmentando HSV
hsv = cv.cvtColor(imagem, cv.COLOR_BGR2HSV)
h, s, v = cv.split(hsv)

while True:
    hsv = cv.merge((h, s, v))  # Juntando as camadas H S V
    resultado = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)  # Transformando HSV -> RGB

    # cv.imshow('HSV',hsv)
    cv.imshow('Original', imagem)
    cv.imshow('Resultado', resultado)
    cv.imshow('Matriz', h)
    cv.imshow('Saturacao', s)
    cv.imshow('Intensidade', v)

    key = cv.waitKey(0) & 0xFF

#       Controles

    if key == ord('h'):
        keybuffer = 1
        print('Matriz Selecionada')
    elif key == ord('s'):
        keybuffer = 2
        print('Saturacao Selecionada')
    elif key == ord('v'):
        keybuffer = 3
        print('Intensidade Selecionada')

    if keybuffer == 1:
        #       Aumentar/Diminuir Matriz-
        if key == ord('+'):
            h = h + CTE
            print('+ Matriz'+f'\n{h}')
        elif key == ord('-'):
            h = h - CTE
            print('- Matriz'+f'\n{h}')
#       Aumentar/DiminuirSaturacao
    elif keybuffer == 2:
        if key == ord('+'):
            s = s + CTE
            print('+ Saturacao'+f'\n{s}')
        elif key == ord('-'):
            s = s - CTE
            print('- Saturacao'+f'\n{s}')
#       Aumentar/Diminuir Intensidade
    elif keybuffer == 3:
        if key == ord('+'):
            v = v + CTE
            print('+ Intensidade'+f'\n{v}')
        elif key == ord('-'):
            v = v - CTE
            print('- Intensidade'+f'\n{v}')
    if key == ord('z'):
        break
cv.destroyAllWindows
