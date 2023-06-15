import os
import json
import io
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'google_key.json'


def detect_image_features(photo_path) -> vision.EntityAnnotation:
    """Provides a quick start example for Cloud Vision."""

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath(photo_path)

    # Loads the image into memory
    with open(file_name, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image, max_results=18)
    labels = response.label_annotations

    print('Labels:')
    mylist=[]
    for label in labels:
        mylist.append(label.description)
    
    mystring = ""
    for item in mylist:
        mystring = mystring + item+", "
    mystring=mystring[:-1]
    
    results = {
        'labels': labels,
        'string_labels': mystring,
        'list_lables': mylist
    }

    return results