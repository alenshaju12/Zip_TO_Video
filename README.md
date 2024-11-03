ZIP <-> Video Converter
Overview
The ZIP <-> Video Converter is a Python-based application that enables users to seamlessly convert ZIP files into video files and vice versa. This innovative tool encodes the binary data of a ZIP file into an AVI video format, where each frame represents a portion of the ZIP data. It also allows users to decode the video back into the original ZIP file format.

Key Features
ZIP to Video Conversion: Effortlessly convert ZIP files to video files in AVI format.
Video to ZIP Conversion: Easily reconstruct ZIP files from video files.
User-Friendly Interface: Intuitive graphical interface built with Tkinter for easy navigation.
Binary Data Support: Handles data encoding and decoding in binary format for accurate conversions.
Requirements
To use the ZIP <-> Video Converter, ensure you have the following installed:

Python 3.x
OpenCV: Required for video processing (opencv-python package).
NumPy: Required for numerical operations.
Tkinter: Usually pre-installed with Python for creating GUI applications.
Installation Instructions
Clone the Repository:

Open your terminal and run:

bash
Copy code
git clone https://github.com/alenshaju12/Zip_TO_Video.git
Navigate to the Project Directory:

bash
Copy code
cd Zip_TO_Video
Install Required Packages:

Use pip to install the necessary packages:

bash
Copy code
pip install opencv-python numpy
How to Use the Application
Run the Application:

Execute the following command in your terminal:

bash
Copy code
python main.py
Choose Conversion Mode:

Upon launching the application, you will see two options:

Convert ZIP to Video: Select this option to convert a ZIP file into a video.
Convert Video to ZIP: Select this option to convert a video back into a ZIP file.
Converting ZIP to Video
Click the Convert ZIP to Video button.
A file dialog will appear for you to select the ZIP file you wish to convert.
Choose the destination and filename to save the resulting video (in AVI format).
After conversion, a success message will be displayed.
Converting Video to ZIP
Click the Convert Video to ZIP button.
A file dialog will prompt you to select the video file for conversion.
Choose the location and filename for the reconstructed ZIP file.
A success message will confirm the conversion.
Important Notes
File Size Considerations: The tool encodes data in binary format, which may result in larger video files compared to the original ZIP files.
File Format: Ensure the selected video file is in the AVI format for successful conversion.
