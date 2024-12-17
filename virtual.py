import cv2
import numpy as np
from collections import deque

# Initialize variables
drawing = False
brush_color = (0, 255, 0)  # Initial brush color (Green)
brush_size = 10
painting_canvas = np.ones((480, 640, 3), dtype=np.uint8) * 255  # White canvas

# Create a deque to store drawing points
draw_points = deque(maxlen=512)

# Open a window
cv2.namedWindow("Virtual Painting")

# Function to draw on the canvas
def draw(event, x, y, flags, param):
    global drawing, brush_color, brush_size

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        draw_points.appendleft((x, y))
        cv2.circle(painting_canvas, (x, y), brush_size, brush_color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# Set the callback function for mouse events
cv2.setMouseCallback("Virtual Painting", draw)

# Main loop
while True:
    cv2.imshow("Virtual Painting", painting_canvas)

    # Break the loop when 'ESC' key is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# Release resources
cv2.destroyAllWindows()
