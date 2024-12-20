# 📅 Timesheet Creator - Python

## 🚀 Overview
Streamline your work hour tracking with the Timesheet Creator! This Python script simplifies the process of generating timesheets, allowing you to input your work hours, observations, and notes with ease. Stay organized and efficient with formatted timesheets for effortless reporting and record-keeping.

## ✨ Features
- **Simple Interface**: Effortlessly input your work hours and observations through an intuitive interface.
- **Customizable Output**: Tailor the format of your timesheets to suit your specific needs and preferences.
- **Automated Calculation**: Let the script handle the math – total work hours are calculated automatically.
- **Observations Section**: Include detailed notes and observations alongside your work hours for comprehensive record-keeping.

## ⚙️ Dependencies
Ensure you have the following dependencies installed:
- customtkinter
- calendar
- datetime
- requests
- argostranslate
- fpdf2
- pathlib
- threading

To install all dependencies, run the following command in your terminal or command prompt:
```bash
pip install -r requirements.txt
```

## 🛠️ Getting Started
1. **Installation**: Clone or download the repository to your local machine.
2. **Dependencies**: Ensure you have Python installed on your system.
3. **Run the Script**: Execute the `timesheet_creator.py` script in your Python environment.
4. **Input Work Hours**: Follow the prompts to input your work hours for each day.
5. **Add Observations**: Optionally, include any relevant observations or notes related to your work hours.
6. **Generate Timesheet**: Once all information is provided, the script will generate a beautifully formatted timesheet.

## 📦 Building an Executable
Take your Timesheet Creator to the next level by building an executable file:
```bash
pyinstaller --noconfirm --onedir --windowed --name "TimeSheetCreator" --icon "path/to/icon.ico" --add-data "path/to/customtkinter;customtkinter/"  "path/to/timesheet_creator.py"
```

## 🤝 Contributions
Your contributions are valuable! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.
