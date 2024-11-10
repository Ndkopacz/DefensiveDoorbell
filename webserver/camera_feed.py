import cv2
from flask import Flask, Response

app = Flask(__name__)

# Initialize the camera
camera = cv2.VideoCapture(0)  # Use 0 for the default camera

def generate_frames():
    while True:
        # Read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode the frame to JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            # Yield the frame in a suitable format for streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    # Video streaming route
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    # Home route to display the video feed
    return '<h1>Camera Feed</h1><img src="/video_feed">'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
