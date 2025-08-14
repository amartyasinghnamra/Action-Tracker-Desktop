# Action Tracker  Desktop

![License](https://img.shields.io/badge/License-GPLv3-blue.svg)

A desktop app built with Python to track daily activities, rate their outcomes, and improve time management.

![App Screenshot](screenshot.png)

## About The Project

Action Tracker is a desktop app for logging daily activities and rating their outcomes. It helps you organize your habits, understand which activities waste your time, and achieve better time management. This app is especially for those who struggle with managing their time efficiently.

### Built With

* **Python:** The core application logic.
* **Flask:** As a micro web server for the backend.
* **Pandas:** For handling data and CSV operations.
* **PyWebView:** To create the desktop GUI wrapper.
* **HTML / Tailwind CSS / JavaScript:** For the user interface.
* **NSIS:** For creating the Windows installer.

## Getting Started

You can either download the ready-to-use application or build it from the source code.

### For Users (Recommended)

1.  Go to the [**Releases**](https://github.com/YOUR_USERNAME/Action-Tracker-Desktop/releases) page of this repository.
2.  Download the latest `ActionTracker-v1.0-setup.exe` file.
3.  Run the installer and follow the on-screen instructions.

### For Developers

To set up the project locally for development:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/YOUR_USERNAME/Action-Tracker-Desktop.git](https://github.com/YOUR_USERNAME/Action-Tracker-Desktop.git)
    cd Action-Tracker-Desktop
    ```
2.  **Install the required Python packages:**
    ```sh
    python -m pip install -r requirements.txt
    ```
3.  **Run the application:**
    ```sh
    python app.py
    ```

## Usage

1.  Launch the Action Tracker application.
2.  Fill in the details for an action: Action name, Duration, Objective, and Outcome.
3.  Select a rating from the dropdown menu.
4.  Click the **Add** button to log the action.
5.  All changes are automatically saved to an `actions.csv` file located in the same directory as the application.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please see `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

Distributed under the GPLv3 License. See `LICENSE` for more information.

## Author

**AmartyaSinghNamra** - *Copyright (c) 2025*

## Screenshots
<img width="1186" height="793" alt="Screenshot1" src="https://github.com/user-attachments/assets/1fbb4191-6247-44b2-8c4c-b0fe7608fbbc" />
<img width="1173" height="787" alt="Screenshot2" src="https://github.com/user-attachments/assets/386fe880-dce7-4672-b4af-72063b1d4f1a" />
