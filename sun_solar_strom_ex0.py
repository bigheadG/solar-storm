import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
import io

def fetch_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Failed to retrieve image.")
        return None

def display_image(image_data):
    img = mpimg.imread(io.BytesIO(image_data), format='jpg')
    plt.imshow(img)
    plt.title("SDO Image at 193 Å")
    plt.axis('off')
    plt.show()

def play_images(base_url, interval=0.5, repeat=10):
    for _ in range(repeat):
        img_data = fetch_image(base_url)
        if img_data:
            display_image(img_data)
            time.sleep(interval)  # Wait before fetching the next image

# Example URL pattern (this might need to be updated based on actual available images)
base_url = 'https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0193.jpg'

play_images(base_url)
