import os
import subprocess

def extract_frames(video_path, output_dir, fps=1):
    """
    Extract frames from a video using ffmpeg.

    Args:
        video_path (str): Path to the input video file.
        output_dir (str): Directory to save extracted frames.
        fps (int): Frames per second to extract (default is 1 fps).
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Full path to ffmpeg
    ffmpeg_path = r"C:\Users\Aastha Rajput\Downloads\ffmpeg-n7.1-latest-win64-gpl-7.1\ffmpeg-n7.1-latest-win64-gpl-7.1\bin\ffmpeg.exe"
    
    # Ensure paths with spaces are handled correctly
    command = [
        ffmpeg_path,
        '-i', video_path,
        '-vf', f'fps={fps}',
        os.path.join(output_dir, 'frame_%04d.png')
    ]

    # Use subprocess.run() instead of os.system() for better handling
    subprocess.run(command, check=True)
    print(f"Frames extracted to {output_dir}")

if __name__ == "__main__":
    # Use the absolute path to your video file
    video_file = r"C:\Users\Aastha Rajput\Desktop\anime-character-detection-aastharajput\data\Naruto_ep1.mp4"  
    output_folder = r"C:\Users\Aastha Rajput\Desktop\anime-character-detection-aastharajput\data\frames"       

    extract_frames(video_file, output_folder, fps=1)
