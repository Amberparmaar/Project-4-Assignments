import os

def rename_files(folder_path, prefix):
    files = os.listdir(folder_path)
    files.sort()  # Sort files alphabetically

    for i, filename in enumerate(files, start=1):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}_{i}{ext}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_path)
            print(f"Renamed: {filename} → {new_name}")

# === EDIT THIS ===
rename_files(
    folder_path=r"D:\python\test_files",
    prefix="test"
)

