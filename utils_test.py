
import cv2
import numpy as np



def findFace(img):
    '''uses Open cv's Viola Jone's algorithm to detect face i a frame'''

    faceCascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(imgGray,1.2,4)

    myFaceList_centre=[] #list of the centre of the
    myFaceListArea=[]


    for(x,y,w,h) in faces:
        '''This for loop goes through '''
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cx = x+w/2
        cy= y+h/2
        area=w*h
        myFaceListArea.append(area)
        myFaceList_centre.append([cx,cy])

    if len(myFaceListArea)!=0:
        i=myFaceListArea.index(max(myFaceListArea))
        return img,[myFaceList_centre[i],myFaceListArea[i]]
    else:
        return img,[[0,0],0]




def testTrackFace(info,w,h,pid,pError):



    #PID contorller

    #error in the x direction
    errorx = info[0][0]-w/2
    #speed=kp*E+kd*E+ki*E
    speedx = pid[0][0]*errorx+pid[0][1]*(errorx-pError[0])
    speedx=int(np.clip(speedx,-100,100))# putting boundaries in the speed input

    # error in the y direction
    errory = info[0][1]-h/2
    #speed=kp*E+kd*E+ki*E
    speedy = pid[1][0]*errory+pid[1][1]*(errory-pError[1])
    speedy=int(np.clip(speedy,-100,100))# putting boundaries in the speed input

    # error in the z direction
    errorz = info[1]-25000
    #speed=kp*E+kd*E+ki*E
    speedz = pid[2][0]*errorz+pid[2][1]*(errorz-pError[2])
    print(f'speed z = {speedz}')
    speedz=int(np.clip(speedz,-100,100))# putting boundaries in the speed input

    speed=[speedx,speedy,speedz]
    error=[errorx,errory,errorz]

    return error


