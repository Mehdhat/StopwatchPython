from tkinter import *
import time

class Stopwatch:
    def __init__(self, stopwatch):
        self.stopwatch = stopwatch
        stopwatch.title("Stopwatch")
        stopwatch.geometry("300x250")
        stopwatch.resizable(0, 0)
        stopwatch.configure(bg="#2E2E2E")  # Dark background for the main window

        # Set the icon for the window
        stopwatch.iconbitmap(r'C:\Users\Admin\Downloads\pythonProject1\126.ico')  # Update this path to your .ico file

        # Initialize time variables
        self.running = False
        self.elapsed_time = 0

        # Label to display elapsed time
        self.time_label = Label(stopwatch, text="0", bg="#2E2E2E", fg="white", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        # Start Button
        self.start_button = Button(stopwatch, text="Start", command=self.start, font=("Helvetica", 12), bg="#4CAF50", fg="white", activebackground="#45A049")
        self.start_button.place(x=30, y=150, width=80, height=40)  # Set position and size

        # Stop Button
        self.stop_button = Button(stopwatch, text="Stop", command=self.stop, font=("Helvetica", 12), bg="#F44336", fg="white", activebackground="#D32F2F")
        self.stop_button.place(x=110, y=150, width=80, height=40)  # Set position and size

        # Reset Button
        self.reset_button = Button(stopwatch, text="Reset", command=self.reset, font=("Helvetica", 12), bg="#2196F3", fg="white", activebackground="#1976D2")
        self.reset_button.place(x=190, y=150, width=80, height=40)  # Set position and size

        # Update the stopwatch display
        self.update_display()

    def update_display(self):
        """Update the display label with the elapsed time."""
        if self.running:
            self.elapsed_time += 1
            self.time_label.config(text=str(self.elapsed_time))
        self.stopwatch.after(1000, self.update_display)  # Call this method every second

    def start(self):
        """Start the stopwatch."""
        if not self.running:
            self.running = True

    def stop(self):
        """Stop the stopwatch."""
        self.running = False

    def reset(self):
        """Reset the stopwatch."""
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text="0")

if __name__ == "__main__":
    root = Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
