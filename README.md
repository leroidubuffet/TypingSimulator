# Typing Simulator

This is a Python script that simulates typing text from a specified file on your screen. It's useful for automated typing demonstrations or simulating realistic typing behavior.

---

## Features
- Reads text from a file.
- Simulates typing each character with a randomized delay to mimic natural typing.
- Includes a countdown timer before starting.
- Allows pausing between typing lines for interaction.
- Gracefully cleans up and exits on interruption (e.g., `Ctrl+C`).

---

## Requirements
- Python 3.x
- Libraries:
  - `pyautogui`
  - `time`
  - `random`
  - `sys`
  - `os`
  - `signal`

---

## Setup
### Step 1: Clone or Download the Repository
1. Clone this repository or download the ZIP and extract it:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

### Step 2: Create a Virtual Environment
1. Create a virtual environment using `venv`:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

### Step 3: Install Dependencies
1. Install the required libraries using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

   > If a `requirements.txt` file does not exist yet, create one and add the following line:
   ```
   pyautogui
   ```

---

## How to Use
1. Ensure your virtual environment is activated.
2. Place your text file at the specified location (default is `texts/textfile.txt`).
3. Run the script:
   ```bash
   python typing_simulator.py
   ```
4. After a 5-second countdown, the script will begin typing the text from the file.

---

## Controls
- Press `Enter` after each line to continue.
- To stop the script, use `Ctrl+C`.

---

## Customization
- Adjust the typing speed by modifying the `min_delay` and `max_delay` variables:
  ```python
  min_delay = 0.00001  # Minimum delay between characters
  max_delay = 0.001    # Maximum delay between characters
  ```

- Change the countdown duration by editing the `countdown` call in the main block:
  ```python
  countdown(5)  # Countdown before typing starts
  ```

---

## Notes
- Ensure focus is on the desired input field where the text should be typed before starting the simulation.
- The script will terminate any other Python processes when interrupted. Use caution in multi-process environments.

---

## Disclaimer
This script is for educational or demonstrative purposes only. Ensure you have proper permissions to use it in your intended environment. Misuse of automated tools may violate policies or agreements.