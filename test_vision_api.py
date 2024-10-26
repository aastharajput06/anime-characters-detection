from google.cloud import vision

def test_vision_api(image_path):
    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    
    if response.error.message:
        raise Exception(f"Error from Vision API: {response.error.message}")
    else:
        for label in response.label_annotations:
            print(f"Label: {label.description}, Score: {label.score}")

if __name__ == "__main__":
    test_image_path = "test_image.png"
    test_vision_api(test_image_path)
