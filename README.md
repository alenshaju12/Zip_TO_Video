# ZIP <-> Video Converter

This project is a Python application that allows users to convert ZIP files into video files and vice versa. The tool encodes the binary data of a ZIP file into a video format, where each frame represents a portion of the data. It also decodes the video back into a ZIP file.

## Features

- Convert ZIP files to video files in AVI format.
- Convert video files back into ZIP files.
- User-friendly graphical interface built with Tkinter.
- Supports data encoding and decoding in binary format.

## Requirements

- Python 3.x
- OpenCV (`cv2` library)
- NumPy
- Tkinter (comes pre-installed with Python)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/alenshaju12/Zip_TO_Video.git
Navigate to the project directory:

bash
Copy code
cd Zip_TO_Video
Install the required packages:

You can install the necessary packages using pip:

bash
Copy code
pip install opencv-python numpy
Usage
Run the application:

Execute the following command in your terminal:

bash
Copy code
python main.py
Choose Conversion Mode:

Upon launching the application, you will see two buttons:

Convert ZIP to Video: Select this option to convert a ZIP file into a video.
Convert Video to ZIP: Select this option to convert a video back into a ZIP file.
Convert ZIP to Video:

Click on the "Convert ZIP to Video" button.
A file dialog will open for you to select the ZIP file you wish to convert.
Next, choose the location and filename to save the resulting video (it will be saved in AVI format).
Upon successful conversion, a message box will display a success message.
Convert Video to ZIP:

Click on the "Convert Video to ZIP" button.
A file dialog will open for you to select the video file you wish to convert.
Next, choose the location and filename to save the reconstructed ZIP file.
Upon successful conversion, a message box will display a success message.
Notes
The tool encodes data in binary, which may result in larger video files than the original ZIP file.
Ensure that the selected video file is in the correct format (AVI) for conversion.
