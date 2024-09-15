# Stopwatch Application

## Overview

This is a simple stopwatch application built using Python's Tkinter library. The application features a dark-themed interface with a display for elapsed time and buttons to control the stopwatch. The interface includes an icon at the top to enhance visual appeal.

## Features

- **Start**: Begin timing.
- **Stop**: Pause the stopwatch.
- **Reset**: Reset the elapsed time to zero.
- **Elapsed Time Display**: Shows the current elapsed time.

## Installation

1. Ensure you have Python installed on your system.
2. Tkinter should be included with your Python installation, but make sure it's available.

## Usage

1. Save the provided code into a file named `stopwatch.py`.
2. Place an icon file named `126.ico` in the same directory or update the path in the code to your .ico file.
3. Run the script using Python:

    ```bash
    python stopwatch.py
    ```

4. A window will open with the stopwatch application.

## Code Details

- **Window Title**: "Stopwatch"
- **Window Size**: 300x250 pixels
- **Background Color**: Dark grey (#2E2E2E)
- **Elapsed Time Display**: 
  - Font: Helvetica, 48
  - Background: Dark grey (#2E2E2E)
  - Foreground: White
- **Start Button**:
  - Color: Green (#4CAF50)
  - Font: Helvetica, 12
- **Stop Button**:
  - Color: Red (#F44336)
  - Font: Helvetica, 12
- **Reset Button**:
  - Color: Blue (#2196F3)
  - Font: Helvetica, 12

## Icon

The application uses an icon file for the window. Make sure to update the path to the correct location of your `.ico` file in the script:

```python
stopwatch.iconbitmap(r'C:\Users\Admin\Downloads\pythonProject1\126.ico')
