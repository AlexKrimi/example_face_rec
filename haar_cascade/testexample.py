import cv2
import sys

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Захват видео с вебки
    ret, frame = video_capture.read()

    # Перевод картинки в черно-белый формат
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Используя записанный в faceCascade классификатор Хаара, определяем где лицо
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Рисовать прямоугольник вокруг лица
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    # Вывести результат в окошко
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# уничтожить окно и отпустить вебкамеру перед выходом из программы
video_capture.release()
cv2.destroyAllWindows()