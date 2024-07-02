import os
import cv2

def video_to_images(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get the frame rate of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    print (fps)

    # Calculate frame interval based on desired frame rate
    frame_interval = int(fps / 41)  # 60 frames per second

    # Initialize variables
    frame_count = 0
    success = True

    # Read and save frames at 60 frames per second
    while success:
        success, frame = cap.read()
        if frame_count % frame_interval == 0:
            if success:
                # Save frame as an image
                frame_name = f"frame_{frame_count}.jpg"
                cv2.imwrite(os.path.join(output_folder, frame_name), frame)
                print(f"Frame {frame_count} saved")
        frame_count += 1

    # Release the video capture object
    cap.release()

if __name__ == "__main__":
    # Specify the path to the video file
    video_path = "C:/Users/danie/OneDrive/Documents/SeeByte/BlueROV2_Data/underwater.mp4"

    # Specify the output folder to save frames
    output_folder = "C:/Users/danie/OneDrive/Documents/SeeByte/BlueROV2_Data/output"

    # Convert the video to image sequence at 60 frames per second
    video_to_images(video_path, output_folder)
