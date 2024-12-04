from ultralytics import YOLO
import cv2
import os

model = YOLO("best.pt")  

def Detect(a):
    image = cv2.imread(a)

    results = model(image)
    boxes = results[0].boxes.xyxy.cpu().numpy()  # xyxy format (x_min, y_min, x_max, y_max)
    confidences = results[0].boxes.conf.cpu().numpy()  # Confidence scores
    class_ids = results[0].boxes.cls.cpu().numpy()  # Class labels

    class_names = model.names
    for box, confidence, class_id in zip(boxes, confidences, class_ids):
        if confidence > 0.45:
            x_min, y_min, x_max, y_max = map(int, box)
            label = f"{class_names[int(class_id)]}: {(confidence*100):.1f}%" 
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(image, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow("YOLOv8 Detection", image)
    cv2.waitKey(0)

folder_path = 'Images'
for filename in os.listdir(folder_path):
    img_path = os.path.join(folder_path, filename)
    if filename.endswith('.jpg') or filename.endswith('.png'):
        Detect(img_path)

cv2.destroyAllWindows()
