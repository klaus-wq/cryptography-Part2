from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDesktopWidget

from window import Ui_MainWindow
import sys
from basicAlgWindow import Ui_BasicAlg
from basicAlg import gcd, exgcd, degree
from RSAWindow import Ui_RSAWind
from RSA import find_e, RSA, find_d
from HellmanWindow import Ui_HellmanWind
from primes import generator, isPrime
from hellman import find_g, find_pq
from ShamirWindow import Ui_ShamirWind
from shamir import find_C
from GamalWindow import Ui_GamalWind
from random import randint
from gamal import find_X

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        if self.ui.comboBox.currentText() == "Базовые алгоритмы теории чисел":
            self.ex = basicAlgWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "RSA":
            self.ex = RSAWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Диффи-Хеллман":
            self.ex = HellmanWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Шамир":
            self.ex = ShamirWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "Эль - Гамаль":
            self.ex = GamalWindow()
            self.ex.show()

class basicAlgWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(basicAlgWindow, self).__init__()
        self.ui = Ui_BasicAlg()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)


    def btnClicked(self):
        a = self.ui.plainTextEdit.toPlainText()
        b = self.ui.plainTextEdit_2.toPlainText()
        if not a or not b:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите a и b!", QtWidgets.QMessageBox.Ok)
            return None
        try:
            a = int(a)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        try:
            b = int(b)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        self.ui.plainTextEdit_3.setPlainText(gcd(a, b))

    def btnClicked_2(self):
        a = self.ui.plainTextEdit_4.toPlainText()
        deg = self.ui.plainTextEdit_5.toPlainText()
        p = self.ui.plainTextEdit_6.toPlainText()
        if not a or not deg or not p:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите числа!", QtWidgets.QMessageBox.Ok)
            return None
        try:
            a = int(a)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        try:
            deg = int(deg)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        try:
            p = int(p)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        if p == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Модуль != 0!", QtWidgets.QMessageBox.Ok)
            return None
        self.ui.plainTextEdit_7.setPlainText(degree(a, deg, p))


    def btnClicked_3(self):
        a = self.ui.plainTextEdit_8.toPlainText()
        p = self.ui.plainTextEdit_9.toPlainText()
        if not a or not p:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите числа!", QtWidgets.QMessageBox.Ok)
            return None
        try:
            a = int(a)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        try:
            p = int(p)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            return None
        self.ui.plainTextEdit_10.setPlainText(exgcd(a, p))

    def btnClicked_4(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.plainTextEdit_4.clear()
        self.ui.plainTextEdit_5.clear()
        self.ui.plainTextEdit_6.clear()
        self.ui.plainTextEdit_7.clear()
        self.ui.plainTextEdit_8.clear()
        self.ui.plainTextEdit_9.clear()
        self.ui.plainTextEdit_10.clear()

class RSAWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(RSAWindow, self).__init__()
        self.ui = Ui_RSAWind()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)
        self.ui.pushButton_5.clicked.connect(self.btnClicked_5)
        self.ui.pushButton_6.clicked.connect(self.btnClicked_6)
        self.ui.pushButton_7.clicked.connect(self.btnClicked_7)
        self.ui.pushButton_8.clicked.connect(self.btnClicked_8)

#генерация
    def btnClicked(self):
        primes = generator(10**100, 10**101, 2)
        p = primes[0]
        q = primes[1]
        self.ui.plainTextEdit.setPlainText(str(p))
        self.ui.plainTextEdit_2.setPlainText(str(q))

#проверка на простоту
    def btnClicked_2(self):
        p = self.ui.plainTextEdit.toPlainText()
        q = self.ui.plainTextEdit_2.toPlainText()
        if not p or not q:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите простые числа!", QtWidgets.QMessageBox.Ok)
            return None
        try:
            p = int(p)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            self.ui.plainTextEdit.clear()
            return None
        try:
            q = int(q)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            self.ui.plainTextEdit_2.clear()
            return None
        if isPrime(p) == False:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число р составное!", QtWidgets.QMessageBox.Ok)
            self.ui.plainTextEdit.clear()
            return None
        if isPrime(q) == False:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q составное!", QtWidgets.QMessageBox.Ok)
            self.ui.plainTextEdit_2.clear()
            return None
        if isPrime(p) == True and isPrime(q) == True:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Пройдено!")
            msgBox.setText("Числа простые!")
            msgBox.exec_()
            return None

