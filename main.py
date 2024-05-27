import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0) #obtener referencia de webcam

#while infinito para ciclar fotograma a fotograma
while True:
    _, img = cap.read() #leer cada fotograma
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convertir a escala de grises
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) #almacenar todas las caras que se detecte

    #dibujar rectangulos
    for (x, y, w, h) in faces: #vertices
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) #(255, 0, 0), 2 -> color y espesor
    cv2.imshow('img', img) #mostrar el fotograma detectado
    k = cv2.waitKey(30) #waitkey -> metodo que devuelve codigo ascii cada 30miliseg
    if k ==27: #ascii de ESC
        break
cap.release()
