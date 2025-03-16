import os
import requests
import hashlib
from tqdm import tqdm

def download_file(url, filename):
    """Download a file with progress bar"""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            pbar.update(size)

def main():
    # Model URL (using a MesoNet pre-trained model as an example)
    model_url = "https://github.com/DariusAf/MesoNet/raw/master/weights/Meso4_DF.h5"
    model_path = "deepfake_model.h5"
    
    print("Downloading pre-trained deepfake detection model...")
    try:
        download_file(model_url, model_path)
        print(f"Model successfully downloaded to {model_path}")
        
        # Verify file exists and has content
        if os.path.exists(model_path) and os.path.getsize(model_path) > 0:
            print("Model file verified successfully!")
        else:
            print("Error: Model file is empty or doesn't exist!")
            
    except Exception as e:
        print(f"Error downloading model: {str(e)}")
        print("Please check your internet connection and try again.")

if __name__ == "__main__":
    main() 