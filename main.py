import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.wiekBar.valueChanged.connect(self.bar_changed)
        self.ui.tentnoBar.valueChanged.connect(self.bar_changed)
        self.ui.cholBar.valueChanged.connect(self.bar_changed)

        self.ui.cholBox.valueChanged.connect(self.box_changed)
        self.ui.wiekBox.valueChanged.connect(self.box_changed)
        self.ui.tentoBox.valueChanged.connect(self.box_changed)
        self.show()


    def box_changed(self):

        self.ui.cholBar.setValue(self.ui.cholBox.value())
        self.ui.wiekBar.setValue(self.ui.wiekBox.value())
        self.ui.tentnoBar.setValue(self.ui.tentoBox.value())


    def bar_changed(self):
        self.ui.tentoBox.setValue(self.ui.tentnoBar.value())
        self.ui.cholBox.setValue(self.ui.cholBar.value())
        self.ui.wiekBox.setValue(self.ui.wiekBar.value())

    def death(self):
        age_death = 0
        age_death = (1/130*self.ui.wiekBar.value())*100
        chol_death = 0
        chol_death = 1/100*(self.ui.cholBar.value()-200)*100
        hearth_death = 0
        if chol_death < 0:
            chol_death = 0
        if self.ui.tentoBox.value() < 50:
            hearth_death = 1/50*(50-self.ui.tentoBox.value())*100
        elif self.ui.cholBox.value() > 100:
            hearth_death = 1/50*(200-self.ui.tentoBox.value()-100)*100

        death = (age_death + chol_death + hearth_death)/3



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())