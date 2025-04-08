class Normalize:
    @staticmethod
    def map_coordinates(x, y, cameraOption, originalWidth, originalHeight, targetWidth=180, targetHeight=180):
        if cameraOption == 0:
            new_x = targetWidth - int((x * targetHeight) / originalWidth)
            
        else:
            new_x = int((x * targetWidth) / originalWidth)

        new_y = int((y * targetHeight) / originalHeight)

        return new_x, new_y