# Drowsiness Detection Application

This project is a real-time drowsiness detection application using a pre-trained YOLOv5 model integrated with a Flask web server. The system monitors a video stream (e.g., a webcam) to detect drowsiness and triggers an alarm when drowsiness is detected for a set threshold duration.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Jupyter Notebook](#jupyter-notebook)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Features

- Real-time drowsiness detection using YOLOv5.
- Flask web server for live video streaming through a web browser.
- Alarm sound that triggers when drowsiness is detected for a set duration.
- Interactive front-end with controls to start/pause the video feed.

## Project Structure

drowsiness-detection-app/ │ ├── app.py # The Flask application code ├── drowsiness_detection.ipynb # Jupyter Notebook for experimentation and training ├── requirements.txt # Python dependencies ├── README.md # Project documentation (this file) ├── best.pt # YOLOv5 model file (add this to .gitignore if large) ├── mixkit-alarm-clock-beep-988.wav # Alarm sound file (add to .gitignore or store in static) ├── static/ │ ├── css/ │ │ └── styles.css # (Optional) Custom stylesheets │ └── images/ │ └── placeholder.jpg # Placeholder image for testing ├── templates/ │ └── index.html # HTML template for the Flask app └── .gitignore # Git ignore file


## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- [Git](https://git-scm.com/)
- [CUDA](https://developer.nvidia.com/cuda-downloads) (if using a GPU for inference)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/drowsiness-detection-app.git
   cd drowsiness-detection-app
   ```markdown
2. **Install Dependencies**
   Install the required Python packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download and Place the Model File**
   Download your trained model (`best.pt`) and place it in the root directory.

4. **Install Pygame for Sound Control**
   ```bash
   pip install pygame
   ```

## Usage

1. **Run the Flask Application**
   Start the Flask server to run the drowsiness detection app:
   ```bash
   python app.py
   ```
   The server will start at `http://0.0.0.0:5000` or `http://localhost:5000`.

2. **Access the Video Feed**
   Open a web browser and go to the provided URL. The application will display the live video feed from your webcam, with real-time drowsiness detection and an alarm if drowsiness is detected.

3. **Controlling the Video**
   - You can start or pause the video using the button provided on the webpage.
   - The system will automatically trigger an alarm if drowsiness is detected for more than the defined threshold (default is 5 seconds).

## Jupyter Notebook

The project includes a [Jupyter Notebook](drowsiness_detection.ipynb) for training and experimenting with the drowsiness detection model.

### Running the Notebook
1. Open the notebook locally using Jupyter or Visual Studio Code.
2. Run the cells sequentially to test and train the model.

The notebook demonstrates:
- Loading and using the YOLOv5 model.
- Running object detection on static images and videos.
- Training a custom model on your own dataset.

Ensure you have the required libraries installed using `requirements.txt` before running the notebook.

## Model Training

If you want to train your own model, follow these steps:

1. **Prepare Your Dataset**
   - Organize your images into labeled folders (e.g., `drowsy`, `awake`).
   - Annotate your images using tools like [LabelImg](https://github.com/tzutalin/labelImg).

2. **Train the Model**
   - Place the images and labels in the appropriate structure (e.g., `train/images`, `train/labels`).
   - Update the `data.yaml` file accordingly and run the following command:
     ```bash
     cd yolov5
     python train.py --img 320 --batch 16 --epochs 50 --data data.yaml --weights yolov5s.pt --workers 2
     ```

3. **Use the Trained Model**
   - Copy the trained model (`best.pt`) to the root directory and update `app.py` to use the new path.

## Contributing

Contributions are welcome! Here's how you can contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes (`git commit -m "Add a new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

Please ensure your code follows the project's coding standards and is well-documented.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5) for the object detection model.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Pygame](https://www.pygame.org/) for sound management.
```
