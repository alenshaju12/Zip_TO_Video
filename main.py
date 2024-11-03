import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def zip_to_bool_text(zip_file_path, text_file_path):
    with open(zip_file_path, 'rb') as zip_file:
        binary_data = zip_file.read()
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    with open(text_file_path, 'w') as text_file:
        text_file.write(binary_string)
    print(f"ZIP file converted to boolean text and saved to: {text_file_path}")

def bool_text_to_zip(text_file_path, output_zip_path):
    with open(text_file_path, 'r') as text_file:
        binary_string = text_file.read()
    binary_data = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i + 8]
        binary_data.append(int(byte, 2))
    with open(output_zip_path, 'wb') as zip_file:
        zip_file.write(binary_data)
    print(f"Boolean text converted back to ZIP file: {output_zip_path}")

def process_frame(bits, frame_height, frame_width):
    frame = np.zeros((frame_height, frame_width), dtype=np.uint8)
    for i, bit in enumerate(bits):
        y = i // (frame_width // 2)
        x = (i % (frame_width // 2)) * 2
        pixel_value = 255 if bit == '1' else 0
        frame[y, x:x+2] = pixel_value
    return frame

def encode_metadata_frame(bit_count, frame_height, frame_width):
    binary_count = format(bit_count, 'b').zfill(frame_width * frame_height // 2)
    return process_frame(binary_count, frame_height, frame_width)

def decode_metadata_frame(frame):
    bit_count_string = ""
    for y in range(frame.shape[0]):
        for x in range(0, frame.shape[1], 2):
            bit_count_string += '1' if frame[y, x] >= 128 else '0'
    return int(bit_count_string, 2)

def bool_text_to_video(text_file_path, video_filename, frame_width=256, frame_height=256):
    with open(text_file_path, 'r') as text_file:
        binary_string = text_file.read().strip()
    actual_bit_count = len(binary_string)
    bits_per_frame = (frame_width // 2) * frame_height
    num_frames = (actual_bit_count + bits_per_frame - 1) // bits_per_frame

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(video_filename, fourcc, 10.0, (frame_width, frame_height))

    # Write metadata in the first frame
    metadata_frame = encode_metadata_frame(actual_bit_count, frame_height, frame_width)
    video_writer.write(cv2.cvtColor(metadata_frame, cv2.COLOR_GRAY2BGR))

    # Write data frames
    for i in range(num_frames):
        start = i * bits_per_frame
        end = min(start + bits_per_frame, actual_bit_count)
        bits = binary_string[start:end].ljust(bits_per_frame, '0')
        frame = process_frame(bits, frame_height, frame_width)
        for _ in range(2):
            video_writer.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
    video_writer.release()
    print(f"Video created: {video_filename}")

def video_to_bool_text(video_filename, output_text_file_path):
    video_capture = cv2.VideoCapture(video_filename)
    
    # Read metadata from the first frame
    ret, first_frame = video_capture.read()
    if not ret:
        print("Failed to read video.")
        return
    actual_bit_count = decode_metadata_frame(cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY))

    binary_data = []
    frame_count = 1  # Start counting from second frame onward

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        frame_count += 1
        if frame_count % 2 == 0:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            for y in range(gray_frame.shape[0]):
                for x in range(0, gray_frame.shape[1], 2):
                    bit = '1' if gray_frame[y, x] >= 128 else '0'
                    binary_data.append(bit)

    video_capture.release()
    binary_data = binary_data[:actual_bit_count]
    
    with open(output_text_file_path, 'w') as text_file:
        text_file.write(''.join(binary_data))
    print(f"Binary data extracted and saved to: {output_text_file_path}")

def zip_to_video():
    zip_file_path = filedialog.askopenfilename(title="Select ZIP File", filetypes=[("ZIP files", "*.zip")])
    if not zip_file_path:
        return
    text_file_path = "zip_as_text.txt"
    video_filename = filedialog.asksaveasfilename(defaultextension=".avi", title="Save Video As", filetypes=[("AVI files", "*.avi")])
    if not video_filename:
        return
    zip_to_bool_text(zip_file_path, text_file_path)
    bool_text_to_video(text_file_path, video_filename)
    messagebox.showinfo("Success", f"ZIP file converted to video and saved as {video_filename}")

def video_to_zip():
    video_filename = filedialog.askopenfilename(title="Select Video File", filetypes=[("AVI files", "*.avi")])
    if not video_filename:
        return
    output_text_file_path = "reconstructed_data.txt"
    output_zip_path = filedialog.asksaveasfilename(defaultextension=".zip", title="Save ZIP As", filetypes=[("ZIP files", "*.zip")])
    if not output_zip_path:
        return
    video_to_bool_text(video_filename, output_text_file_path)
    bool_text_to_zip(output_text_file_path, output_zip_path)
    messagebox.showinfo("Success", f"Video file converted to ZIP and saved as {output_zip_path}")

def main():
    root = tk.Tk()
    root.title("ZIP <-> Video Converter")
    root.geometry("400x200")

    title_label = tk.Label(root, text="Choose Conversion Mode", font=("Arial", 14))
    title_label.pack(pady=20)

    zip_to_video_btn = tk.Button(root, text="Convert ZIP to Video", command=zip_to_video, width=20, font=("Arial", 12))
    zip_to_video_btn.pack(pady=10)

    video_to_zip_btn = tk.Button(root, text="Convert Video to ZIP", command=video_to_zip, width=20, font=("Arial", 12))
    video_to_zip_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
