import numpy as np

def has_cancer_optimized(microscope_image, dye_image, width, height):
    # Convert lists to NumPy arrays for efficient processing
    microscope_array = np.array(microscope_image)
    dye_array = np.array(dye_image)
    
    # Count the number of blob pixels and dye pixels within the blob
    blob_pixels = np.sum(microscope_array == 1)
    dye_pixels_within_blob = np.sum((microscope_array == 1) & (dye_array == 1))
    
    # Calculate the percentage of dye pixels within the blob
    dye_percentage = dye_pixels_within_blob / blob_pixels if blob_pixels > 0 else 0
    return dye_percentage > 0.10

if __name__ == "__main__":
    # Load generated images from files
    with open("microscope_image.txt", "r") as f:
        microscope_image = [list(map(int, line.strip().split(','))) for line in f]

    with open("dye_image.txt", "r") as f:
        dye_image = [list(map(int, line.strip().split(','))) for line in f]

    width, height = len(microscope_image[0]), len(microscope_image)  # Get dimensions from image
    result = has_cancer_optimized(microscope_image, dye_image, width, height)
    print(f"Parasite has cancer: {result}")
