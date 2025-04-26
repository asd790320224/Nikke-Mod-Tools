import os
import UnityPy
from PIL import Image

# Change the working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Define paths for modded, original, repacked bundles, and unpacked assets
modded_bundles_folder = os.path.join(script_dir, "Modded Files")
original_bundles_folder = os.path.join(script_dir, "Original Bundles")
repacked_folder = os.path.join(script_dir, "Results")
unpacked_folder = os.path.join(script_dir, "unpacked")

# Ensure the directories exist
os.makedirs(unpacked_folder, exist_ok=True)
os.makedirs(repacked_folder, exist_ok=True)  # Ensure Results folder exists
if not os.path.exists(modded_bundles_folder):
    print(f"Modded bundles folder not found: {modded_bundles_folder}")
    exit()
if not os.path.exists(original_bundles_folder):
    print(f"Original bundles folder not found: {original_bundles_folder}")
    exit()

# Function to unpack Texture2D and TextAsset from modded bundles to the unpacked folder
def unpack_assets(bundle_path):
    env = UnityPy.load(bundle_path)
    for obj in env.objects:
        if obj.type.name == "Texture2D":
            texture_data = obj.read()
            texture_name = getattr(texture_data, 'm_Name', 'unnamed_texture')
            texture_data.image.save(os.path.join(unpacked_folder, f"{texture_name}.png"))
        elif obj.type.name == "TextAsset":
            text_data = obj.read()
            text_name = getattr(text_data, 'm_Name', 'unnamed_text_asset')
            script_content = getattr(text_data, 'm_Script', None)
            if script_content is not None:
                try:
                    if isinstance(script_content, str):
                        script_content = script_content.encode('utf-8', 'replace')  
                    with open(os.path.join(unpacked_folder, f"{text_name}.txt"), "wb") as f:
                        f.write(script_content)
                except Exception as e:
                    print(f"Error writing {text_name}: {e}")
            else:
                print(f"Warning: 'm_Script' attribute not found for TextAsset: {text_name}")
    print(f"Assets unpacked from: {os.path.basename(bundle_path)}")

# Function to repack Texture2D and TextAsset from unpacked folder into original bundles
def repack_assets(original_path):
    env = UnityPy.load(original_path)
    modified = False

    for obj in env.objects:
        if obj.type.name == "Texture2D":
            texture_data = obj.read()
            texture_path = os.path.join(unpacked_folder, f"{texture_data.m_Name}.png")
            if os.path.exists(texture_path):
                img = Image.open(texture_path).convert("RGBA")
                size = texture_data.m_Width, texture_data.m_Height
                texture_data.set_image(img.resize(size))
                modified = True
                print(f"Modified Texture2D: {texture_data.m_Name}")

        elif obj.type.name == "TextAsset":
            text_data = obj.read()
            text_path = os.path.join(unpacked_folder, f"{text_data.m_Name}.txt")
            if os.path.exists(text_path):
                with open(text_path, "rb") as f:
                    script_content = f.read()
                    text_data.m_Script = script_content
                modified = True
                print(f"Modified TextAsset: {text_data.m_Name}")

    if modified:
        repacked_path = os.path.join(repacked_folder, os.path.basename(original_path))
        with open(repacked_path, 'wb') as f:
            f.write(env.file.save(packer="lz4"))
        print(f"Repacked and saved: {os.path.basename(original_path)}")
    else:
        print(f"No changes made to {os.path.basename(original_path)}.")
    return os.path.basename(original_path) if modified else None

# Step 1: Unpack assets from all modded bundle files
for modded_file in os.listdir(modded_bundles_folder):
    modded_path = os.path.join(modded_bundles_folder, modded_file)
    if os.path.isfile(modded_path):
        try:
            unpack_assets(modded_path)
        except Exception as e:
            print(f"Failed to unpack {modded_file}: {e}")

# Step 2: Repack assets into all original bundle files using the unpacked assets
for original_file in os.listdir(original_bundles_folder):
    original_path = os.path.join(original_bundles_folder, original_file)
    if os.path.isfile(original_path):
        repacked_filename = repack_assets(original_path)

        # Step 3: Rename the repacked file based on matched modded bundle name
        if repacked_filename:
            for modded_file in os.listdir(modded_bundles_folder):
                modded_path = os.path.join(modded_bundles_folder, modded_file)
                modded_env = UnityPy.load(modded_path)

                # Check for matching Texture2D names
                match_found = False
                for modded_obj in modded_env.objects:
                    if modded_obj.type.name == "Texture2D":
                        modded_data = modded_obj.read()
                        original_env = UnityPy.load(original_path)

                        for original_obj in original_env.objects:
                            if original_obj.type.name == "Texture2D":
                                original_data = original_obj.read()
                                if modded_data.m_Name == original_data.m_Name:
                                    # Rename the repacked file to the modded bundle name
                                    repacked_path = os.path.join(repacked_folder, repacked_filename)
                                    new_repacked_path = os.path.join(repacked_folder, modded_file)
                                    os.rename(repacked_path, new_repacked_path)
                                    print(f"Renamed {repacked_filename} to {modded_file}")
                                    match_found = True
                                    break
                        if match_found:
                            break

print("Process complete.")