#генерация ключей
    def btnClicked_3(self):
        if self.isCorrect() == None:
            return None

#зашифровать
    def btnClicked_4(self):
        if self.isCorrect() == None:
            return None
        else:
            p = self.ui.plainTextEdit.toPlainText()
            q = self.ui.plainTextEdit_2.toPlainText()
            e = self.ui.plainTextEdit_3.toPlainText()
            text = self.ui.plainTextEdit_7.toPlainText()
            if not text:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите сообщение!", QtWidgets.QMessageBox.Ok)
                return None

            tmp = RSA(text, int(p), int(q), 1, 0, "", int(e), "")
            if type(tmp) == int:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка!")
                msgBox.setText("Модуль p*q должен быть больше " + str(tmp) + '!')
                msgBox.exec_()
                return None
            else:
                self.ui.plainTextEdit_8.setPlainText(tmp)

#расшифровать
    def btnClicked_5(self):
        if self.isCorrect1() == None:
            return None
        else:
            d = self.ui.plainTextEdit_5.toPlainText()
            p = self.ui.plainTextEdit.toPlainText()
            q = self.ui.plainTextEdit_2.toPlainText()

            text = self.ui.plainTextEdit_8.toPlainText()
            if not text:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите сообщение!", QtWidgets.QMessageBox.Ok)
                return None
            tmp = RSA(text, int(p), int(q), 0, 0, "", "", int(d))
            if tmp == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Расшифровывается только поток чисел через пробел!", QtWidgets.QMessageBox.Ok)
                return None
            elif type(tmp) == int:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка!")
                msgBox.setText("Модуль p*q должен быть больше " + str(tmp) + '!')
                msgBox.exec_()
                return None
            else:
                self.ui.plainTextEdit_9.setPlainText(tmp)

#зашифровать файл
    def btnClicked_6(self):
        if self.isCorrect() == None:
            return None
        else:
            p = self.ui.plainTextEdit.toPlainText()
            q = self.ui.plainTextEdit_2.toPlainText()
            e = self.ui.plainTextEdit_3.toPlainText()
            path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            if path == "":
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Откройте файл!")
                msgBox.exec_()
                return None

            file = open(path, 'rb')
            text = file.read()
            file.close()

            res = RSA(text, int(p), int(q), 1, 1, "", int(e), "")
            path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            if path == "":
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Откройте файл!")
                msgBox.exec_()
                return None
            file = open(path, 'w')
            file.write(res)
            file.close()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Успешно")
            msgBox.setText("Успешно выгружено!")
            msgBox.exec_()
            return ("")

