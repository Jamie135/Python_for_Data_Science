import os
import shutil


def delete_pycache_folders(directory):
    for root, dirs, files in os.walk(directory):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            try:
                shutil.rmtree(pycache_path)
                print(f"Deleted: {pycache_path}")
            except Exception as e:
                print(f"Error deleting {pycache_path}: {e}")


delete_pycache_folders('.')
