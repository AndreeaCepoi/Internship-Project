import os.path
import subprocess
def extract_data(archive_path, destination_dir):
    try:
        if not os.path.exists(archive_path):
            raise FileNotFoundError(f"Archive '{archive_path}' not found")

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        subprocess.run(['tar', 'xzf', archive_path, '-C', destination_dir], check=True)

        print(f"Data from archive '{archive_path}' successfully extracted to '{destination_dir}'")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Error during extraction from archive: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Extraction process completed successfully")


if __name__ == "__main__":

    archive_name = "internshipProject.tar.gz"
    destination_dir = "/home/acepoi/Downloads"

    archive_path = os.path.join(destination_dir, archive_name)
    destination_dir_extract = "/home/acepoi/Downloads/extract_data"

    extract_data(archive_path, destination_dir_extract)
