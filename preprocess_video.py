import imageio
import os
from PIL import Image
import numpy as np

def preprocess_video(video_path, output_dir, target_size=(1920, 1080)):
    print(f"Checking video path: {video_path}")
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return
    
    print(f"Creating output directory: {output_dir}")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        print(f"Opening video: {video_path}")
        reader = imageio.get_reader(video_path)
        print("Video opened successfully")
        
        frame_count = 0
        for i, frame in enumerate(reader):
            # Convert frame to PIL Image
            frame = Image.fromarray(frame)
            # Resize to target size
            frame = frame.resize(target_size, Image.Resampling.LANCZOS)
            # Convert back to numpy array for saving
            frame = np.array(frame)
            output_path = os.path.join(output_dir, f"frame_{i:03d}.png")
            imageio.imwrite(output_path, frame)
            print(f"Saved {output_path}")
            frame_count += 1
        print(f"Total {frame_count} frames saved")
        reader.close()
    except Exception as e:
        print(f"Error preprocessing video: {e}")

if __name__ == "__main__":
    # Example usage
    video_path = "path/to/video.mp4"
    output_dir = "output"
    preprocess_video(video_path, output_dir)