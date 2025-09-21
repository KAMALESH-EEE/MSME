import cv2
from picamera2 import Picamera2

# Initialize the Picamera2 object
picam2 = Picamera2()

# Configure the camera for a preview (video) stream
# XRGB8888 is an image format that is directly compatible with OpenCV
# You can change the size to a resolution that fits your needs
camera_config = picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)})
picam2.configure(camera_config)

# Start the camera
picam2.start()

# Loop to continuously capture frames
while True:
    # Capture a frame as a NumPy array
    frame = picam2.capture_array()

    # OpenCV expects BGR format, so you need to convert from XRGB
    # The X in XRGB is an extra byte for alignment, so you slice it off
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

    # Display the frame in a window
    cv2.imshow("PiCamera OpenCV Feed", frame_bgr)

    # Press 'q' to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cv2.destroyAllWindows()
picam2.stop()