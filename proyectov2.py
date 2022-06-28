import cv2
import sim
import numpy as np
import time

def connect(port):
    sim.simxFinish(-1) 
    clientID=sim.simxStart('127.0.0.1',port,True,True,2000,5) 
    if clientID == 0: print("Conectado al puerto: ", port)
    else: print("La conexión ha fallado :(")
    return clientID

clientID = connect(19997)


# Obtenemos los manejadores 
ret,joint1=sim.simxGetObjectHandle(clientID,'Franka_joint1',sim.simx_opmode_blocking)
ret,joint2=sim.simxGetObjectHandle(clientID,'Franka_joint2',sim.simx_opmode_blocking)
ret,joint3=sim.simxGetObjectHandle(clientID,'Franka_joint3',sim.simx_opmode_blocking)
ret,joint4=sim.simxGetObjectHandle(clientID,'Franka_joint4',sim.simx_opmode_blocking)
ret,joint5=sim.simxGetObjectHandle(clientID,'Franka_joint5',sim.simx_opmode_blocking)
ret,joint6=sim.simxGetObjectHandle(clientID,'Franka_joint6',sim.simx_opmode_blocking)
ret,joint7=sim.simxGetObjectHandle(clientID,'Franka_joint7',sim.simx_opmode_blocking)
ret,joint8=sim.simxGetObjectHandle(clientID,'Prismatic_joint',sim.simx_opmode_blocking)

image = cv2.VideoCapture(0)  

contador_tr = 0
contador_cua = 0
contador_rec = 0
contador_penta = 0
contador_hexa = 0
contador_est = 0
contador_cr = 0


