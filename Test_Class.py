from utils_test import *
import cv2
import matplotlib.pyplot as plt
import csv

''' The test file uses the laptop computer to test the face detection without initilizing with the Drone
'''





class FindData:
    """
    FindData.videodata():
    analyses video and returns the subject position:
    [cx,cy,area]

    Find.savedata():
    saves the analysed data in a csv format

    FindData.plotdata():
    plots the data using matplotlib

    """

    def __init__(self, video_path, datafile_name):
        self.video_path = video_path
        self.datafile_name = datafile_name

    def videodata(self):

        w, h = 720, 480

        # capturing the video

        cap = cv2.VideoCapture(self.video_path)

        area_boundary = []
        cx = []
        cy = []
        results = [cx, cy, area_boundary]

        if not cap.isOpened():
            print("Error File Not Found")

        while cap.isOpened():
            ret, frame = cap.read()

            if ret:
                # step 1 get the frame from the video
                img = cv2.resize(frame, (w, h))
                img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

                # step 2 Detect face and return info of the location of the face
                # returns the image with rectangle around the face and info=[[cx,cy],Area]
                img, info = findFace(img)
                area_boundary.append(info[1])
                cx.append(info[0][0])
                cy.append(info[0][1])

                cv2.imshow('Image', img)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()
        print("videeo analysis complete")

        return results

        # the following code is for test purposes

    def savedata(self, results):

        try:

            x = list(range(0, len(results[0])))
            with open(self.datafile_name, 'w', newline='') as f:
                thewrite = csv.writer(f)
                thewrite.writerow(['data number', 'cx', 'cy', 'Area'])
                for i in range(1, len(x)):
                    thewrite.writerow([x[i], results[0][i], results[1][i], results[2][i]])
        except ValueError:
            print('saving unsuccessful')

    def plotdata(self,results):
        try:
            x = list(range(0, len(results[0])))

            fig, ax = plt.subplots()
            ax.plot(x, results[0])

            ax.set(xlabel='Data point', ylabel='Cx',
                   title='cx vs Data Point')
            ax.grid()
            plt.show()

            fig, ax = plt.subplots()
            ax.plot(x, results[1])

            ax.set(xlabel='Data point', ylabel='Cy',
                   title='cy vs Data Point')
            ax.grid()
            plt.show()

            fig, ax = plt.subplots()
            ax.plot(x, results[2])

            ax.set(xlabel='Data point', ylabel='Area',
                   title='Area vs Data Point')
            ax.grid()
            plt.show()

        except ValueError:
            print('saving unsuccessful')


""""
    Kp_z = (cv2.getTrackbarPos('KP', 'PID-z')) / 100
    Kd_z = (cv2.getTrackbarPos('KD', 'PID-z')) / 100
    pidz = [Kp_z, Kd_z]
    print(f'kp_z={Kp_z}')
    print(f'kd_z={Kd_z}')
    pid = [pidx, pidy, pidz]

    # Step 3
    pError = testTrackFace(info, w, h, pid, pError)
    print(pError)'''
"""
