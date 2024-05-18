# t2s

T2S, a.k.a Text 2 Speech.

## Features

- Changing voice.
- Downloading speech
- Speaking text.

## Installation

Well that's very easy. Just download the `.exe` file in the Releases 
section and install it.

## How to use?

Very easy!

First type the text in the text box.

Then there is a dropdown. You can choose Male (default) or Female

Then click either of the two buttons.

- Speak: For speaking the text.
- Download speech: Downloading the speech

There you go! That's Text 2 Speech for you!

## Programs and Tools Used

As usual, for the GUI I used Qt 6.6 and the base of the GUI was built using Qt's nice tool Qt Designer.

For the text to speech feature I used Pyttsx3.

For operating system related features, I used python's built-in package 'os'.

For some C++ related features I used ctypes.

For editing I used Microsoft Visual Studio 2022 Community.


## Building from source

Its easy to build from source.

So to get started clone the repo using `git clone https://github.com/agnivomallick/t2s.git`

- It is recommended a virtual environment for this.
- Get started by installing `PySide6` and `pyttsx3` using `pip install PySide6 pyttsx3`
- Open the folder of the repo and open the `t2s.py` file
- Run the file using Python 3.9+ interpreter
- If no errors then good
- Editing the code: Adhering to the terms and conditions of the [MIT License](https://github.com/agnivomallick/t2s/blob/main/LICENSE)
- Now you can package your app. I prefer PyInstaller.
- You can use anything else, but you have to see its docs. 
- If you are good with PyInstaller then install using `pip install pyinstaller`
- If you prefer a GUI-based solution for packaging using PyInstaller install `pip install auto-py-to-exe`
- Now you can install UPX if you feel. Download from the github repo of UPX.
- No problem if you don't want.
- If you want to package using command line then type the command:
`pyinstaller --noconfirm --onedir --windowed --icon "<repo/logo.ico>" --name "<any name but t2s is preferred>" --upx-dir "<if you installed upx here the path to the upx.exe file (the dir, not the exe)>" --version-file "<repo/version.yml>" --add-data "<repo/logo.ico>;." --add-data "<repo/ui_t2s.py_>;."  "<repo/t2s.py>"`
repo/logo.ico means the path to the logo.ico file (in the cloned repo)
Same for the others. Place the text inside the placeholders accordingly.
- For GUI based auto-py-to-exe then its fully and a lot customizable.
- Few things have to be kept in mind:
- i. For the Script location is repo/t2s.py (use the Browse button)
- ii. Onefile option will be One Directory
- iii. Icon will be repo/logo.ico
- iv. For additional files use the file chooser and add repo/ui_t2s.py and repo/logo.ico
- v. For name you can give anything you want but t2s is preferred
- vi. For version file it is repo/version.yml
- After this you can customize any way you want and click the Convert .py to .exe button.
- There we go! That's building from source. You can now distribute and ADHERING TO THE MIT LICENSE.

## Licensing
This product is licensed under the terms of the [MIT License](https://github.com/agnivomallick/t2s/blob/main/LICENSE)

## OS Note
This app will run only on Windows.

Why, you may ask?

Because the voice and all thing will not work on all devices. The voices are stored
in a fixed path which exists only on Windows - not others.
