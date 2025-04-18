import cv2

class Camera:
    def __init__(self, originalWidth:int, originalHeight:int):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, originalWidth)
        self.cap.set(4, originalHeight)

    def getFrame(self):
        success, img = self.cap.read()
        if success:
            return img
        return None