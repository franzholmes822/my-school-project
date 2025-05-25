import requests
import os

def upload_file(file_path):
    response = requests.post('http://upload.example.com/upload', files={'file': open(file_path, 'rb')})
    print(f"File uploaded successfully: {response.status_code} - {response.text}")

if __name__ == "__main__":
    file_path = input("Enter the path to the file you want to upload: ")
    upload_file(file_path)
