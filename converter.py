import cv2
import argparse
import sys
import os

def convert_to_sketch(image_path, output_path=None):
    """
    Converts an image to a pencil sketch.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the output sketch. If None, display only.
    """
    # 1. Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not open or find the image at '{image_path}'.")
        return

    # 2. Convert to Gray Scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 3. Invert the image
    inverted_image = 255 - gray_image

    # 4. Blur the inverted image
    # Gaussian Blur helps in smoothing out the noise
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

    # 5. Invert the blurred image
    inverted_blurred = 255 - blurred

    # 6. Create the pencil sketch
    # We divide the gray image by the inverted blurred image
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

    # 7. Output Result
    if output_path:
        cv2.imwrite(output_path, pencil_sketch)
        print(f"Sketch saved to '{output_path}'")
    else:
        # Display results (press any key to close)
        cv2.imshow("Original Image", image)
        cv2.imshow("Pencil Sketch", pencil_sketch)
        print("Press any key to close the image windows...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description="Convert an image to a pencil sketch.")
    parser.add_argument("input", help="Path to the input image file")
    parser.add_argument("-o", "--output", help="Path to save the output sketch file (optional)")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: The file '{args.input}' does not exist.")
        sys.exit(1)

    convert_to_sketch(args.input, args.output)

if __name__ == "__main__":
    main()
