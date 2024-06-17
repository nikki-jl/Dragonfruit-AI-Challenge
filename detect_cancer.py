def has_cancer(microscope_image, dye_image, width, height):
    total_blob_pixels = 0
    total_dye_pixels = 0

    for y in range(height):
        for x in range(width):
            if microscope_image[y][x] == 1:  # Blob pixel
                total_blob_pixels += 1
                if dye_image[y][x] == 1:  # Dye within blob
                    total_dye_pixels += 1

    dye_percentage = total_dye_pixels / total_blob_pixels if total_blob_pixels > 0 else 0
    return dye_percentage > 0.10

if __name__ == "__main__":
    # Load generated images from files
    with open("microscope_image.txt", "r") as f:
        microscope_image = [list(map(int, line.strip().split(','))) for line in f]

    with open("dye_image.txt", "r") as f:
        dye_image = [list(map(int, line.strip().split(','))) for line in f]

    width, height = len(microscope_image[0]), len(microscope_image)  # Get dimensions from image
    result = has_cancer(microscope_image, dye_image, width, height)
    print(f"Parasite has cancer: {result}")
