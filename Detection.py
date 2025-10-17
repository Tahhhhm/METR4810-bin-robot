from ultralytics import YOLO
import cv2

# Load your model
model = YOLO("/home/amaana/Desktop/servo/venv/Models/bin_detection_best.pt")

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

    results = model(frame, imgsz=320, verbose=False)
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
        
        binlocation = f"{label}{side}"
        
        print(binlocation)

        # Display side text
        cv2.putText(
            annotated,
            f"{label} ({side})",
            (int(x1), int(y1)+300),
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
