from djitellopy import Tello

from examples.simple import run_tello_drone
import subprocess


def run_record_video():
    """
    Function to run the record-video.py script from within the main.py file.
    """
    try:
        # Run the 'record-video.py' script using subprocess
        subprocess.run(['python', 'record-video.py'], check=True)
        print("Video recording completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error while running the script: {e}")
    except FileNotFoundError:
        print("Error: The file 'record-video.py' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("Starting the drone operation...")
    #run_tello_drone()
    run_record_video()
