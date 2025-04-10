from entity.StorePoints import StorePoints

all_points = StorePoints()

class Normalize:
    @staticmethod
    def map_coordinates(x, y, cameraOption=all_points.getcameraOption(), originalWidth=all_points.getoriginalWidth(), originalHeight=all_points.getoriginalHeight(), targetWidth=all_points.gettargetWidth(), targetHeight=all_points.gettargetHeight()):
        if cameraOption == 0:
            new_x = targetWidth - int((x * targetHeight) / originalWidth)
            
        else:
            new_x = int((x * targetWidth) / originalWidth)

        new_y = int((y * targetHeight) / originalHeight)

        return new_x, new_y