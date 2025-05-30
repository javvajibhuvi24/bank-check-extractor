import os
import pytesseract
from PIL import Image
import pandas as pd

# Set tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set full absolute path to the 'checks' folder
input_folder = r'C:\Users\javva_28xwla\OneDrive\Documents\bank-check-extractor\data\checks'
output_folder = r'C:\Users\javva_28xwla\OneDrive\Documents\bank-check-extractor\data\output'
output_file = os.path.join(output_folder, 'extracted_data.csv')

print("Input folder:", input_folder)

# Check if folder exists
if not os.path.exists(input_folder):
    print(f"Error: Input folder '{input_folder}' does not exist!")
    exit(1)

os.makedirs(output_folder, exist_ok=True)

def process_files(input_dir):
    results = []
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        print(f"Processing file: {filename}")

        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
            print(f"Extracted Text:\n{text}\n")
            results.append({'file': filename, 'text': text})
        else:
            print(f"Skipping unsupported file: {filename}")
    return results

if __name__ == "__main__":
    extracted_data = process_files(input_folder)

    df = pd.DataFrame(extracted_data)
    df.to_csv(output_file, index=False)

    print(f"✅ Extracted data saved to: {output_file}")