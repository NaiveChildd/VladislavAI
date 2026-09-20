from ultralytics import YOLO
model = YOLO("Project/yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=180,
    imgsz=640,
    patience=300
)