import cv2
import numpy as np


background_video = cv2.VideoCapture('background_video.mp4')

# Capture live video feed (your webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Capture the next frame from the background video
    ret_bg, background = background_video.read()
    if not ret_bg:
        background_video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset to the start of the video if it's finished
        ret_bg, background = background_video.read()

    # Resize the background video to match the frame size (optional, depending on video resolution)
    background = cv2.resize(background, (frame.shape[1], frame.shape[0]))

    # Convert the current frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the red color range
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Define additional dark/maroon red range
    lower_dark_red = np.array([10, 100, 100])  # Darker reds with low saturation and value
    upper_dark_red = np.array([40, 120, 100])  # Maroon/darker red shades

    # Assuming 'hsv' is your input image in HSV color space
    # Create masks for the original red areas
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Create masks for the dark/maroon red areas
    dark_red_mask = cv2.inRange(hsv, lower_dark_red, upper_dark_red)

    # Combine the masks to get a mask that detects all shades of red (including dark maroon)
    red_mask = mask1 + mask2 + dark_red_mask

    frame_rgba = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    # Invert the red mask to get the areas that are not red
    inverse_red_mask = cv2.bitwise_not(red_mask)

    #alpha channel zero means transparent  soo in inverted mask whwere ever 0 is there they will be full transpert
    frame_rgba[:, :, 3] = inverse_red_mask  # Set alpha channel to 0 where red

    #now in this transperant place i have to fill the backroung video pixel right
    for y in range(frame.shape[0]):
        for x in range(frame.shape[1]):
            if red_mask[y, x] == 255:  # If it's red (in mask)
                frame_rgba[y, x, :3] = background[y, x, :3]  # Replace with background

    cv2.imshow('Output', frame_rgba)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
background_video.release()
cv2.destroyAllWindows()