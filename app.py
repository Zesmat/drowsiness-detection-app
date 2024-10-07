from flask import Flask, render_template, Response
import torch
import cv2
import numpy as np
import time
import pygame

# Initialize the Flask app
app = Flask(__name__)

# Load the YOLOv5 model using PyTorch
model = torch.hub.load('ultralytics/yolov5', 'custom', path='D:/deployment/best.pt', force_reload=True)

# Initialize Pygame mixer for sound control
pygame.mixer.init()

# Variables to track drowsiness and time
drowsy_start_time = None  # Timestamp when drowsiness starts
alarm_triggered = False  # Alarm state

# Thresholds
DROWSY_THRESHOLD_SECONDS = 5  # Number of seconds of drowsiness required to trigger alarm


# Function to play alarm sound
def play_alarm():
    global alarm_triggered
    if not alarm_triggered:
        pygame.mixer.music.load('D:/deployment/mixkit-alarm-clock-beep-988.wav')  # Load the alarm sound
        pygame.mixer.music.play(-1)  # Play in a loop
        alarm_triggered = True


# Function to stop the alarm
def stop_alarm():
    global alarm_triggered
    if alarm_triggered:
        pygame.mixer.music.stop()  # Stop the alarm sound
        alarm_triggered = False


# Video capture function
def generate_frames():
    global drowsy_start_time, alarm_triggered
    cap = cv2.VideoCapture(0)  # Use your webcam, replace '0' with the path of a video file for testing

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Resize the frame to 720px width for consistency
        target_width = 720
        height, width = frame.shape[:2]
        aspect_ratio = height / width
        new_height = int(target_width * aspect_ratio)
        frame = cv2.resize(frame, (target_width, new_height))  # Resize to 720px width

        # Process frame with YOLOv5
        results = model(frame)

        # Extract the results for the "drowsy" label
        labels = results.pandas().xyxy[0]['name'].tolist()  # Get the labels detected

        if 'Drowsy' in labels:
            if drowsy_start_time is None:
                # Start counting when drowsiness is first detected
                drowsy_start_time = time.time()
            else:
                # Check how long drowsiness has been detected
                elapsed_time = time.time() - drowsy_start_time
                if elapsed_time >= DROWSY_THRESHOLD_SECONDS:
                    # Trigger alarm if the threshold is met
                    play_alarm()
        else:
            # If no drowsiness is detected, reset timer and stop alarm
            drowsy_start_time = None
            stop_alarm()  # Stop the alarm if awake

        # Render results on frame
        processed_frame = np.squeeze(results.render())

        # Convert frame to byte format
        ret, buffer = cv2.imencode('.jpg', processed_frame)
        frame_bytes = buffer.tobytes()

        # Yield frames in the correct format for streaming
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()


# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')


# Route to stream the video
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
