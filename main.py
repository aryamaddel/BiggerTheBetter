import cv2

# Load the image
image = cv2.imread('your_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect corners using Harris corner detection
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Threshold to get strong corners
threshold = 0.01 * dst.max()
corner_image = image.copy()
corner_image[dst > threshold] = [0, 0, 255]  # Mark corners in red

# Display the detected corners
cv2.imshow('Detected Corners', corner_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