while(True):
    ret, frame = image.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Convierte a escala de grises
    canny = cv2.Canny(gray, 10, 150) #Imagen binarizada 
    canny = cv2.dilate(canny, None, iterations=1) #Agrega dilatación a la imagen
    canny = cv2.erode(canny, None, iterations=1) #Agrega erosión a la imagen
    cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 4 Encontrar los contornos 

    k = cv2.waitKey(1)

    for c in cnts:
        area = cv2.contourArea(c)
        epsilon = 0.009*cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,epsilon,True) 
        x,y,w,h = cv2.boundingRect(approx) #Se utiliza para dibujar un rectangulo aproximado alrededor de la imagen binaria

        if area > 400:

            if len(approx)==3: #cantidad de puntos o vertices obtenidos
                cv2.putText(frame,'Triangulo', (x,y-5),1,1,(0,255,0),1)
                cv2.drawContours(frame, [approx], 0, (0,255,0),2) #Dibuja todos los contornos encontrados
                if k%256 == 32:
                    # Tecla espacio
                    nombre_img = "triangulo{}.png".format(contador_tr)
                    cv2.imwrite(nombre_img, frame)
                    print("{} ¡Foto tomada!".format(nombre_img))
                    contador_tr += 1
                    print("Es un triangulo")

                    #Secuencia triángulo

                    q3 = 90.3* np.pi/180
                    q4 =-5.5 *np.pi/180
                    q6 =-65* np.pi/180
                    q8 = 0.0

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(20)

                    q3 = 87.5* np.pi/180
                    q4 =0 *np.pi/180
                    q6 =-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = 92.5* np.pi/180
                    q4 =0 *np.pi/180
                    q6 =-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    #

                    q3 = 89.7* np.pi/180
                    q4 =-5.5 *np.pi/180
                    q6 =-65* np.pi/180
                    q8 = 0.0

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = 92.5* np.pi/180
                    q4 =0 *np.pi/180
                    q6 =-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

            if len(approx)==4:
                aspect_ratio = float(w)/h #aspect ratio se obtiene de la relación de alto y ancho
                print('aspect_ratio= ', aspect_ratio)
                if 0.90 <= aspect_ratio <= 1.20:
                    cv2.putText(frame,'Cuadrado', (x,y-5),1,1,(0,255,0),1)
                    cv2.drawContours(frame, [approx], 0, (0,255,0),2) #Dibuja todos los contornos encontrados
                    if k%256 == 32:
                        # Tecla espacio
                        nombre_img = "cuadrado{}.png".format(contador_cua)
                        cv2.imwrite(nombre_img, frame)
                        print("{} ¡Foto tomada!".format(nombre_img))
                        contador_cua += 1
                        print("Es un cuadrado")
                        #Secuencia cuadrado

                        q3 = 2.5* np.pi/180
                        q4 =-4.5 *np.pi/180
                        q6 =-69* np.pi/180
                        q8 = 0.0

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)

                        q3 = -2.5* np.pi/180
                        q4 =-4.5 *np.pi/180
                        q6 =-69* np.pi/180
                        q8 = 0.05

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)

                        q3 = -2.5* np.pi/180
                        q4 =-5.5 *np.pi/180
                        q6 =-65* np.pi/180
                        q8 = 0.0

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)

                        q3 = -2.5* np.pi/180
                        q4 =0 *np.pi/180
                        q6 =-90* np.pi/180
                        q8 = 0.05

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)

                        q3 = 2.5* np.pi/180
                        q4 =0 *np.pi/180
                        q6 =-90* np.pi/180
                        q8 = 0.05

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)

                        #

                        q3 = 2.5* np.pi/180
                        q4 =-5.5 *np.pi/180
                        q6 =-65* np.pi/180
                        q8 = 0.0

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)

                        q3 = 2.5* np.pi/180
                        q4 =0 *np.pi/180
                        q6 =-90* np.pi/180
                        q8 = 0.05

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)
                else:
                    cv2.putText(frame,'Rectangulo', (x,y-5),1,1,(0,255,0),1)
                    cv2.drawContours(frame, [approx], 0, (0,255,0),2) #Dibuja todos los contornos encontrados
                    if k%256 == 32:
                        # Tecla espacio
                        nombre_img = "rectangulo{}.png".format(contador_rec)
                        cv2.imwrite(nombre_img, frame)
                        print("{} ¡Foto tomada!".format(nombre_img))
                        contador_rec += 1
                        print("Es un rectangulo")

                        #Secuencia rectangulo

                        q3 = 181.25* np.pi/180
                        q4 =-4.5 *np.pi/180
                        q6 =-69* np.pi/180
                        q8 = 0.0

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(20)

                        q3 = 178.75* np.pi/180
                        q4 =-4.5 *np.pi/180
                        q6 =-69* np.pi/180
                        q8 = 0.05

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)

                        q3 = 178.75* np.pi/180
                        q4 =-5.5 *np.pi/180
                        q6 =-65* np.pi/180
                        q8 = 0.0

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)

                        q3 = 178.75* np.pi/180
                        q4 =0 *np.pi/180
                        q6 =-90* np.pi/180
                        q8 = 0.05

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)

                        q3 = 181.25* np.pi/180
                        q4 =0 *np.pi/180
                        q6 =-90* np.pi/180
                        q8 = 0.05

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)

                        #

                        q3 = 181.25* np.pi/180
                        q4 =-5.5 *np.pi/180
                        q6 =-65* np.pi/180
                        q8 = 0.0

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)

                        q3 = 181.25* np.pi/180
                        q4 =0 *np.pi/180
                        q6 =-90* np.pi/180
                        q8 = 0.05

                        returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                        returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                        time.sleep(5)

            if len(approx)==5:
                cv2.putText(frame,'Pentagono', (x,y-5),1,1,(0,255,0),1)
                cv2.drawContours(frame, [approx], 0, (0,255,0),2) #Dibuja todos los contornos encontrados
                if k%256 == 32:
                    # Tecla espacio
                    nombre_img = "pentagono{}.png".format(contador_penta)
                    cv2.imwrite(nombre_img, frame)
                    print("{} ¡Foto tomada!".format(nombre_img))
                    contador_penta += 1
                    print("Es un Pentagono")

                    #Secuencia pentagono

                    q3 = 0.1* np.pi/180
                    q4 =-5.5 *np.pi/180
                    q6 =-65* np.pi/180
                    q8 = 0.0

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = -2.5* np.pi/180
                    q4 =-2.5 *np.pi/180
                    q6 =-77* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = -1.5* np.pi/180
                    q4 =0 *np.pi/180
                    q6 =-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    #

                    q3 = -0.1* np.pi/180
                    q4 =-5.5 *np.pi/180
                    q6 =-65* np.pi/180
                    q8 = 0.0

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = 2.5* np.pi/180
                    q4 =-2.5 *np.pi/180
                    q6 =-77* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = 1.5* np.pi/180
                    q4 =0 *np.pi/180
                    q6 =-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = -1.5* np.pi/180
                    q4 =0 *np.pi/180
                    q6=-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

            if len(approx)==6:
                cv2.putText(frame,'Hexagono', (x,y-5),1,1,(0,255,0),1)
                cv2.drawContours(frame, [approx], 0, (0,255,0),2) #Dibuja todos los contornos encontrados
                if k%256 == 32:
                    # Tecla espacio
                    nombre_img = "hexagono{}.png".format(contador_hexa)
                    cv2.imwrite(nombre_img, frame)
                    print("{} ¡Foto tomada!".format(nombre_img))
                    contador_hexa += 1
                    print("Es un hexagono")

                    #Secuencia hexagono

                    q3 = 1.5* np.pi/180
                    q4 =-5.3 *np.pi/180
                    q6 =-66* np.pi/180
                    q8 = 0.0

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = -1.5* np.pi/180
                    q4 =-5.3 *np.pi/180
                    q6 =-66* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = -1.5* np.pi/180
                    q4 =-5.5 *np.pi/180
                    q6 =-65* np.pi/180
                    q8 = 0.0

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = -2.5* np.pi/180
                    q4 =-2 *np.pi/180
                    q6 =-79* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = -1.5* np.pi/180
                    q4 =0 *np.pi/180
                    q6 =-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    #

                    q3 = 1.5* np.pi/180
                    q4 =-5.5 *np.pi/180
                    q6 =-65* np.pi/180
                    q8 = 0.0

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = 2.5* np.pi/180
                    q4 =-2 *np.pi/180
                    q6 =-79* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = 1.5* np.pi/180
                    q4 =0 *np.pi/180
                    q6 =-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = -1.5* np.pi/180
                    q4 =0 *np.pi/180
                    q6 =-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)  
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)
            
            if len(approx)==10:
                cv2.putText(frame,'Estrella', (x,y-5),1,1,(0,255,0),1)
                cv2.drawContours(frame, [approx], 0, (0,255,0),2) #Dibuja todos los contornos encontrados
                if k%256 == 32:
                    # Tecla espacio
                    nombre_img = "estrella{}.png".format(contador_est)
                    cv2.imwrite(nombre_img, frame)
                    print("{} ¡Foto tomada!".format(nombre_img))
                    contador_est += 1
                    print("Es una estrella")

                    #Secuencia estrella

                    q3 = 0.1* np.pi/180
                    q4 =-5.5 *np.pi/180
                    q6 =-65* np.pi/180
                    q8 = 0.0

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(10)

                    q3 = -1* np.pi/180
                    q4 =-2.5 *np.pi/180
                    q6 =-77* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = -3.2* np.pi/180
                    q4 =-2.5 *np.pi/180
                    q6 =-77* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = -1.8* np.pi/180
                    q4 =-1 *np.pi/180
                    q6 =-85* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = -2.5* np.pi/180
                    q4 =0.5 *np.pi/180
                    q6 =-93* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = 0* np.pi/180
                    q4 =0 *np.pi/180
                    q6 =-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    #

                    q3 = -0.1* np.pi/180
                    q4 =-5.5 *np.pi/180
                    q6 =-65* np.pi/180
                    q8 = 0.0

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = 1* np.pi/180
                    q4 =-2.5 *np.pi/180
                    q6 =-77* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = 3.2* np.pi/180
                    q4 =-2.5 *np.pi/180
                    q6 =-77* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = 1.8* np.pi/180
                    q4 =-1 *np.pi/180
                    q6 =-85* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = 2.5* np.pi/180
                    q4 =0.5 *np.pi/180
                    q6 =-93* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

                    q3 = 0* np.pi/180
                    q4 =0 *np.pi/180
                    q6 =-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

            if len(approx)>=13:
                cv2.putText(frame,'Circulo', (x,y-5),1,1,(0,255,0),1)
                cv2.drawContours(frame, [approx], 0, (0,255,0),2) #Dibuja todos los contornos encontrados
                if k%256 == 32:
                    # Tecla espacio
                    nombre_img = "circulo{}.png".format(contador_cr)
                    cv2.imwrite(nombre_img, frame)
                    print("{} ¡Foto tomada!".format(nombre_img))
                    contador_cr += 1
                    print("Es un circulo")

                    #Secuencia Circulo

                    q3=0* np.pi/180
                    q4=0* np.pi/180
                    q6=-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(4)

                    q3=120* np.pi/180
                    q4=0* np.pi/180
                    q6=-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(18)

                    q3=250* np.pi/180
                    q4=0* np.pi/180
                    q6=-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(18)

                    q3=360* np.pi/180
                    q4=0* np.pi/180
                    q6=-90* np.pi/180
                    q8 = 0.05

                    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint6, q6, sim.simx_opmode_oneshot)
                    returnCode = sim.simxSetJointTargetPosition(clientID, joint8, q8, sim.simx_opmode_oneshot)
                    time.sleep(5)

        cv2.imshow('frame',frame)
   
    if k%256 == 27:
        # Tecla ESC
        print("Cerrando...")
        break
        
image.release()
cv2.destroyAllWindows()