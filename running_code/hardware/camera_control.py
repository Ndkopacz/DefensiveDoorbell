import cv2
import time

# Initialize the camera
camera = cv2.VideoCapture(0)  # Use the appropriate index for your camera

def setup_camera():
    """Set up the camera."""
    if not camera.isOpened():
        camera.open(0)  # Reopen the camera if it was closed
    print("Camera setup complete.")

def cleanup_camera():
    """Release the camera resource."""
    camera.release()
    print("Camera cleanup complete.")

def generate_frames():
    """Generate frames from the camera and encode them as JPEG."""
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Resize the frame if needed (using OpenCV)
            # frame = cv2.resize(frame, (640, 480))  # Example resize to 640x480

            # Encode the frame as JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
