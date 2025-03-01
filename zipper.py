import os
import zipfile

# Define the files and folder to zip
files_to_zip = ['pack.mcmeta', 'pack.png']
folder_to_zip = 'assets'
output_folder = 'zip-output'
output_zip_file = os.path.join(output_folder, 'DTNxNW-1.6.zip')

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Creating a zip file
with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Add individual files to the zip file
    for file in files_to_zip:
        zipf.write(file)
    
    # Add folder to the zip file
    for root, dirs, files in os.walk(folder_to_zip):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, arcname=os.path.relpath(file_path, os.path.join(folder_to_zip, '..')))

print(f'Files and folder have been zipped into {output_zip_file}')
