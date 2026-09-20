from ultralytics import  YOLO
import cv2

model = YOLO("best.pt")

def detect_image(image_path):
    results = model(image_path)
    barrier_found = False
    names = model.names

    for box in results[0].boxes:
        cls = int(box.cls[0])
        label = names[cls]
        if label.lower() == "barrier":
            barrier_found = True
    result_image = results[0].plot()
    cv2.imwrite("results/result.jpg", result_image)
    return barrier_found