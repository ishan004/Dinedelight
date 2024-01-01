import csv
import os
import requests


# Function to download an image from a URL and save it to a specified folder
def download_image(url, folder_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Extract the image filename from the URL and join it with the output folder path
            filename = os.path.join(folder_path, os.path.basename(url))
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"Downloaded: {url}")
        else:
            print(f"Failed to download: {url} (Status code {response.status_code})")
    except Exception as e:
        print(f"Failed to download: {url} ({str(e)})")


# CSV file containing Image URLs
csv_file = "chitwan.csv"

# Folder to save downloaded images
output_folder = "downloaded_images"

# Create the output folder if it doesn't exist

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the CSV file and read the "Imageurls" column
with open(csv_file, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        image_url = row.get(
            "ImageURL"
        )  # Make sure this column name matches the one in your CSV
        if image_url:
            download_image(image_url, output_folder)

print("Download completed.")
