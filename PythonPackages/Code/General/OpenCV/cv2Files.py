#cv2 example - Files

#Here's an example that demonstrates how to use the cv2 package (OpenCV-Python) to read an image file, display it, and save it with some modifications. 
#In this example, we assume that you have an image named 'image.jpg' in the same directory as your Python script

import cv2

# Read the image file
image = cv2.imread("../../../Images/cv2/image.jpg")

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)  # Wait until a key is pressed
cv2.destroyAllWindows()  # Close all windows

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the grayscale image
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Display the blurred image
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)  # Wait until a key is pressed
cv2.destroyAllWindows()  # Close all windows

# Save the blurred image
cv2.imwrite('blurred_image.jpg', blurred_image)

# Load and display the saved image
saved_image = cv2.imread('blurred_image.jpg')
cv2.imshow('Saved Image', saved_image)
cv2.waitKey(0)  # Wait until a key is pressed
cv2.destroyAllWindows()  # Close all windows