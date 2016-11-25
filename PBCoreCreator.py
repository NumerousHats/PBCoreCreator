import sys
from PBCoreElements import *
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
from genericInputbox import Ui_GenericInputbox

config = None

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.menuBar.setNativeMenuBar(False)

        self.titles = PBcoreTitle(config["title"]["values"], self.title_list)
        self.descriptions = PBcoreDescription(config["description"]["values"], self.description_list)
        self.dates = PBcoreDate(config["date"]["values"], self.date_list)
        self.coverages = PBcoreCoverage(config["coverage"]["values"], self.coverage_list)
        self.creators = PBcoreCreator(config["creator"]["values"], self.creator_list)
        self.contributors = PBcoreContributor(config["creator"]["values"], self.contributor_list)
        self.publishers = PBcorePublisher(config["publisher"]["values"], self.publisher_list)

        ###############
        ##### set up signals/slots
        ###############

        ##### menu items

        # self.ui.actionWhat.triggered.connect(self.what)

        ##### GUI elements

        ## "add" buttons
        self.title_addbutton.clicked.connect(lambda: self.genericInputbox(self.titles))
        self.description_addbutton.clicked.connect(lambda: self.genericInputbox(self.descriptions))
        self.date_addbutton.clicked.connect(lambda: self.genericInputbox(self.dates))
        self.coverage_addbutton.clicked.connect(lambda: self.genericInputbox(self.coverages))
        self.creator_addbutton.clicked.connect(lambda: self.genericInputbox(self.creators))
        self.contributor_addbutton.clicked.connect(lambda: self.genericInputbox(self.contributors))
        self.publisher_addbutton.clicked.connect(lambda: self.genericInputbox(self.publishers))

        # THESE NEED TO HAVE THEIR OWN SPECIAL DIALOGS
        # language
        # rights

        ## "remove" buttons
        ### ????
        self.title_removebutton.clicked.connect(
            lambda: self.debugdump(self.titles))
   
        ## forget about the up/down arrows for now (maybe forever)

        # deal with double clicks on list boxes
        # self.ui.tophit_list.itemDoubleClicked.connect(self.clickAssign)

    def debugdump(self, listobj):
        print(len(listobj))

    def genericInputbox(self, listobj):
        from itertools import groupby

        dlg = StartGenericInputbox()

        all_attributes = listobj.options

        # deal with end delimiter
        attributes = [list(group) for k, group in groupby(all_attributes, lambda x: x == "#") if not k][0]

        # deal with separators
        attributes = [list(group) for k, group in groupby(attributes, lambda x: x == "-") if not k]
        attributes = attributes[::-1]

        this_list = attributes.pop()
        dlg.attribute.addItems(this_list)

        while (len(attributes) > 0):
            dlg.attribute.insertSeparator(dlg.attribute.count())
            this_list = attributes.pop()
            dlg.attribute.addItems(this_list)

        if dlg.exec_():
            input = dlg.getValues()
            data = PBcoreElement(input["attribute"], input["text"])
            listbox = listobj.list_element
            listbox.addItem(str(data))
            listobj.append(data)
        else:
            return

class StartGenericInputbox(QtWidgets.QDialog, Ui_GenericInputbox):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)

    def getValues(self):
        return {"attribute": str(self.attribute.currentText()), "text": self.text.toPlainText()}


if __name__ == "__main__":
    import json

    with open('config.json') as data_file:    
        config = json.load(data_file)

    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()

    sys.exit(app.exec_())

