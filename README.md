# RustHax – Real-Time Object Detection System

## Overview

**RustHax** is a real-time object detection system designed to identify and track objects efficiently using state-of-the-art deep learning models. Leveraging **YOLOv8** and **OpenCV**, RustHax achieves high detection accuracy with low latency, making it suitable for various applications, including surveillance, autonomous driving, and robotics.

## Features

- **Real-Time Detection**: Processes video streams at 60 frames per second (FPS), ensuring timely object detection.
- **High Accuracy**: Trained on custom datasets to enhance detection precision for specific object classes.
- **Scalability**: Modular design allows easy integration with different systems and scalability across various platforms.
- **Performance Optimization**: Implements efficient algorithms to minimize latency and maximize throughput.
- **Extensive Testing**: Achieves a 95% precision rate with reduced false positives, validated through comprehensive testing.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/pawelsloboda5/rustHax.git
   cd rustHax
2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

Download Pre-trained Models:

YOLOv8s.pt
Custom Model – RustHax.onnx
Place the downloaded models in the models/ directory.
Usage

4. **Run the Detection Script**:
   ```bash
   python script.py --source path_to_video.mp4 --model models/yolov8s.pt

Adjust Detection Parameters:

Modify confidence thresholds, input sizes, and other parameters in config.yaml to suit your requirements.
Custom Training
To train RustHax on your dataset:

Prepare Dataset:

Organize images and annotations in YOLO format.
Update data.yaml with dataset paths and class names.

5. **Train Model**:
   ```bash
   python train.py --data data.yaml --cfg models/yolov8s.yaml --weights '' --epochs 100
6. **Export Trained Model**:
   ```bash
   python export.py --weights runs/train/exp/weights/best.pt --include onnx

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
YOLOv8 by Ultralytics
OpenCV Library
yaml
