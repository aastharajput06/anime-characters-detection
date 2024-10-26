import os
from google.cloud import vision

# Ensure Google Cloud credentials are set if not already
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Aastha Rajput/Desktop/anime-character-detection-aastharajput/service-account.json"

def detect_characters(image_path):
    print(f"Processing image: {image_path}")  # Debugging

    client = vision.ImageAnnotatorClient()
    try:
        with open(image_path, 'rb') as image_file:
            content = image_file.read()
            image = vision.Image(content=content)
    except Exception as e:
        print(f"Error reading image {image_path}: {e}")
        return 0

    try:
        response = client.object_localization(image=image)
        objects = response.localized_object_annotations
        if not objects:
            print(f"No objects detected in {image_path}")  # Debugging
    except Exception as e:
        print(f"API request failed for {image_path}: {e}")
        return 0

    character_count = 0
    for obj in objects:
        print(f"Detected object: {obj.name} with confidence {obj.score}")  # Debugging
        if 'Person' in obj.name:
            character_count += 1

    print(f"Character count for {image_path}: {character_count}")  # Debugging
    return character_count

def process_frames(frames_directory): 
    frames = [f for f in os.listdir(frames_directory) if f.endswith('.png')]
    results = []

    if not frames:
        print(f"No frames found in {frames_directory}")
        return results

    for frame in frames: 
        frame_path = os.path.join(frames_directory, frame)
        print(f"Processing frame: {frame_path}")  # Debugging
        count = detect_characters(frame_path)
        results.append((frame, count))
        print(f"Frame {frame} has {count} characters detected")  # Debugging

    print(f"Processed {len(results)} frames")
    return results

def process_frames(frames_directory):
    frames = [f for f in os.listdir(frames_directory) if f.endswith('.png')]
    results = []

    if not frames:
        print(f"No frames found in {frames_directory}")
        return results

    for frame in frames:
        frame_path = os.path.join(frames_directory, frame)
        print(f"Processing frame: {frame_path}")  # Debugging
        count = detect_characters(frame_path)
        results.append((frame, count))
        print(f"Frame {frame} has {count} characters detected")  # Debugging

    return results

if __name__ == "__main__":
    frames_directory = "C:/Users/Aastha Rajput/Desktop/anime-character-detection-aastharajput/data/frames"
    results = process_frames(frames_directory)
    
    # Ensure outputs directory exists
    output_dir = "C:/Users/Aastha Rajput/Desktop/anime-character-detection-aastharajput/outputs"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save results to detection_results.txt in outputs folder
    output_file_path = os.path.join(output_dir, "detection_results.txt")
    print(f"Saving results to: {output_file_path}")  # Debugging

    with open(output_file_path, "w") as f:
        for frame, count in results:
            f.write(f"{frame}: {count}\n")
            print(f"Writing to file: {frame}: {count}")  # Debugging

    # Confirm file contents were written
    with open(output_file_path, "r") as f:
        contents = f.read()
        print("File contents after writing:\n", contents)
        
    print(f"Total frames processed: {len(results)}")
    if os.path.exists(output_file_path):
        print(f"Output file created successfully at {output_file_path}")
    else:
        print("Error: Output file was not created.")
