import cv2

class Camera:
    def __init__(self, originalWidth:int, originalHeight:int, cameraOption=0):
        self.cap = cv2.VideoCapture(r"C:\Stack overflow\Main-Project_2k25\Development Phase\Review-4\Project\group-of-white-people-is-raising-hands-up-in-the-air-clear-blue-sky-is-on-the--SBV-306427565-preview.mp4")
        self.cap.set(3, originalWidth)
        self.cap.set(4, originalHeight)

    def getFrame(self):
        success, img = self.cap.read()
        if success:
            return img
        return None