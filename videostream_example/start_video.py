import cv2

video_capture = cv2.VideoCapture(0)
capture_video = True

while capture_video:
    # Захват видео с вебки
    ret, frame = video_capture.read()

    # Показ захвата с вебкамеры в окне
    cv2.imshow('Видео окно', frame)

    # Закрыть 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        capture_video = False

video_capture.release()
cv2.destroyAllWindows()