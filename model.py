from ultralytics import YOLO

def train_model():
    # Load a YOLOv8 model. You can start with 'yolov8n.pt' (Nano), 'yolov8s.pt' (Small), etc.
    model = YOLO('yolov8s.pt')  # Adjust to the model size you need

    # Train the model using your dataset on the GPU
    model.train(
        data='data.yaml', 
        epochs=2000, 
        imgsz=640, 
        batch=16, 
        device='cuda',  # Ensure it's set to use CUDA
        save_period=50,
        workers=8,
        optimizer='AdamW',
        cos_lr=True,
        amp=True,  # Automatic Mixed Precision for faster and optimized training
        patience=100,  # Early stopping after 100 epochs of no improvement
        mixup=0.2,  # Mixup data augmentation (value between 0-1)
        mosaic=1.0,  # Mosaic augmentation
        lr0=0.001,  # Initial learning rate
        lrf=0.01,  # Final learning rate
        verbose=True,  # Show detailed logs
        plots=True,  # Enable training plots for better tracking
        save_json=True  # Save detailed metrics to JSON
    )

if __name__ == "__main__":
    train_model()
