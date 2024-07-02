# from ultralytics import YOLO  # Import the YOLO class
# import cv2

# # Load the official or custom model
# model = YOLO('yolov8s-seg.pt')  # For the official model
# model = YOLO("segment.pt")   # Uncomment this line for a custom model

# # Perform detection on a video
# results = model('video.avi')

# # Show results
# for img in results.imgs:  # Iterate through images (frames) in results
#     cv2.imshow('YOLOv8 Detection', img)  # Display image
#     if cv2.waitKey(1) == ord('q'):  # Break on 'q' key press
#         break

# cv2.destroyAllWindows()

from ultralytics import YOLO
import cv2

# Load the model
model = YOLO('yolov8s-seg.pt')  # Official model
# model = YOLO("segment.pt")   # Custom model

# Open the video
cap = cv2.VideoCapture("video.avi")

# Check if the video opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Process video frame by frame
while True:
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if no frame is returned

    # Perform detection
    results = model(frame)

    # Retrieve the processed frame for display
    processed_frame = results.render()[0]

    # Display the frame
    cv2.imshow('YOLOv8 Detection', processed_frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

