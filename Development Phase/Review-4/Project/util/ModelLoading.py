from ultralytics import YOLO

class ModelLoading:
    @staticmethod
    def loadModel(path=r"C:\Stack overflow\Main-Project_2k25\YOLO_weights\ALL Animals\best_final.pt"):
        model = YOLO(path)
        return model