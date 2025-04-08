from ultralytics import YOLO

class ModelLoading:
    @staticmethod
    def loadModel(path=r"C:\Stack overflow\Main-Project_2k25\Development Phase\Review-4\Project\util\best_hand_n.pt"):
        model = YOLO(path)
        return model