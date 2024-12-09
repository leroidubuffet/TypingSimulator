import pyautogui
import time
import random
import sys
import os
import signal

min_delay = 0.00001  # Lower min_delay for faster typing
max_delay = 0.001  # Lower max_delay for faster typing
file_path = 'texts/textfile.txt'  # Correct file path


def countdown(seconds):
	for i in range(seconds, 0, -1):
		print(f"Countdown: {i} seconds")
		time.sleep(1)


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

if __name__ == "__main__":
    text = read_text_from_file(file_path)
    if text:
        countdown(5)
        simulate_typing(text)
    else:
        print("No text to type.")
