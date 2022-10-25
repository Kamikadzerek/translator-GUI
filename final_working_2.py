# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    # --------------------------Layout generated by Qt Designer--------------------------------------------------------
    def __init__(self):
        self.history = QtWidgets.QLabel(Form)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.edit_input_text = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.btn_translate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.label_translation = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.list_pl = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.list_en = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.label_send = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.btn_yes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_no = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.edit_output_text = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.btn_output = QtWidgets.QPushButton(self.horizontalLayoutWidget)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1359, 1000)
        with open("styles.css", "r") as file:
            Form.setStyleSheet(file.read())

        self.history.setGeometry(QtCore.QRect(240, 220, 81, 50))
        self.history.setObjectName("history")
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 921, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.edit_input_text.setObjectName("edit_input_text")
        self.verticalLayout.addWidget(self.edit_input_text)
        self.btn_translate.setObjectName("btn_translate")
        self.verticalLayout.addWidget(self.btn_translate)
        self.btn_translate.clicked.connect(self.click_translate)
        self.label_translation.setText("")
        self.label_translation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_translation.setObjectName("label_translation")
        self.verticalLayout.addWidget(self.label_translation)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 270, 921, 621))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout.setObjectName("horizontalLayout")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_pl.sizePolicy().hasHeightForWidth())
        self.list_pl.setSizePolicy(sizePolicy)
        self.list_pl.setObjectName("list_pl")
        self.horizontalLayout.addWidget(self.list_pl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_en.sizePolicy().hasHeightForWidth())
        self.list_en.setSizePolicy(sizePolicy)
        self.list_en.setObjectName("list_en")
        self.horizontalLayout.addWidget(self.list_en)
        self.list_en.clicked.connect(self.list_en_clicked)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_send.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_send.setObjectName("label_send")
        self.verticalLayout_3.addWidget(self.label_send)
        self.label_send.setHidden(True)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_yes.sizePolicy().hasHeightForWidth())
        self.btn_yes.setSizePolicy(sizePolicy)
        self.btn_yes.setMinimumSize(QtCore.QSize(0, 200))
        self.btn_yes.setAutoFillBackground(False)
        self.btn_yes.setObjectName("btn_yes")
        self.horizontalLayout_2.addWidget(self.btn_yes)
        self.btn_yes.clicked.connect(self.click_yes)
        self.btn_yes.setHidden(True)
        self.btn_no.setMinimumSize(QtCore.QSize(0, 200))
        self.btn_no.setObjectName("btn_no")
        self.horizontalLayout_2.addWidget(self.btn_no)
        self.btn_no.clicked.connect(self.click_no)
        self.btn_no.setHidden(True)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_output_text.sizePolicy().hasHeightForWidth())
        self.edit_output_text.setSizePolicy(sizePolicy)
        self.edit_output_text.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.edit_output_text.setObjectName("edit_output_text")
        self.verticalLayout_2.addWidget(self.edit_output_text)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_output.sizePolicy().hasHeightForWidth())
        self.btn_output.setSizePolicy(sizePolicy)
        self.btn_output.setObjectName("btn_output")
        self.btn_output.clicked.connect(self.click_output)
        self.verticalLayout_2.addWidget(self.btn_output)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Translator"))
        self.history.setText(_translate("Form", "History"))
        self.edit_input_text.setPlaceholderText(_translate("Form", "Wpisz słówko"))
        self.btn_translate.setText(_translate("Form", "Translate"))
        self.btn_translate.setShortcut(_translate("Form", "Return"))
        self.label_send.setText(_translate("Form", "Send to Anki?"))
        self.btn_yes.setText(_translate("Form", "Yes(1)"))
        self.btn_yes.setShortcut(_translate("Form", "1"))
        self.btn_no.setText(_translate("Form", "No(2)"))
        self.btn_no.setShortcut(_translate("Form", "2"))
        self.edit_output_text.setPlaceholderText(_translate("Form", "output.apkg"))
        self.btn_output.setText(_translate("Form", "Generate Output"))

    def click_translate(self):
        global word
        global slowo
        word = self.edit_input_text.text()
        slowo = translator.translate_text(word, target_lang="PL").text
        # slowo = ts.bing(word, from_language='en', to_language='pl')
        self.label_translation.setText(slowo)



        self.btn_yes.setHidden(False)
        self.btn_no.setHidden(False)
        self.label_send.setHidden(False)
        self.label_send.setFocus()

    def click_yes(self):
        if word not in used:
            en_pl = genanki.Note(
                model=my_model,
                fields=[word, slowo])
            pl_en = genanki.Note(
                model=my_model,
                fields=[slowo, word])
            my_deck.add_note(en_pl)
            my_deck.add_note(pl_en)
            used.append(word)

            list_item_en = QtWidgets.QListWidgetItem(word)
            list_item_en.setBackground(QtGui.QBrush(QtGui.QColor("green")))
            self.list_en.addItem(list_item_en)

            list_item_pl = QtWidgets.QListWidgetItem(slowo)
            list_item_pl.setBackground(QtGui.QBrush(QtGui.QColor("green")))
            self.list_pl.addItem(list_item_pl)
        else:
            list_item_en = QtWidgets.QListWidgetItem(word)
            list_item_en.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))
            self.list_en.addItem(list_item_en)

            list_item_pl = QtWidgets.QListWidgetItem(slowo)
            list_item_pl.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))
            self.list_pl.addItem(list_item_pl)

        self.btn_yes.setHidden(True)
        self.btn_no.setHidden(True)
        self.label_send.setHidden(True)
        self.edit_input_text.setFocus()
        self.edit_input_text.setText("")

    def click_no(self):
        list_item_en = QtWidgets.QListWidgetItem(word)
        list_item_en.setBackground(QtGui.QBrush(QtGui.QColor("red")))
        self.list_en.addItem(list_item_en)

        list_item_pl = QtWidgets.QListWidgetItem(slowo)
        list_item_pl.setBackground(QtGui.QBrush(QtGui.QColor("red")))
        self.list_pl.addItem(list_item_pl)

        self.btn_yes.setHidden(True)
        self.btn_no.setHidden(True)
        self.label_send.setHidden(True)
        self.edit_input_text.setFocus()
        self.edit_input_text.setText("")

    def click_output(self):
        output_name = self.edit_output_text.text()
        if output_name[-5:] != ".apkg":
            output_name = output_name + ".apkg"
        with open('/home/szymek/used.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            [writer.writerow([r]) for r in used]
        genanki.Package(my_deck).write_to_file('/home/szymek/' + output_name)
        app.exit()

    def list_en_clicked(self):
        self.edit_input_text.setText(self.list_en.currentItem().text())


if __name__ == "__main__":
    import sys
    import csv
    import genanki
    import translators as ts
    import deepl
    auth_key = "769f6d51-6827-a8a6-7037-2c20b7137d03:fx"
    translator = deepl.Translator(auth_key)

    global used
    with open('/home/szymek/used.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        used = [r[0] for r in reader]

    style = """
    .card {
     font-family: arial;
     font-size: 30px;
     text-align: center;
     color: black;
     background-color: white;
    }
    """
    my_model = genanki.Model(
        1607392319,
        'Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
        css=style)
    my_deck = genanki.Deck(
        2059400110,
        'Reading_words')

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
