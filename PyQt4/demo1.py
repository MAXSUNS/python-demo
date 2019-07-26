# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import json

with open("./test.json",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)

jgender=load_dict['gender']
jage=load_dict['age']
jname=load_dict['name']
jheight=load_dict['height']


QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

def resource_path(relative_path):
    """定义一个读取相对路径的函数"""
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class InputDlg(QDialog):
    def __init__(self, parent=None):
        super(InputDlg, self).__init__(parent)

        label1 = QLabel(self.tr("姓名"))
        label2 = QLabel(self.tr("性别"))
        label3 = QLabel(self.tr("年龄"))
        label4 = QLabel(self.tr("身高"))
       # self.label2 = QLabel(self)
       # self.label2.setFixedWidth(600)
       # self.label2.setFixedHeight(400)
       # self.label2.setPixmap(QPixmap(resource_path('resources/test.png')))

        self.nameLabel = QLabel(jname)
        self.nameLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.sexLabel = QLabel(self.tr(jgender))
        self.sexLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.ageLabel = QLabel(jage)
        self.ageLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.statureLabel = QLabel(jheight)
        self.statureLabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        nameButton = QPushButton("...")
        sexButton = QPushButton("...")
        ageButton = QPushButton("...")
        statureButton = QPushButton("...")

        self.connect(nameButton, SIGNAL("clicked()"), self.slotName)
        self.connect(sexButton, SIGNAL("clicked()"), self.slotSex)
        self.connect(ageButton, SIGNAL("clicked()"), self.slotAge)
        self.connect(statureButton, SIGNAL("clicked()"), self.slotStature)

        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.nameLabel, 0, 1)
        layout.addWidget(nameButton, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.sexLabel, 1, 1)
        layout.addWidget(sexButton, 1, 2)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.ageLabel, 2, 1)
        layout.addWidget(ageButton, 2, 2)
        layout.addWidget(label4, 3, 0)
        layout.addWidget(self.statureLabel, 3, 1)
        layout.addWidget(statureButton, 3, 2)

        self.setLayout(layout)

        self.setWindowTitle(self.tr("资料收集"))

    def save(self):
        print(load_dict)
        with open("./test.json", "w") as dump_f:
            json.dump(load_dict, dump_f)

    def Q2S(self, qStr):
        # # QString，如果内容是中文，则直接使用会有问题，要转换成 python string
        return unicode(qStr.toUtf8(), 'utf-8', 'ignore')


    def slotName(self):
        name, ok = QInputDialog.getText(self, self.tr("用户名"),
                                        self.tr("请输入新的名字:"),
                                        QLineEdit.Normal, self.nameLabel.text())
        if ok and (not name.isEmpty()):
            self.nameLabel.setText(name)
            load_dict['name']=self.Q2S(name)
            self.save()
            # print (self.Q2S(name))

    def slotSex(self):
        list = QStringList()
        list.append(self.tr("男"))
        list.append(self.tr("女"))
        sex, ok = QInputDialog.getItem(self, self.tr("性别"), self.tr("请选择性别"), list)

        if ok:
            self.sexLabel.setText(sex)
            load_dict['gender']=self.Q2S(sex)
            self.save()

    def slotAge(self):
        age, ok = QInputDialog.getInteger(self, self.tr("年龄"),
                                          self.tr("请输入年龄:"),
                                          int(self.ageLabel.text()), 0, 150)
        if ok:
            self.ageLabel.setText(str(age))
            load_dict['age']=str(age)
            self.save()

    def slotStature(self):
        stature, ok = QInputDialog.getDouble(self, self.tr("身高"),
                                             self.tr("请输入身高:"),
                                             float(self.statureLabel.text()), 0, 2300.00)
        if ok:
            self.statureLabel.setText(str(stature))
            load_dict['height']=str(stature)
            self.save()


app = QApplication(sys.argv)
form = InputDlg()
form.show()
app.exec_()
