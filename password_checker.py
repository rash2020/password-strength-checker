import tkinter as tk
from tkinter import ttk
import re

# A sample list of common passwords; in practice, use a more extensive list.
common_passwords = ["123456", "password", "123456789", "qwerty", "12345678", "111111", "123123"]

# Function to check the strength of the password
def check_password_strength(event=None):
    password = password_entry.get()
    strength = 0

    # Check if password is in common password list
    if password in common_passwords:
        strength_label.config(text="Very Weak (Common Password)", foreground="red")
        progress_bar['value'] = 0
        return

    # Check the length of the password
    if len(password) >= 12:
        strength += 2  # Emphasis on length per NIST guidelines
    elif len(password) >= 8:
        strength += 1

    # Check for uppercase and lowercase characters
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1

    # Check for digits
    if re.search(r'[0-9]', password):
        strength += 1

    # Check for special characters
    if re.search(r'[@$!%*?&]', password):
        strength += 1

    # Calculate entropy-based strength
    entropy = len(set(password)) * len(password)
    if entropy > 70:
        strength += 1

    # Update the progress bar and label based on strength
    progress_bar['value'] = strength * 10
    if strength <= 3:
        strength_label.config(text="Weak", foreground="red")
    elif strength == 4 or strength == 5:
        strength_label.config(text="Moderate", foreground="orange")
    elif strength == 6:
        strength_label.config(text="Strong", foreground="blue")
    elif strength >= 7:
        strength_label.config(text="Very Strong", foreground="green")

# Function to reset the fields
def reset_fields():
    password_entry.delete(0, tk.END)
    progress_bar['value'] = 0
    strength_label.config(text="Enter Password", foreground="gray")

# Set up the GUI
root = tk.Tk()
root.title("Password Strength Checker")

# Password label and entry
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=10)
password_entry.bind('<KeyRelease>', check_password_strength)

# Strength label and progress bar
strength_label = tk.Label(root, text="Enter Password", foreground="gray")
strength_label.pack(pady=10)

progress_bar = ttk.Progressbar(root, length=300, maximum=100)
progress_bar.pack(pady=10)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
