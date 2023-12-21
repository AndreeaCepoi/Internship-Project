import os.path
import subprocess
def archive_data(source_dir, archive_name, destination_dir):
    try:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory '{source_dir}' not found")

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        if os.path.exists(os.path.join(destination_dir, archive_name)):
            raise FileExistsError(f"Archive '{archive_name}' already exist in the destination directory")

        archive_path = os.path.join(destination_dir, archive_name)
        subprocess.run(['tar', 'czf', archive_path, '-C', source_dir, '.'], check=True)

        print(f"Archive '{archive_name}' created successfully in '{destination_dir}'")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except FileExistsError as e:
        print(f"Error: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Error during archive creation: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Archive process completed successfully.")


if __name__ == "__main__":

    source_dir="/home/acepoi/Downloads/Internship-Project"
    archive_name="internshipProject.tar.gz"
    destination_dir="/home/acepoi/Downloads"

    archive_data(source_dir, archive_name, destination_dir)

