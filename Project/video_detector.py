import cv2
from ultralytics import YOLO

model = YOLO("best.pt")

def detect_video(video_path):
    cap = cv2.VideoCapture(video_path)
    barrier_found = False
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        if frame_count % 5 != 0:
            continue
        results = model(frame)
        boxes = results[0].boxes
        for box in boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            if label.lower() == "barrier":
                barrier_found = True
                break
        if barrier_found:
            break

    cap.release()

    return barrier_found