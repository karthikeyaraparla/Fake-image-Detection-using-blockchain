import cv2
import numpy as np
import os

def create_test_image():
    # Create directory if it doesn't exist
    os.makedirs('test_images', exist_ok=True)
    
    # Create a simple test image (256x256 with some shapes)
    img = np.zeros((256, 256, 3), dtype=np.uint8)
    
    # Add some shapes
    cv2.circle(img, (128, 128), 64, (0, 255, 0), -1)  # Green circle
    cv2.rectangle(img, (32, 32), (224, 224), (0, 0, 255), 2)  # Red rectangle
    cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 2)  # Blue diagonal line
    
    # Save the image
    cv2.imwrite('test_images/sample.jpg', img)
    print("Test image created at test_images/sample.jpg")

if __name__ == "__main__":
    create_test_image() 