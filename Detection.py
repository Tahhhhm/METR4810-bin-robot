from ultralytics import YOLO
import cv2
from dataclasses import dataclass

class AI:
    def __init__(self):
        self.road_detection_model = YOLO("model/Road_detection.pt")    
        self.bin_detection_model = YOLO("model/bin_detection_best.pt")

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 1)

        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.middle_x = self.frame_width // 2  # vertical divider
    


    def detect_bin(self):
        ret, frame = self.cap.read()
        if not ret:
            print("No frame captured for bin detection")
            return []

        detections = []
        bin_results = self.bin_detection_model(frame, imgsz=320, verbose=False)

        for box in bin_results[0].boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            bin_label = self.bin_detection_model.names[cls]

            # Find object center
            center_x = (x1 + x2) / 2

            # Decide if left or right
            side = "left" if center_x < self.middle_x else "right"

            detection = BinDetection(label=bin_label, side=side, confidence=conf)
            detections.append(detection)

        return detections


    def detect_road(self):
        ret, frame = self.cap.read()
        if not ret:
            print("No frame captured for road detection")
            return []

        detections = []
        road_results = self.road_detection_model(frame, imgsz=320, verbose=False)

        for road in road_results[0].boxes:
            cls = int(road.cls[0])
            conf = float(road.conf[0])
            road_label = self.road_detection_model.names[cls]

            detection = RoadDetection(label=road_label, confidence=conf)
            detections.append(detection)

        return detections


    def end_detection(self):
        self.cap.release()
        cv2.destroyAllWindows()
