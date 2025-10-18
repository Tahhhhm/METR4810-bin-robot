from ultralytics import YOLO
import cv2

# Load your bin_detection_model
bin_detection_model = YOLO("bin_detection_models/bin_detection_best.pt")
road_detection_model = YOLO("road_detection.pt")

# Open camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_XI_FRAMERATE, 1)


frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
middle_x = frame_width // 2  # vertical divider

while True:
    ret, frame = cap.read()
    if not ret:
        break

    bin_results = bin_detection_model(frame, imgsz=320, verbose=False)
    road_results = road_detection_model(frame, imgsz=320, verbose=False)

    annotated_bin = bin_results[0].plot()
    annotated_road = road_results[0].plot()

    # BIN ONLY: Draw a dividing line in the middle
    cv2.line(annotated_bin, (middle_x, 0), (middle_x, frame.shape[0]), (0, 255, 255), 2)

    # Go through bin detections
    for box in bin_results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        cls = int(box.cls[0])
        bin_label = bin_detection_model.names[cls]

        # Find object center
        center_x = (x1 + x2) / 2

        # Decide if left or right
        if center_x < middle_x:
            side = "left"
        else:
            side = "right"
        
        binlocation = f"{bin_label} {side}"
        
        print(binlocation)

    # Go through road detections
    for tile in road_results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        cls = int(box.cls[0])
        road_label = road_detection_model.names[cls]
        tile_type = f"{road_label}"
        
        print(tile_type)

cap.release()
cv2.destroyAllWindows()
