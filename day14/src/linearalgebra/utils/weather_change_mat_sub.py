#weather change matrix and subtract it from the image
import numpy as np
def weather_change_mat_sub(image, weather_change_mat):
    #check if the weather change matrix is the same size as the image
    if weather_change_mat.shape != image.shape:
        raise ValueError("Weather change matrix must be the same size as the image")
    #subtract the weather change matrix from the image
    result = image - weather_change_mat
    return result.astype(np.uint8)
if __name__ == "__main__":
    #test the function
    
    result = weather_change_mat_sub(image, weather_change_mat)
    print("Original Image:\n", image)
    print("Weather Change Matrix:\n", weather_change_mat)
    print("Resulting Image:\n", result)