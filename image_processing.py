import cv2
import numpy as np
import os

def process_image(image, filter_type):
    """Apply selected image processing technique."""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    filters = {
        "Original": gray_image,
        "Gaussian Blur": cv2.GaussianBlur(gray_image, (5, 5), 0),
        "Median Blur": cv2.medianBlur(gray_image, 5),
        "Histogram Equalization": cv2.equalizeHist(gray_image),
        "Sobel Edge Detection": cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5),
        "Canny Edge Detection": cv2.Canny(gray_image, 100, 200),
    }

    return filters.get(filter_type, gray_image)

def resize_image(image, width, height):
    """Resize image to the given width and height."""
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

def compress_image(image, width, height, target_size_kb, output_format):
    """
    Resize and compress the image to achieve the target file size.
    """
    image = resize_image(image, width, height)
    output_path = f"compressed_image.{output_format.lower()}"
    quality = 95  # Start with high quality
    encode_param = [cv2.IMWRITE_JPEG_QUALITY, quality] if output_format == "JPEG" else [cv2.IMWRITE_PNG_COMPRESSION, 9]
    
    cv2.imwrite(output_path, image, encode_param)
    file_size = os.path.getsize(output_path) // 1024  # Convert bytes to KB

    # Adjust quality to reach the target size range
    while file_size > target_size_kb and quality > 10:
        quality -= 5  # Reduce quality gradually
        encode_param[1] = quality
        cv2.imwrite(output_path, image, encode_param)
        file_size = os.path.getsize(output_path) // 1024

    return output_path