#расшифровать файл
    def btnClicked_7(self):
        if self.isCorrect1() == None:
            return None
        else:
            d = self.ui.plainTextEdit_5.toPlainText()
            p = self.ui.plainTextEdit.toPlainText()
            q = self.ui.plainTextEdit_2.toPlainText()

            path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            if path == "":
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Откройте файл!")
                msgBox.exec_()
                return None

            file = open(path, 'r')
            text = file.read()
            file.close()

            path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            if path == "":
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Откройте файл!")
                msgBox.exec_()
                return None
            res = RSA(text, int(p), int(q), 0, 1, path, "", int(d))
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Успешно")
            msgBox.setText("Успешно выгружено!")
            msgBox.exec_()
            return ("")

    def isCorrect(self):
        p = self.ui.plainTextEdit.toPlainText()
        q = self.ui.plainTextEdit_2.toPlainText()
        e = self.ui.plainTextEdit_3.toPlainText()
        if p:
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit.clear()
                return None
            if isPrime(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число р составное!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit.clear()
                return None
        if q:
            try:
                q = int(q)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit_2.clear()
                return None
            if isPrime(q) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q составное!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit_2.clear()
                return None
        if p == q:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p == q!", QtWidgets.QMessageBox.Ok)
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit_2.clear()
            return None
        if not p and not q:
            primes = generator(10**100, 10**101, 2)
            p = primes[0]
            q = primes[1]
            self.ui.plainTextEdit.setPlainText(str(p))
            self.ui.plainTextEdit_2.setPlainText(str(q))
        elif not p:
            p = generator(10**100, 10**101, 1)[0]
            self.ui.plainTextEdit.setPlainText(str(p))
        elif not q:
            q = generator(10**100, 10**101, 1)[0]
            self.ui.plainTextEdit_2.setPlainText(str(q))
        if e:
            try:
                e = int(e)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Сгенерируете число в качестве открытого ключа!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit_3.clear()
                return None
        if e:
            if e >= (p-1)*(q-1):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "e > (p-1)*(q-1)!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit_3.clear()
                e = find_e(p, q)
                self.ui.plainTextEdit_3.setPlainText(str(e))
                d = find_d(e, p, q)
                self.ui.plainTextEdit_5.setPlainText(str(d))
                self.ui.plainTextEdit_4.setPlainText(str(p * q))
                self.ui.plainTextEdit_6.setPlainText(str(p * q))
                return None
            if gcd(e, (p-1)*(q-1)) != '1' and (gcd(e, p-1) == gcd(e, q-1)) != '1' and exgcd(e, (p-1)*(q-1)) == 'Обратный элемент не существует!':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите другое е!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit_3.clear()
                e = find_e(p, q)
                self.ui.plainTextEdit_3.setPlainText(str(e))
                d = find_d(e, p, q)
                self.ui.plainTextEdit_5.setPlainText(str(d))
                self.ui.plainTextEdit_4.setPlainText(str(p * q))
                self.ui.plainTextEdit_6.setPlainText(str(p * q))
                return None
            else:
                d = find_d(e, p, q)
                self.ui.plainTextEdit_5.setPlainText(str(d))
                self.ui.plainTextEdit_4.setPlainText(str(p * q))
                self.ui.plainTextEdit_6.setPlainText(str(p * q))
        if not e:
            e = find_e(p, q)
            d = find_d(e, p, q)
            self.ui.plainTextEdit_3.setPlainText(str(e))
            self.ui.plainTextEdit_5.setPlainText(str(d))
            self.ui.plainTextEdit_4.setPlainText(str(p*q))
            self.ui.plainTextEdit_6.setPlainText(str(p*q))
        return True

    def isCorrect1(self):
        d = self.ui.plainTextEdit_5.toPlainText()
        if d:
            try:
                d = int(d)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Сгенерируете число в качестве закрытого ключа!",
                                               QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit_5.clear()
                return None
        if not d:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Сгенерируете число в качестве закрытого ключа!",
                                           QtWidgets.QMessageBox.Ok)
            return None
        p = self.ui.plainTextEdit.toPlainText()
        if p:
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit.clear()
                return None
            if isPrime(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число р составное!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit.clear()
                return None
        q = self.ui.plainTextEdit_2.toPlainText()
        if q:
            try:
                q = int(q)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit_2.clear()
                return None
            if isPrime(q) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q составное!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit_2.clear()
                return None
        if not p or not q:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите простые числа!", QtWidgets.QMessageBox.Ok)
            return None
        return True

    def btnClicked_8(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.plainTextEdit_4.clear()
        self.ui.plainTextEdit_5.clear()
        self.ui.plainTextEdit_6.clear()
        self.ui.plainTextEdit_7.clear()
        self.ui.plainTextEdit_8.clear()
        self.ui.plainTextEdit_9.clear()

class HellmanWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(HellmanWindow, self).__init__()
        self.ui = Ui_HellmanWind()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_5.clicked.connect(self.btnClicked_5)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)
        self.ui.pushButton_8.clicked.connect(self.btnClicked_8)

#генерация простых чисел
    def btnClicked(self):
        p, q = find_pq()
        self.ui.plainTextEdit.setPlainText(str(p))
        self.ui.plainTextEdit_2.setPlainText(str(q))

#найти g
    def btnClicked_2(self):
        if self.isCorrect() == None:
            return None

#проверка на простоту
    def btnClicked_5(self):
        p = self.ui.plainTextEdit.toPlainText()
        q = self.ui.plainTextEdit_2.toPlainText()
        if not p or not q:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите простые числа!", QtWidgets.QMessageBox.Ok)
            return None
        try:
            p = int(p)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            self.ui.plainTextEdit.clear()
            return None
        try:
            q = int(q)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            self.ui.plainTextEdit_2.clear()
            return None
        if isPrime(p) == False:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число р составное!", QtWidgets.QMessageBox.Ok)
            self.ui.plainTextEdit.clear()
            return None
        if isPrime(q) == False:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q составное!", QtWidgets.QMessageBox.Ok)
            self.ui.plainTextEdit_2.clear()
            return None
        if isPrime(p) == True and isPrime(q) == True:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Пройдено!")
            msgBox.setText("Числа простые!")
            msgBox.exec_()
            return None

#общий ключ
    def btnClicked_3(self):
        if self.isCorrect() == None:
            return None
        else:
            p = int(self.ui.plainTextEdit.toPlainText())
            g = int(self.ui.plainTextEdit_10.toPlainText())

            Xa = randint(10**50, p - 1)
            Xb = randint(10**50, p - 1)
            Ya = int(degree(g, Xa, p))
            Yb = int(degree(g, Xb, p))
            Zab = int(degree(Yb, Xa, p))
            Zba = int(degree(Ya, Xb, p))
            self.ui.plainTextEdit_3.setPlainText(str(Ya))
            self.ui.plainTextEdit_4.setPlainText(str(Xa))
            self.ui.plainTextEdit_5.setPlainText(str(Yb))
            self.ui.plainTextEdit_6.setPlainText(str(Xb))
            self.ui.plainTextEdit_7.setPlainText(str(Zab))
            self.ui.plainTextEdit_8.setPlainText(str(Zba))

#выгрузить
    def btnClicked_4(self):
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return None

        file = open(path, 'w')
        file.write(self.ui.plainTextEdit_7.toPlainText())
        file.close()
        msgBox = QtWidgets.QMessageBox()
        msgBox.setWindowTitle("Успешно")
        msgBox.setText("Успешно выгружено!")
        msgBox.exec_()
        return ("")

    def isCorrect(self):
        p = self.ui.plainTextEdit.toPlainText()
        q = self.ui.plainTextEdit_2.toPlainText()
        g = self.ui.plainTextEdit_10.toPlainText()
        if q:
            try:
                q = int(q)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit_2.clear()
                return None
            if isPrime(q) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q составное!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit_2.clear()
                return None
        if p:
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit.clear()
                return None
            if isPrime(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p составное!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit.clear()
                return None
            if q:
                if int(p) != 2 * int(q) + 1:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p != 2*q+1!", QtWidgets.QMessageBox.Ok)
                    self.ui.plainTextEdit.clear()
                    return None
        if q and not p:
            p = 2 * q + 1
            if isPrime(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p составное! Введите другое q!", QtWidgets.QMessageBox.Ok)
                return None
            else:
                self.ui.plainTextEdit.setPlainText(str(p))
        if p and not q:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите сначала q!", QtWidgets.QMessageBox.Ok)
            return None
        if not p and not q:
            p, q = find_pq()
            self.ui.plainTextEdit.setPlainText(str(p))
            self.ui.plainTextEdit_2.setPlainText(str(q))
        if g:
            try:
                g = int(g)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit_10.clear()
                return None
            if degree(g, q, p) == '1':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "g^q mod p == 1!", QtWidgets.QMessageBox.Ok)
                self.ui.plainTextEdit_10.clear()
                return None
        if not g:
            g = find_g(q, p)
            self.ui.plainTextEdit_10.setPlainText(str(g))
        return True

    def btnClicked_8(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.plainTextEdit_4.clear()
        self.ui.plainTextEdit_5.clear()
        self.ui.plainTextEdit_6.clear()
        self.ui.plainTextEdit_7.clear()
        self.ui.plainTextEdit_8.clear()
        self.ui.plainTextEdit_10.clear()

class ShamirWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ShamirWindow, self).__init__()
        self.ui = Ui_ShamirWind()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)
        self.ui.pushButton_5.clicked.connect(self.btnClicked_5)
        self.ui.pushButton_8.clicked.connect(self.btnClicked_8)
        self.ui.pushButton_6.clicked.connect(self.btnClicked_6)
        self.ui.pushButton_7.clicked.connect(self.btnClicked_7)

#генерация
    def btnClicked(self):
        p = generator(10**100, 10**101, 1)[0]
        Ca = find_C(int(p))
        Cb = find_C(int(p))
        self.ui.p.setPlainText(str(p))
        self.ui.Ca.setPlainText(str(Ca))
        self.ui.Cb.setPlainText(str(Cb))

#найти C и d
    def btnClicked_3(self):
        if self.isCorrect() == None:
            return None

#проверка на простоту
    def btnClicked_2(self):
        p = self.ui.p.toPlainText()
        if not p:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите простые числа числа!", QtWidgets.QMessageBox.Ok)
            return None
        try:
            p = int(p)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            self.ui.p.clear()
            return None
        if isPrime(p) == False:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число р составное!", QtWidgets.QMessageBox.Ok)
            self.ui.p.clear()
            return None
        if isPrime(p) == True:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Пройдено!")
            msgBox.setText("Числа простые!")
            msgBox.exec_()
            return None

#отправить сообщение целиком
    def btnClicked_5(self):
        if self.isCorrect() == None:
            return None
        else:
            p = self.ui.p.toPlainText()
            Ca = self.ui.Ca.toPlainText()
            da = self.ui.da.toPlainText()
            Cb = self.ui.Cb.toPlainText()
            db = self.ui.db.toPlainText()
            m = self.ui.m.toPlainText()
            if not m:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите сообщение!", QtWidgets.QMessageBox.Ok)
                return None
            for i in m:
                tmp = ord(i)
                if tmp > int(p):
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setWindowTitle("Ошибка!")
                    msgBox.setText("Модуль p должен быть больше " + str(tmp) + '!')
                    msgBox.exec_()
                    return None
                else:
                    x1 = int(degree(tmp, int(Ca), int(p)))
                    x2 = int(degree(x1, int(Cb), int(p)))
                    x3 = int(degree(x2, int(da), int(p)))
                    x4 = int(degree(x3, int(db), int(p)))
                    self.ui.mi.setPlainText(str(tmp))
                    self.ui.x1.setPlainText(str(x1))
                    self.ui.x2.setPlainText(str(x2))
                    self.ui.x3.setPlainText(str(x3))
                    self.ui.x4.setPlainText(str(x4))
                    res = self.ui.plainTextEdit_13.toPlainText()
                    res+=chr(x4)
                    self.ui.plainTextEdit_13.setPlainText(res)

#отправить сообщение поэтапно
    def btnClicked_4(self):
        if self.isCorrect() == None:
            return None
        else:
            i = len(self.ui.plainTextEdit_13.toPlainText())
            p = self.ui.p.toPlainText()
            Ca = self.ui.Ca.toPlainText()
            da = self.ui.da.toPlainText()
            Cb = self.ui.Cb.toPlainText()
            db = self.ui.db.toPlainText()
            m = self.ui.m.toPlainText()
            if not m:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите сообщение!", QtWidgets.QMessageBox.Ok)
                return None
            if i >= len(m):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Cообщение передано целиком!", QtWidgets.QMessageBox.Ok)
                return None
            tmp = ord(m[i])
            if tmp > int(p):
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка!")
                msgBox.setText("Модуль p должен быть больше " + str(tmp) + '!')
                msgBox.exec_()
                return None
            else:
                x1 = int(degree(tmp, int(Ca), int(p)))
                x2 = int(degree(x1, int(Cb), int(p)))
                x3 = int(degree(x2, int(da), int(p)))
                x4 = int(degree(x3, int(db), int(p)))
                self.ui.mi.setPlainText(str(tmp))
                self.ui.x1.setPlainText(str(x1))
                self.ui.x2.setPlainText(str(x2))
                self.ui.x3.setPlainText(str(x3))
                self.ui.x4.setPlainText(str(x4))
                res = self.ui.plainTextEdit_13.toPlainText()
                res+=chr(x4)
                self.ui.plainTextEdit_13.setPlainText(res)

    def isCorrect(self):
        p = self.ui.p.toPlainText()
        Ca = self.ui.Ca.toPlainText()
        da = self.ui.da.toPlainText()
        Cb = self.ui.Cb.toPlainText()
        db = self.ui.db.toPlainText()
        if p:
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.p.clear()
                return None
            if isPrime(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p составное!", QtWidgets.QMessageBox.Ok)
                self.ui.p.clear()
                return None
        else:
            p = generator(10**100, 10**101, 1)[0]
            self.ui.p.setPlainText(str(p))
        if da:
            try:
                da = int(da)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.da.clear()
                return None
        if db:
            try:
                db = int(db)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.db.clear()
                return None
        if Ca:
            try:
                Ca = int(Ca)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.Ca.clear()
                return None
            if gcd(int(Ca), int(p) - 1) != '1':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "gcd(Ca, p - 1) != 1!", QtWidgets.QMessageBox.Ok)
                self.ui.Ca.clear()
                return None
            if da:
                if (int(Ca) * int(da)) % (int(p) - 1) != 1:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Ca*da != 1 mod (p - 1)!", QtWidgets.QMessageBox.Ok)
                    self.ui.da.clear()
                    return None
            else:
                da = exgcd(int(Ca), int(p) - 1)
                self.ui.da.setPlainText(str(da))
        if Cb:
            try:
                Cb = int(Cb)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.Cb.clear()
                return None
            if gcd(int(Cb), int(p) - 1) != '1':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "gcd(Cb, p - 1) != 1!", QtWidgets.QMessageBox.Ok)
                self.ui.Cb.clear()
                return None
            if db:
                if (int(Cb) * int(db)) % (int(p) - 1) != 1:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Cb*db != 1 mod (p - 1)!", QtWidgets.QMessageBox.Ok)
                    self.ui.db.clear()
                    return None
            else:
                db = exgcd(int(Cb), int(p) - 1)
                self.ui.db.setPlainText(str(db))
        if Ca and not da:
            da = exgcd(int(Ca), int(p) - 1)
            self.ui.da.setPlainText(str(da))
        if Cb and not db:
            db = exgcd(int(Cb), int(p) - 1)
            self.ui.db.setPlainText(str(db))
        if not Ca:
            Ca = find_C(int(p))
            da = exgcd(int(Ca), int(p) - 1)
            self.ui.Ca.setPlainText(str(Ca))
            self.ui.da.setPlainText(str(da))
        if not Cb:
            Cb = find_C(int(p))
            db = exgcd(int(Cb), int(p) - 1)
            self.ui.Cb.setPlainText(str(Cb))
            self.ui.db.setPlainText(str(db))
        return True

    def btnClicked_6(self):
        if self.isCorrect() == None:
            return None
        else:
            p = self.ui.p.toPlainText()
            Ca = self.ui.Ca.toPlainText()
            da = self.ui.da.toPlainText()
            Cb = self.ui.Cb.toPlainText()
            db = self.ui.db.toPlainText()
            path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            if path == "":
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Откройте файл!")
                msgBox.exec_()
                return None

            file = open(path, 'rb')
            text = file.read()
            file.close()

            path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            if path == "":
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Выберите файл для выгрузки!")
                msgBox.exec_()
                return None

            file = open(path, 'wb')
            for i in range(len(text)):
                x1 = int(degree(int(text[i]), int(Ca), int(p)))
                x2 = int(degree(x1, int(Cb), int(p)))
                x3 = int(degree(x2, int(da), int(p)))
                x4 = int(degree(x3, int(db), int(p)))
                file.write(bytes([x4]))
            file.close()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Успешно")
            msgBox.setText("Успешно выгружено!")
            msgBox.exec_()
            return None

    def btnClicked_8(self):
        self.ui.m.clear()
        self.ui.plainTextEdit_13.clear()
        self.ui.mi.clear()
        self.ui.x1.clear()
        self.ui.x2.clear()
        self.ui.x3.clear()
        self.ui.x4.clear()

    def btnClicked_7(self):
        self.ui.p.clear()
        self.ui.Ca.clear()
        self.ui.da.clear()
        self.ui.Cb.clear()
        self.ui.db.clear()
        self.ui.m.clear()
        self.ui.x1.clear()
        self.ui.x2.clear()
        self.ui.x3.clear()
        self.ui.x4.clear()
        self.ui.plainTextEdit_13.clear()
        self.ui.mi.clear()

class GamalWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(GamalWindow, self).__init__()
        self.ui = Ui_GamalWind()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_4)
        self.ui.pushButton_6.clicked.connect(self.btnClicked_6)
        self.ui.pushButton_7.clicked.connect(self.btnClicked_7)
        self.ui.pushButton_9.clicked.connect(self.btnClicked_9)
        self.ui.pushButton_8.clicked.connect(self.btnClicked_8)

    # генерация простых чисел
    def btnClicked(self):
        p, q = find_pq()
        self.ui.p.setPlainText(str(p))
        self.ui.q.setPlainText(str(q))

    # проверка на простоту
    def btnClicked_2(self):
        p = self.ui.p.toPlainText()
        q = self.ui.q.toPlainText()
        if not p or not q:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите простые числа!", QtWidgets.QMessageBox.Ok)
            return None
        try:
            p = int(p)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            self.ui.p.clear()
            return None
        try:
            q = int(q)
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
            self.ui.q.clear()
            return None
        if isPrime(p) == False:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число р составное!", QtWidgets.QMessageBox.Ok)
            self.ui.p.clear()
            return None
        if isPrime(q) == False:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q составное!", QtWidgets.QMessageBox.Ok)
            self.ui.q.clear()
            return None
        if isPrime(p) == True and isPrime(q) == True:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Пройдено!")
            msgBox.setText("Числа простые!")
            msgBox.exec_()
            return None

    # общий ключ
    def btnClicked_3(self):
        if self.isCorrect() == None:
            return None

    def isCorrect(self):
        p = self.ui.p.toPlainText()
        q = self.ui.q.toPlainText()
        g = self.ui.g.toPlainText()
        if q:
            try:
                q = int(q)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.q.clear()
                return None
            if isPrime(q) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q составное!", QtWidgets.QMessageBox.Ok)
                self.ui.q.clear()
                return None
        if p:
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.p.clear()
                return None
            if isPrime(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p составное!", QtWidgets.QMessageBox.Ok)
                self.ui.p.clear()
                return None
            if q:
                if int(p) != 2 * int(q) + 1:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p != 2*q+1!", QtWidgets.QMessageBox.Ok)
                    self.ui.p.clear()
                    return None
        if q and not p:
            p = 2 * q + 1
            if isPrime(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p составное! Введите другое q!", QtWidgets.QMessageBox.Ok)
                return None
            else:
                self.ui.p.setPlainText(str(p))
        if p and not q:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите сначала q!", QtWidgets.QMessageBox.Ok)
            return None
        if not p and not q:
            p, q = find_pq()
            self.ui.p.setPlainText(str(p))
            self.ui.q.setPlainText(str(q))
        if g:
            try:
                g = int(g)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.g.clear()
                return None
            if degree(g, q, p) == '1':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "g^q mod p == 1!", QtWidgets.QMessageBox.Ok)
                self.ui.g.clear()
                g = find_g(q, p)
                self.ui.g.setPlainText(str(g))
                return None
        if not g:
            g = find_g(q, p)
            self.ui.g.setPlainText(str(g))
        Xa = self.ui.Xa.toPlainText()
        Xb = self.ui.Xb.toPlainText()
        Ya = self.ui.Ya.toPlainText()
        Yb = self.ui.Yb.toPlainText()
        if Xa:
            try:
                Xa = int(Xa)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                return None
        else:
            Xa = find_X(int(p))
            self.ui.Xa.setPlainText(str(Xa))
        if Xb:
            try:
                Xb = int(Xb)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                return None
        else:
            Xb = find_X(int(p))
            self.ui.Xb.setPlainText(str(Xb))
        if Ya:
            try:
                Ya = int(Ya)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                return None
        else:
            Ya = degree(int(g), int(Xa), int(p))
            self.ui.Ya.setPlainText(Ya)
        if Yb:
            try:
                Yb = int(Yb)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                return None
        else:
            Yb = degree(int(g), int(Xb), int(p))
            self.ui.Yb.setPlainText(Yb)
        # if k:
        #     for i in k.split(' '):
        #         try:
        #             i = int(i)
        #         except Exception:
        #             QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
        #             return None
        #         if i > p-2:
        #             QtWidgets.QMessageBox.critical(self, "Ошибка", "k > p - 2!", QtWidgets.QMessageBox.Ok)
        #             k = randint(1, p - 2)
        #             self.ui.k.setPlainText(str(k))
        #             return None
        # else:
        #     #k = degree(int(Yb), int(Xa), int(p))
        #     k = randint(1, p-2)
        #     self.ui.k.setPlainText(str(k))
        # if r:
        #     for i in r.split(' '):
        #         try:
        #             i = int(i)
        #         except Exception:
        #             QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
        #             return None
        #         if i >= p:
        #             QtWidgets.QMessageBox.critical(self, "Ошибка", "r >= p!", QtWidgets.QMessageBox.Ok)
        #             self.ui.r.clear()
        #             return None
        # else:
        #     r = degree(int(g), int(k), int(p))
        #     self.ui.r.setPlainText(str(r))
        return True

#зашифровать
    def btnClicked_4(self):
        if self.isCorrect() == None:
            return None
        else:
            p = int(self.ui.p.toPlainText())
            g = int(self.ui.g.toPlainText())
            #k = int(self.ui.k.toPlainText())
            Yb = int(self.ui.Yb.toPlainText())
            m = self.ui.plainTextEdit_9.toPlainText()
            res = ''
            r1 = ''
            k1 = ''
            for i in m:
                tmp = ord(i)
                if tmp > p:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите p >" + str(tmp) + "!", QtWidgets.QMessageBox.Ok)
                    return None
                k = randint(1, p - 2) % p
                r = degree(g, k, p)
                k1+=(str(k) + ' ')
                r1 += (str(r) + ' ')
                e = (int(degree(Yb, k, p))*tmp) % p
                res+=(str(e) + ' ')
            self.ui.plainTextEdit_11.setPlainText(res)
            self.ui.k.setPlainText(k1)
            self.ui.r.setPlainText(r1)

#расшифровать
    def btnClicked_6(self):
        r = self.ui.r.toPlainText().split(' ')
        if self.isCorrect() == None:
            return None
        elif not r:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Сначала зашифруйте!", QtWidgets.QMessageBox.Ok)
            return None
        else:
            p = self.ui.p.toPlainText()
            Xb = self.ui.Xb.toPlainText()
            e = self.ui.plainTextEdit_11.toPlainText()
            e = e[:len(e) - 1].split(' ')
            res = ''
            for i in range(len(e)):
                try:
                    e[i] = int(e[i])
                except Exception:
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Расшифровывается только поток чисел через пробел!", QtWidgets.QMessageBox.Ok)
                    return None
                deg = int(degree(int(r[i]), ((int(p) - 1) - int(Xb)), (int(p))))
                m_2 = (deg * int(e[i])) % int(p)
                res += chr(m_2)
            self.ui.plainTextEdit_12.setPlainText(res)

    #зашифровать файл
    def btnClicked_7(self):
        if self.isCorrect() == None:
            return None
        else:
            p = int(self.ui.p.toPlainText())
            Yb = int(self.ui.Yb.toPlainText())
            g = int(self.ui.g.toPlainText())
            path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            if path == "":
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Откройте файл!")
                msgBox.exec_()
                return None
            file = open(path, 'rb')
            text = file.read()
            file.close()

            path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            if path == "":
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Выберите файл для выгрузки!")
                msgBox.exec_()
                return None

            file = open(path, 'w')
            k1 = ''
            r1 = ''
            for i in range(len(text)):
                k = randint(1, p - 2) % p
                r = degree(g, k, p)
                k1 += (str(k) + ' ')
                r1 += (str(r) + ' ')
                e = str((int(text[i])*int(degree(Yb, k, p))) % p) + ' '
                file.write(e)
            file.close()
            self.ui.k.setPlainText(k1)
            self.ui.r.setPlainText(r1)
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Успешно")
            msgBox.setText("Успешно выгружено!")
            msgBox.exec_()
            return None

    #расшифровать файл
    def btnClicked_9(self):
        r = self.ui.r.toPlainText()
        if self.isCorrect() == None:
            return None
        elif not r:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Сначала зашифруйте файл!", QtWidgets.QMessageBox.Ok)
            return None
        else:
            p = int(self.ui.p.toPlainText())
            r = r[:len(r) - 1].split(' ')
            Xb = int(self.ui.Xb.toPlainText())
            path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            if path == "":
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Откройте файл!")
                msgBox.exec_()
                return None
            file = open(path, 'r')
            text = file.read()
            text = text[:len(text) - 1].split(' ')
            file.close()

            path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            if path == "":
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("Выберите файл для выгрузки!")
                msgBox.exec_()
                return None

            file = open(path, 'wb')
            for i in range(len(text)):
                e = (int(text[i]) * int(degree(int(r[i]), (p - 1) - Xb,  p))) % p
                file.write(bytes([e]))
            file.close()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Успешно")
            msgBox.setText("Успешно выгружено!")
            msgBox.exec_()
            return None

    def btnClicked_8(self):
        self.ui.k.clear()
        self.ui.r.clear()
        self.ui.p.clear()
        self.ui.q.clear()
        self.ui.g.clear()
        self.ui.Ya.clear()
        self.ui.Yb.clear()
        self.ui.Xb.clear()
        self.ui.Xa.clear()
        self.ui.plainTextEdit_11.clear()
        self.ui.plainTextEdit_9.clear()
        self.ui.plainTextEdit_12.clear()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
