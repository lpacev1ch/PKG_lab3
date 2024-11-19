import cv2
import numpy as np

def linear_contrast(image):
    return cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

def histogram_equalization(image):
    return cv2.equalizeHist(image)

def global_threshold(image):
    _, thresh_global = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    return thresh_global

def adaptive_threshold(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

def morphological_operations(image, kernel_size=3, operation='erode'):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    if operation == 'erode':
        return cv2.erode(image, kernel)
    elif operation == 'dilate':
        return cv2.dilate(image, kernel)
    else:
        raise ValueError("Operation must be 'erode' or 'dilate'")