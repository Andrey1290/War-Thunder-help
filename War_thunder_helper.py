import os
from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from PyQt5.QtGui import QFont

app = QApplication([])

win=QWidget()
win.resize(700,600)
win.setWindowTitle("War Thunder Info")
win.setWindowIcon(QtGui.QIcon("logo.png"))
win.setStyleSheet("background-color: brown")
font = QFont()
font.setPointSize(12)

label_caption=QLabel("Информация про танки в War Thunder!")
label_caption.setFont(font)



label_t=QLabel("Текст")
label_t.setFixedSize(500,400)
label_t.setFont(font)
label_p=QLabel("Картинка")
label_p.setFixedSize(500,400)
label_p.setFont(font)


left=QPushButton("<<")
left.setStyleSheet('background-color: red; color: white;')
right=QPushButton(">>")
right.setStyleSheet('background-color: red; color: white;')

V=QVBoxLayout()
V.addWidget(label_caption)
H1=QHBoxLayout()
H2=QHBoxLayout()

V.addLayout(H1)
V.addLayout(H2)

H1.addWidget(label_t)
H1.addWidget(label_p)
H2.addWidget(left)
H2.addWidget(right)



m=os.path.abspath("1.txt")
t=open(m,encoding="utf-8")
label_t.setText(t.read())
label_p.hide()
pixmapimage = QPixmap("1.png")
w,h=label_p.width(), label_p.height()
pixmapimage = pixmapimage.scaled(500,700,Qt.KeepAspectRatio)
label_p.setPixmap(pixmapimage)
label_p.show()

c=1
def goright():
    global c
    c=c+1
    if c==5:
        c=1
    t=open(str(c)+".txt", encoding="utf-8")
    label_t.setText(t.read())
    
    label_p.hide()
    pixmapimage = QPixmap(str(c)+".png")
    w,h=label_p.width(), label_p.height()
    pixmapimage = pixmapimage.scaled(500,700,Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    label_p.show()

def goleft():
    global c
    c=c-1
    if c==0:
        c=4
    t=open(str(c)+".txt", encoding="utf-8")
    label_t.setText(t.read())
    
    label_p.hide()
    pixmapimage = QPixmap(str(c)+".png")
    w,h=label_p.width(), label_p.height()
    pixmapimage = pixmapimage.scaled(500,700,Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    label_p.show()



right.clicked.connect(goright)
left.clicked.connect(goleft)


win.setLayout(V)

win.show()
app.exec_()