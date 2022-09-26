import cv2 as cv
import imageio
import os

imagemBuffer = []
keyBuffer = -1
dir = "kitten"
video = cv.VideoCapture(f'Resources/videos/{dir}.mp4')
gif = cv.VideoCapture(f'Resources/videos/{dir}.gif')

os.system('cls')
print(' [S]Capturar frames\n' + '[D]Salvar/Sair\n')
while True:
    try:
        ret, frame = video.read()
        cv.imshow(dir, frame)
        key = cv.waitKey(30)

        if key == ord('s'):
            if keyBuffer == -1:
                print('Captura iniciada! Pressione [D] para finalizar a captura.')
            key = -1
            keyBuffer = ord('s')
        if key == -1 and keyBuffer == ord('s'):
            rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            imagemBuffer.append(rgb)

        if key & 0xFF == ord('d'):
            video.release()
    except:break

if len(imagemBuffer) > 0:
    print('Salvando gif...')
    imageio.mimsave(f'Resources/videos/{dir}.gif', imagemBuffer, fps=20)
    print('Tarefa finalizada.\nReproduzindo Gif')
    while True:
        try:
            ret, frame = gif.read()
            cv.imshow(f'{dir} gif', frame)
            key = cv.waitKey(30)
            if key & 0xFF == ord('d'):
                gif.release()
                cv.destroyAllWindows()
        except:break