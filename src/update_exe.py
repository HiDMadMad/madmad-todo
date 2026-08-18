import os

VERSION = "0.2.0"

os.system(f"pyinstaller --onefile --console --icon=../assets/icon.ico --name=\"CheckMate-v{VERSION}\" --paths=. app.py")
#MadMad_6