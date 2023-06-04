import os
import shutil

# Define the source directory
source_directory = "/Users/%user%/Downloads"

# Define the destination directories for different file types
destination_directories = {
    ".pdf": "/Volumes/NVMe/tidy-folders/pdf",
    ".png": "/Volumes/NVMe/tidy-folders/images",
    ".jpg": "/Volumes/NVMe/tidy-folders/images",
    ".jpeg": "/Volumes/NVMe/tidy-folders/images",
    ".psd": "/Volumes/NVMe/tidy-folders/images",
    ".procreate": "/Volumes/NVMe/tidy-folders/procreate",
    ".heic": "/Volumes/NVMe/tidy-folders/images",
    ".mp4": "/Volumes/NVMe/tidy-folders/videos",
    ".mov": "/Volumes/NVMe/tidy-folders/videos",
    ".zip": "/Volumes/NVMe/tidy-folders/zip",
    ".rar": "/Volumes/NVMe/tidy-folders/zip",
    ".dmg": "/Volumes/NVMe/tidy-folders/applications",
    ".xlsx": "/Volumes/NVMe/tidy-folders/excel",
    ".csv": "/Volumes/NVMe/tidy-folders/excel",
    ".docx": "/Volumes/NVMe/tidy-folders/documents",
    ".fbx": "/Volumes/NVMe/tidy-folders/3d-models",
    ".fbm": "/Volumes/NVMe/tidy-folders/3d-models",
    ".indd": "/Volumes/NVMe/tidy-folders/indesign",
    
}

# Create destination directories if they don't exist
for directory in destination_directories.values():
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

# Iterate over files in the source directory
for file_name in os.listdir(source_directory):
    # Get the file extension (converted to lowercase)
    file_extension = os.path.splitext(file_name)[1].lower()
    
    # Check if the file extension is in the destination directories dictionary
    if file_extension in destination_directories:
        # Get the destination directory for the file extension
        destination_directory = destination_directories[file_extension]
        
        # Construct the full file paths
        source_path = os.path.join(source_directory, file_name)
        destination_path = os.path.join(destination_directory, file_name)

        try:
            # Move the file to the destination directory (overwrite if exists)
            shutil.move(source_path, destination_path)
            print(f"Moved {file_name} to {destination_directory}")
        except Exception as e:
            print(f"Error occurred while moving {file_name}: {str(e)}")
            continue
    else:
        print(f"Ignored {file_name}")
