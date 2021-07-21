import sys
from design2 import Ui_MainWindow
from TheoryW import Ui_TheoryW
from Formulars import Ui_Formulars
from Calculator import Ui_Calculator
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.openTheory)
        self.ui.pushButton_2.clicked.connect(self.openFormula)
        self.ui.pushButton_3.clicked.connect(self.openCalc)

    def openTheory(self):
        theory = Theory(self)
        theory.exec_()

    def openFormula(self):
        formula = Formula(self)
        formula.exec_()

    def openCalc(self):
        calculator = Calculator(self)
        calculator.exec_()


class Theory(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Theory, self).__init__(parent)
        self.uiTheory = Ui_TheoryW()
        self.uiTheory.setupUi(self)


class Formula(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Formula, self).__init__(parent)
        self.uiFormula = Ui_Formulars()
        self.uiFormula.setupUi(self)


class Calculator(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.uiCalculator = Ui_Calculator()
        self.uiCalculator.setupUi(self)

        self.uiCalculator.clear.clicked.connect(self.clear)
        self.uiCalculator.getAnswerGolden.clicked.connect(self.calcGold)
        self.uiCalculator.getAnswerDichotomy.clicked.connect(self.calcDick)


    def calcDick(self):
        function = self.uiCalculator.funcCounts.text()
        limit = self.uiCalculator.sectionCounts.text()
        e = self.uiCalculator.accuracyCounts.text()
        function = eval("lambda x:" + function)
        limit = [float(s) for s in limit.split(" ")]
        e = float(e)
        answer = self.dichotomy(function, limit, e)
        self.uiCalculator.getAnswer.setText("Результат полученный методом Дихотомии:\n"+str(answer))


    def calcGold(self):
        function = self.uiCalculator.funcCounts.text()
        limit = self.uiCalculator.sectionCounts.text()
        e = self.uiCalculator.accuracyCounts.text()
        function = eval("lambda x:" + function)
        limit = [float(s) for s in limit.split(" ")]
        e = float(e)
        answer = self.goldenRatio(function, limit, e)
        self.uiCalculator.getAnswer.setText("Результат полученный методом Золотого Сечения:\n"+str(answer))

    def clear(self):
        self.uiCalculator.getAnswer.setText('')

    def goldenRatio(self, function, limit, e):
        '''
            Метод Золотого Сечения
                                    '''

        goldenNumber = 0.61803

        fX1 = function(limit[0])
        fX2 = function(limit[1])
        xTilde = (limit[1] - limit[0]) * goldenNumber + limit[0]

        if abs(limit[0] - limit[1]) < e:
            return xTilde

        else:
            xDoubleTilde = (limit[1] - xTilde) * goldenNumber + xTilde
            fXtilde = function(xTilde)
            fXdoubleTilde = function(xDoubleTilde)

            if fX1 <= fXtilde < fX2:
                return self.goldenRatio(function, [limit[0], xTilde], e)

            elif fXtilde <= fXdoubleTilde:
                return self.goldenRatio(function, [limit[0], xDoubleTilde], e)

            else:
                return self.goldenRatio(function, [xTilde, limit[1]], e)

    def dichotomy(self, function, limit, e):

        '''
            Метод Дихотомии
                            '''

        x = (limit[0] + limit[1]) / 2

        if abs(limit[0] - limit[1]) < e:
            return x

        else:
            f1 = function(x - e / 2)
            f2 = function(x + e / 2)

            if f1 == f2:
                return x

            elif f1 > f2:
                return self.dichotomy(function, [x, limit[1]], e)

            elif f2 > f1:
                return self.dichotomy(function, [limit[0], x], e)


App = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(App.exec())

