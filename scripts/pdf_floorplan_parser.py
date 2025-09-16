# Simplified floorplan parser using pdfplumber + OpenCV for image extraction
import os
import pdfplumber
from PIL import Image

INPUT = os.path.join('..','sample_data','floorplan.pdf')
OUTPUT_DIR = os.path.join('..','output','floorplan_images')


def extract_pages_as_images(pdf_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    with pdfplumber.open(pdf_path) as pdf:
        for i,page in enumerate(pdf.pages):
            im = page.to_image(resolution=150)
            out_path = os.path.join(out_dir, f'page_{i+1}.png')
            im.save(out_path)
            print('Saved', out_path)


if __name__ == '__main__':
    if not os.path.exists(INPUT):
        print('Place a floorplan PDF at', INPUT)
    else:
        extract_pages_as_images(INPUT, OUTPUT_DIR)
