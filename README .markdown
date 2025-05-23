# 📹 Video Preprocessing Script README 🚀

Welcome to the **Video Preprocessing Script**! This Python script extracts frames from a video file, resizes them to a specified resolution, and saves them as individual images. Perfect for preparing video data for analysis, machine learning, or other creative projects! 🎥✨

## 📋 Overview

This script takes a video file (e.g., `.mp4`), processes each frame, resizes it to a target resolution (default: 1920x1080), and saves the frames as PNG images in a specified output directory. It uses `imageio` for video handling, `PIL` (Pillow) for image processing, and `numpy` for array operations. 🖼️

## 🛠️ Features

- **📂 Input Validation**: Checks if the video file and output directory exist.
- **🖼️ Frame Extraction**: Extracts each frame from the video.
- **📏 Resizing**: Resizes frames to a user-defined resolution using high-quality Lanczos resampling.
- **💾 Frame Saving**: Saves frames as numbered PNG files (e.g., `frame_000.png`, `frame_001.png`).
- **🚨 Error Handling**: Catches and reports errors during processing.

## 📦 Requirements

To run this script, you need the following Python libraries:

- `imageio` 📽️
- `Pillow` (PIL) 🖼️
- `numpy` 🔢
- `os` 🗂️

Install them using pip:

```bash
pip install imageio pillow numpy
```

For video processing, you may also need `imageio-ffmpeg`:

```bash
pip install imageio-ffmpeg
```

## 📜 Code Explanation

Here’s a breakdown of the `preprocess_video` function:

1. **Input Validation** ✅:
   - Checks if the video file exists at `video_path`. If not, it prints an error and exits. 🚫
   - Creates the `output_dir` if it doesn’t exist. 🗂️

2. **Video Processing** 🎬:
   - Opens the video using `imageio.get_reader`. 📥
   - Iterates through each frame in the video. 🔄

3. **Frame Processing** 🖌️:
   - Converts each frame to a PIL Image for processing. 🖼️
   - Resizes the frame to the `target_size` (default: 1920x1080) using Lanczos resampling for high quality. 📏
   - Converts the resized frame back to a NumPy array and saves it as a PNG file in `output_dir`. 💾

4. **Error Handling** 🛡️:
   - Wraps the processing in a try-except block to catch and report any errors (e.g., corrupted video files). 🚨

5. **Output** 📈:
   - Saves frames as `frame_XXX.png` (e.g., `frame_000.png`, `frame_001.png`).
   - Prints progress messages and the total number of frames saved. ✅

## 🚀 How to Use

1. **Set Up the Environment**:
   - Ensure all required libraries are installed (see Requirements above).

2. **Run the Script**:
   - Update the `video_path` and `output_dir` in the `if __name__ == "__main__":` block with your video file path and desired output directory.

   ```python
   video_path = "path/to/your/video.mp4"  # Replace with your video file
   output_dir = "output_frames"           # Replace with your output folder
   preprocess_video(video_path, output_dir)
   ```

3. **Execute**:
   - Run the script using Python:

   ```bash
   python script.py
   ```

4. **Check Output**:
   - Frames will be saved in the `output_dir` as `frame_000.png`, `frame_001.png`, etc. 🖼️
   - Check the console for progress messages and any errors. 📢

## 📝 Example

```python
preprocess_video("sample_video.mp4", "frames", target_size=(1280, 720))
```

This processes `sample_video.mp4`, resizes frames to 1280x720, and saves them in the `frames` directory. 🎉

## ⚠️ Notes

- Ensure the video file format is supported by `imageio` (e.g., `.mp4`, `.avi`). 📽️
- Large videos may require significant disk space for extracted frames. 💽
- Adjust `target_size` based on your needs (e.g., `(1280, 720)` for smaller frames). 📐
- If errors occur, check the console output for details. 🕵️‍♂️

## 🌟 Contributing

Feel free to fork this script, add features, or improve error handling! Submit pull requests or share ideas to make it even better. 🤝

Happy video processing! 🎥🚀