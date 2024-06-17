import random

def generate_microscope_image(width, height):
    image = []
    for _ in range(height):
        row = []
        for _ in range(width):
            if random.random() < 0.75:  # 75% chance for background (black pixel)
                row.append(0)
            else:  # 25% chance for blob (white pixel)
                row.append(1)
        image.append(row)
    return image

def generate_dye_image(width, height):
    image = []
    for _ in range(height):
        row = []
        for _ in range(width):
            if random.random() < 0.05:  # 5% chance for lit pixel (dye present)
                row.append(1)
            else:
                row.append(0)
        image.append(row)
    return image

if __name__ == "__main__":
    width, height = 100, 100  # Using smaller dimensions for testing
    microscope_image = generate_microscope_image(width, height)
    dye_image = generate_dye_image(width, height)

    # Save generated images to files
    with open("microscope_image.txt", "w") as f:
        for row in microscope_image:
            f.write(','.join(map(str, row)) + "\n")

    with open("dye_image.txt", "w") as f:
        for row in dye_image:
            f.write(','.join(map(str, row)) + "\n")

    print("Images generated and saved.")
