"""
Author: Agnivo Mallick
Company: Agnivos Software Corporation
Version: 1.0
"""

"""
This program is a text to speech app.
More details can be found in the README.md file.
Comments are there to help you understand the statement.
"""

# importing necessary packages - Qt 6.6, PyTTsx 3, ui file, and os

from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

from ui_t2s import Ui_MainWindow

import pyttsx3 as ptsx3
import os

basedir = os.path.dirname(__file__)  # for getting the file directory. The resources will not get imported if this is not present.

# Only works on Windows.
# For setting the taskbar icon to the custom one.
# A bit of error handling also. (for non-windows OS)

try:
    from ctypes import windll
    
    appid = 'mycompany.myproduct.subproduct.version'
    
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
    
except ImportError:
    pass

# Main window class

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  # inheriting properties of QMainWindow
        

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # setting up the UI
        
        # icon file
        
        self.icon = QIcon()
        self.icon.addFile(os.path.join(basedir, "logo.ico"), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(self.icon)
       
        
        self.ui.speak_now.clicked.connect(lambda: self.sayTheText(self.ui.speech.toPlainText()))
        # connect the speak button to the function that says the text.
        
        self.ui.speak_down.clicked.connect(lambda: self.downloadSpokenText(self.ui.speech.toPlainText()))
        # connect the download button to the function that downloads the text.
        
        self.FEMALE_VOICE = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
        self.MALE_VOICE = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0"
        
        # only works in Windows - these are registry entries present ONLY in Windows.

    def sayTheText(self, textToSay):
        """
        Function to say the text.
        
        Parameter 1: textToSay: The text to say.
        
        Here also the gender choosing is checked and accordingly the text is heard.
        """
        if textToSay == '':
            return
        
        else:
            engine = ptsx3.init()
            

            selectedVoice = self.ui.gender_choose.currentText() # get the selected voice
            
            if selectedVoice == 'Male':
                engine.setProperty('voice', self.MALE_VOICE)
                engine.say(textToSay) # say the text (male)
            
            else:
                engine.setProperty('voice', self.FEMALE_VOICE)
                engine.say(textToSay) # say the text (female)
            
            
            engine.runAndWait()
            
    def downloadSpokenText(self, download_text):
        """
        Function to download the spoken text.
        
        Parameter 1: download_text: The text (same as in sayTheText function )
        
        Here a filedialog is displayed.
        
        And if the path (user cancels operation) is None then nothing happens
        
        If there is a path the PyTTsx engine saves it.
        
        """
        engine = ptsx3.init()

        selected_voice = self.ui.gender_choose.currentText()  # same as sayTheText function
        
        if selected_voice == 'Male':
            engine.setProperty('voice', self.MALE_VOICE)
        else:
            engine.setProperty('voice', self.FEMALE_VOICE)
            

        if download_text == '':
            return
        
        else:
            path, _ = QFileDialog.getSaveFileName(self, "Save Voice", os.getcwd(), "Audio files (*.ogg *.mp3 *.wav)")
            # use the directory (initial) as the current working directory.
            

            if path == '':
                return
            
            else:
                engine.save_to_file(download_text, os.path.relpath(path)) # save file, with relative path from current directory.
                
        engine.runAndWait()  # Fun fact: I forgot so many times to put this statement. So my app wouldn't even work!
                
                
if __name__ == '__main__':
    app = QApplication()
    win = MainWindow()
    win.show()
    app.exec()
    