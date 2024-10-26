# Anime Character Detection Project

This project is an end-to-end computer vision pipeline to detect and count anime characters across frames in an anime episode. The program extracts frames, uses the Google Cloud Vision API for character detection, and generates a visual summary of character density using Matplotlib.

## Features

- **Frame Extraction**: Extracts frames from video files.
- **Character Detection**: Uses Google Cloud Vision API to detect and count characters in each frame.
- **Data Visualization**: Generates a bar chart to visualize character density across frames.

## Project Structure

- `data/frames`: Stores extracted frames from the anime episode.
- `outputs/detection_results.txt`: Contains character count results for each frame.
- `scripts/extract_frames.py`: Script to extract frames from the video.
- `scripts/detect_characters.py`: Main script to detect characters and generate outputs.
- `scripts/test_vision_api.py`: Test script for Google Cloud Vision API with a sample image.

## Prerequisites

- Python 3.8+
- Google Cloud SDK, with Vision API enabled
- Matplotlib

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aastharajput06/anime-characters-detection.git

   ```

2. Navigate to the project directory and set up a virtual environment:
   cd anime-character-detection
   python -m venv venv
   source venv/bin/activate # or venv\Scripts\activate on Windows

3. Install required packages:
   pip install -r requirements.txt

4. Add your Google Cloud service-account.json file to the root directory.

Usage

1. Extract Frames:
   python scripts/extract_frames.py

2. Detect Characters:
   python scripts/detect_characters.py

3. View Character Density: Open the generated bar chart in outputs.