import PyInstaller.__main__
import os

# --- Configuration ---
APP_NAME = "ActionTracker"
SCRIPT_FILE = "app.py"
ICON_FILE = "icon.ico"

def build_executable():
    """
    Builds the application into a single executable file.
    """
    print("--- Starting the build process ---")

    pyinstaller_options = [
        '--name=%s' % APP_NAME,
        '--onefile',
        '--windowed',
        '--add-data=%s%s%s' % (os.path.join('templates', 'index.html'), os.pathsep, 'templates'),
    ]

    if os.path.exists(ICON_FILE):
        pyinstaller_options.append('--icon=%s' % ICON_FILE)
        print(f"Icon found: {ICON_FILE}")
    else:
        print("Warning: No icon.ico file found. Using default icon.")

    pyinstaller_options.append(SCRIPT_FILE)

    print(f"\nRunning PyInstaller with options:\n{pyinstaller_options}\n")

    PyInstaller.__main__.run(pyinstaller_options)

    print("\n--- Build process completed! ---")
    print(f"You can find your executable in the 'dist' folder: dist\\{APP_NAME}.exe")


if __name__ == "__main__":
    build_executable()