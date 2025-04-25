import os

directory = "F:/Memories/Ghorepani Poonhill/F07"  # Path to your directory
counter = 3588
extensions = [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".heic", ".heif"]

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    if filename.lower().endswith(tuple(extensions)) and os.path.isfile(filepath):
        file_parts = os.path.splitext(filename)
        newname = f"IMG_{counter:04d}{file_parts[1]}"
        newpath = os.path.join(directory, newname)
        os.rename(filepath, newpath)
        counter += 1
