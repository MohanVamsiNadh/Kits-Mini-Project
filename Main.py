import os
import cv2

# Set the path to the input directory containing the images
input_dir = "D:\MiniProject\sampleinputs"

# Set the path to the output directory where the human images will be saved
human_output_dir = "D:\MiniProject\Photo_outputs"

# Set the path to the output directory where the signature images will be saved
signature_output_dir = "D:\MiniProject\Sign_outputs"

# Define a function to detect the type of image (human or signature)
def detect_image_type(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding method to binarize the image
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Calculate the ratio of white pixels to black pixels in the image
    ratio = cv2.countNonZero(thresh) / (gray.shape[0] * gray.shape[1])

    # If the ratio is less than 0.1, the image is likely a signature; otherwise, it's likely a human
    if ratio < 0.1:
        return "signature"
    else:
        return "human"

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Set the full path to the input image file
    image_path = os.path.join(input_dir, filename)

    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Detect the type of image
    image_type = detect_image_type(image)

    # Save the image to the appropriate output directory
    output_dir = human_output_dir if image_type == "human" else signature_output_dir
    output_path = os.path.join(output_dir, os.path.basename(image_path))
    cv2.imwrite(output_path, image)

    print(f"Image saved: {output_path}")
