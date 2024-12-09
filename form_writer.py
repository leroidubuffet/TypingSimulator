import pyautogui
import time
import random
import sys
import os
import signal

min_delay = 0.00001  # Lower min_delay for faster typing
max_delay = 0.001  # Lower max_delay for faster typing
texts_dir = 'texts/'  # Directory containing text files

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Countdown: {i} seconds")
        time.sleep(1)

def list_text_files(directory):
    """List all text files in the given directory."""
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.txt')]
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        return []

def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def cleanup_and_exit():
    # Terminate all Python instances
    current_pid = os.getpid()
    for line in os.popen("ps ax | grep 'python' | grep -v grep"):
        fields = line.split()
        pid = int(fields[0])
        if pid != current_pid:
            os.kill(pid, signal.SIGKILL)
    sys.exit(0)

def simulate_typing(text):
    try:
        lines = text.splitlines(keepends=True)
        first_line = True
        for line in lines:
            if not first_line:
                input("Press Enter to continue...")
            first_line = False
            time.sleep(1)  # Add a shorter delay to change focus
            for char in line:
                pyautogui.typewrite(char)
                delay = random.uniform(min_delay, max_delay)  # Reduce the delay range for faster typing
                time.sleep(delay)
    except KeyboardInterrupt:
        print("\nProcess terminated by user.")
        cleanup_and_exit()
    finally:
        print("Cleaning up...")

def select_file():
    """Display a menu to select a file from the directory."""
    files = list_text_files(texts_dir)
    if not files:
        print("No text files found in the 'texts/' directory.")
        return None
    
    print("Available text files:")
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")
    
    while True:
        try:
            choice = int(input("Select a file by number (or 0 to exit): "))
            if choice == 0:
                print("Exiting.")
                sys.exit(0)
            if 1 <= choice <= len(files):
                return os.path.join(texts_dir, files[choice - 1])
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    file_path = select_file()
    if file_path:
        text = read_text_from_file(file_path)
        if text:
            countdown(5)
            simulate_typing(text)
        else:
            print("No text to type.")
