import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QVBoxLayout, QWidget

class HexEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hex Editor')
        self.setGeometry(100, 100, 800, 600)

        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        self.createMenu()

    def createMenu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        openFile = fileMenu.addAction('Open')
        openFile.triggered.connect(self.openFileDialog)

    def openFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Hex Files (*.hex)", options=options)
        if fileName:
            self.loadFile(fileName)

    def loadFile(self, fileName):
        with open(fileName, 'rb') as file:
            content = file.read()
            hexContent = content.hex()
            formattedHex = ' '.join(hexContent[i:i+2] for i in range(0, len(hexContent), 2))
            self.textEdit.setText(formattedHex)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = HexEditor()
    editor.show()
    sys.exit(app.exec_())
