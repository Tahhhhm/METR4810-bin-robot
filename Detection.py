from ultralytics import YOLO
import cv2

# Load your model
model = YOLO("Models/bin_detection_best.pt")

# Open camera
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
middle_x = frame_width // 2  # vertical divider

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, imgsz=640, verbose=False)
    annotated = results[0].plot()

    # Draw a dividing line in the middle
    cv2.line(annotated, (middle_x, 0), (middle_x, frame.shape[0]), (0, 255, 255), 2)

    # Go through detections
    for box in results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        cls = int(box.cls[0])
        label = model.names[cls]

        # Find object center
        center_x = (x1 + x2) / 2

        # Decide if left or right
        if center_x < middle_x:
            side = "left"
        else:
            side = "right"
        
        binlocation = f"{side}{label}"
        
        print(binlocation)

        # Display side text
        cv2.putText(
            annotated,
            f"{label} ({side})",
            (int(x1), int(y1) - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 0),
            2
        )

    cv2.imshow("Zone Detection", annotated)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
