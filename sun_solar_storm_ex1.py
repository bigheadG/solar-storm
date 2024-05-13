import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import time

def fetch_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        print("Failed to retrieve image.")
        return None

def display_image(image):
    plt.imshow(image)
    plt.title("SDO Image at 193 Å")
    plt.axis('off')
    plt.show()

def play_images(base_url, interval=0.5, repeat=10):
    for _ in range(repeat):
        img = fetch_image(base_url)
        if img:
            display_image(img)
            time.sleep(interval)  # Wait before fetching the next image

# Example URL pattern (this might need to be updated based on actual available images)
base_url = 'https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0193.jpg'

play_images(base_url)
