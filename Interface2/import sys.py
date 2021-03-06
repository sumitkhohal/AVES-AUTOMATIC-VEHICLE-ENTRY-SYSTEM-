import sys
import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap 
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from interface2 import Ui_Interface2
class aves(QDialog):

    def __init__(self):
        super(aves,self).__init__()
        loadUi('1.ui',self)
        self.logic = 0
        self.value = 1
        self.SHOW.clicked.connect(self.onClicked)
        self.CAPTURE.clicked.connect(self.CaptureClicked)
        self.CLOSE.clicked.connect(self.OffClicked , self.afterclicked)
        
    @pyqtSlot()
    def onClicked(self):
        cap = cv2.VideoCapture(0)
        while (cap.isOpened()):

            ret, frame = cap.read()
            if ret == True:
                self.displayImage(frame, 1)
                cv2.waitKey()

                if (self.logic==2):
                    self.value = self.value+1
                    cv2.imwrite('Images/%s.png'%(self.value), frame)
                    self.logic = 1
            else :
                print('return not found')
        cap.release()
        cv2.destroyAllWindows()

    def CaptureClicked(self): 
        self.logic = 2

    def OffClicked(self):
        cap.close()
        window.close()

    def afterclicked(self):
        
        self.window = QtWidgets.QApplication()
        window.hide()
        self.ui = Ui_Interface2()
        self.ui.setupUi(self, Interface2)
        self.window.show()

    def displayImage(self, img,window=1):
        qformat = QImage.Format_Indexed8

        if len(img.shape) == 3:
                if (img.shape[2]) == 4:
                    qformat = QImage.Format_RGBA888
                else:
                    qformat = QImage.Format_RGB888
                    img = QImage(img, img.shape[1], img.shape[0], qformat)
                    img = img.rgbSwapped()
                    self.imgLabel.setPixmap(QPixmap.fromImage(img))
                    self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

app=QApplication(sys.argv)
window=aves()
window.show()
try:
    sys.exit(app.exec_())
except:
    print('exiting')
