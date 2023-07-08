from PyQt5 import QtCore, QtGui, QtWidgets

class ImageWindow(QtWidgets.QLabel):

    def __init__(self, img_path, parent=None):
        super(ImageWindow, self).__init__(parent)
        self.setScaledContents(True)
        self.update_image(img_path)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check_updates)
        self.timer.start(5000) # Adjust to desired polling interval (in milliseconds)

    def update_image(self, img_path):
        image = QtGui.QPixmap(img_path)
        if not image.isNull():
            self.setPixmap(image)

    def check_updates(self):
        # Poll for new images and update
        self.update_image('results.png')

def main(img_path):
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ImageWindow(img_path)

    # This function is called whenever a key is pressed
    def keyPressEvent(event):
        # If the key is the 'Escape' key
        if event.key() == QtCore.Qt.Key_Escape:
            # Close the application
            app.quit()

    # Override the keyPressEvent method with the function we just defined
    mainWin.keyPressEvent = keyPressEvent

    mainWin.showFullScreen()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main('results.png')