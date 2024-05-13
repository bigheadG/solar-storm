import cv2

def play_video(url):
    # Open the video capture
    cap = cv2.VideoCapture(url)

    # Check if the video capture is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return

    # Read and display frames until the video ends
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Break the loop if there are no more frames

        # Display the frame
        cv2.imshow('Video', frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

# URL of the video
video_url = 'https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_0193.mp4'

# Play the video
play_video(video_url)
