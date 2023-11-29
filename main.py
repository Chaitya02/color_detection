import cv2
from PIL import Image
from util import get_limits

yellow = [0, 255, 255]  # color to be detected
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()  # Read a frame from the video capture

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the frame from BGR to HSV color space

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)  # Create a binary mask based on the color limits

    mask_ = Image.fromarray(mask)  # Convert the mask to a PIL Image

    bbox = mask_.getbbox()  # Get the bounding box

    # print(bbox)

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.relearse()  # Release the camera

cv2.destroyAllWindows()  # Close all OpenCV windows
