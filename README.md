# password-strength-checker
A Python-based tool to evaluate password strength using NIST and OWASP guidelines with a simple GUI interface

Password Strength Checker
This is a simple Password Strength Checker implemented in Python using the tkinter library for the graphical user interface (GUI). The checker evaluates the strength of a password based on guidelines inspired by the NIST (National Institute of Standards and Technology) and OWASP (Open Web Application Security Project) frameworks.

Features
Real-Time Feedback: The strength of the password is evaluated as you type, with the strength level displayed and color-coded.
Length Check: Emphasizes longer passwords, giving higher scores to passwords that are at least 12 characters long.
Character Diversity: Considers the presence of uppercase letters, lowercase letters, digits, and special characters.
Entropy Calculation: Calculates the entropy of the password to assess its unpredictability.
Common Password Blacklist: Checks the password against a basic list of commonly used passwords and flags them as "Very Weak".
Reset Functionality: Includes a reset button to clear the password input and reset the progress bar and strength label.
Installation
Prerequisites
Python 3.x
tkinter (This is included with Python by default, so no additional installation is required.)
Clone the Repository
git clone https://github.com/rash2020/password-strength-checker.git
cd password-strength-checker
Running the Program
python password_checker.py
Usage
Run the script using Python.
A GUI window will open where you can enter a password.
The strength of the password will be displayed in real-time, with a corresponding color:
Very Weak: Gray (For common passwords)
Weak: Red
Moderate: Orange
Strong: Blue
Very Strong: Green
Click the "Reset" button to clear the input and start again.
How It Works
Strength Criteria
Length:
12 or more characters: High score
8-11 characters: Moderate score
Less than 8 characters: Low score
Character Types:
Presence of both uppercase and lowercase letters
Inclusion of digits
Inclusion of special characters (e.g., @, $, !, etc.)
Entropy Calculation:
Higher entropy (unpredictability) results in a stronger password rating.
Common Password Blacklist:
The script includes a simple list of common passwords to avoid. If the entered password is in this list, it is marked as "Very Weak".
GUI
The program uses the tkinter library to create a simple graphical interface where users can enter a password and see its strength evaluated dynamically.

Customization
You can expand or modify the list of common passwords in the common_passwords variable. For a more comprehensive check, consider integrating a larger dataset or API.

License
This project is licensed under the MIT License.

Contributing
Feel free to fork this repository and submit pull requests if you'd like to contribute improvements or additional features.
