import rosbag
import cv2
from cv_bridge import CvBridge, CvBridgeError
import os

# Path to your ROS bag file
bag_file = '/home/daniel/demo_bag/2024-04-12-15-37-43.bag'

# Topic from which to extract images
image_topic = '/stereo/left/image_raw/compressed'

# Output video file path
output_video_file = 'bag_video.avi'

# Desired frames per second for the output video
fps = 30

# Initialize the CvBridge and ROS bag
bridge = CvBridge()
bag = rosbag.Bag(bag_file, 'r')

# Extract first image to determine video properties
first_image_msg = next(bag.read_messages(topics=[image_topic]))[1]
try:
    first_image = bridge.compressed_imgmsg_to_cv2(first_image_msg, 'bgr8')
    height, width, _ = first_image.shape
except CvBridgeError as e:
    print(e)
    exit()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_video_file, fourcc, fps, (width, height))

# Iterate through the bag and write images to video
for topic, msg, t in bag.read_messages(topics=[image_topic]):
    if topic == image_topic:
        try:
            cv_image = bridge.compressed_imgmsg_to_cv2(msg, 'bgr8')
            out.write(cv_image)
        except CvBridgeError as e:
            print(e)

# Release resources
bag.close()
out.release()
print("Video has been created successfully.")
