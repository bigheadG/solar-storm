import cv2

def play_and_save_video(url, save_path):
    # Open the video capture
    cap = cv2.VideoCapture(url)

    # Check if the video capture is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video.")
        return

    # Get the video's width, height, and frames per second
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Change codec as needed
    out = cv2.VideoWriter(save_path, fourcc, fps, (frame_width, frame_height))

    # Read and display frames until the video ends
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Break the loop if there are no more frames

        # Display the frame
        cv2.imshow('Video', frame)

        # Write the frame to the output video file
        out.write(frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture and writer and close all windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# URL of the video
video_url = 'https://sdo.gsfc.nasa.gov/assets/img/latest/mpeg/latest_1024_0193.mp4'

# Path to save the video
save_path = 'saved_video.mp4'

# Play the video and save it
play_and_save_video(video_url, save_path)

# Playback the saved video
saved_video_cap = cv2.VideoCapture(save_path)
while True:
    ret, frame = saved_video_cap.read()
    if not ret:
        break  # Break the loop if there are no more frames

    # Display the frame
    cv2.imshow('Saved Video', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
saved_video_cap.release()
cv2.destroyAllWindows()
