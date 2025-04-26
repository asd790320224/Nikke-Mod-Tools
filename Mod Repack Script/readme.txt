Script made by gjopin (chatgpt)

Prerequisites
Ensure Python is installed on your system.
Install required Python packages with:
pip install UnityPy Pillow

Set up folders:
Run the script: createfolders.bat

Using getfiles.py
This script copies specific files from a source directory to a target directory based on patterns defined in a JSON file.
Ensure the JSON file is in the same directory as getfiles.py, and set the JSON filename if different.

Run the script:
Open a terminal or command prompt, navigate to the directory containing getfiles.py, and run:
python getfiles.py
This will copy matching files from source_dir to the Original Bundles folder (created in the same directory as getfiles.py).
You may also double click the script to run it.
After the files are copied into the folder, decrypt the entire folder using NAU.


Using repackscript.py
This script unpacks assets from modded files, then repacks and renames them based on patterns found in original files.

Run the script:
Open a terminal, navigate to the directory containing repackscript.py, and execute:
python repackscript.py
You may also double click the script to run it.
The script will process each modded file, unpack its assets, and then repack and rename the original files in Results to match the modded assets.

Check output:
The repacked files, renamed to match modded bundles, will be saved in the Results folder.

Troubleshooting
If there are any errors or missing dependencies, make sure all the required libraries are installed using pip.
Verify that your folder paths are correctly set and that the asset files exist in the correct directories (only for getfiles.py).
By following these steps, you should be able to successfully export, modify, and repack your Unity asset bundles!
If the commands pip install UnityPy Pillow does not work, try replacing "pip" with "python"