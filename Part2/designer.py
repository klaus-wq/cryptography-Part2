from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDesktopWidget

from window import Ui_MainWindow
import sys
from basicAlgWindow import Ui_BasicAlg
from basicAlg import gcd, exgcd, degree, amodp
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
from MD5window import Ui_MD5
from MD5 import MD5
from SHA1 import SHA1
from SHA1window import Ui_SHA1
from GOST94window import Ui_GOST94
from GOST import GOST94
from RSAPodpisWindow import Ui_RSAPodpisWind
from GamalPodpisWindow import Ui_GamalPodpisWind
from sign import find_k
from GOSTPodpisWindow import Ui_GOSTPodpisWind
from gost94Sign import find_a, find_krs, gen_PQ

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
        if self.ui.comboBox.currentText() == "MD5":
            self.ex = MD5Window()
            self.ex.show()
        if self.ui.comboBox.currentText() == "SHA-1":
            self.ex = SHA1Window()
            self.ex.show()
        if self.ui.comboBox.currentText() == "ГОСТ Р 34.11-94":
            self.ex = GOST94Window()
            self.ex.show()
        if self.ui.comboBox.currentText() == "ЭП RSA":
            self.ex = RSAPodpisWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "ЭП Эль-Гамаль":
            self.ex = GamalPodpisWindow()
            self.ex.show()
        if self.ui.comboBox.currentText() == "ЭП ГОСТ-94":
            self.ex = GOSTPodpisWindow()
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

class MD5Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(MD5Window, self).__init__()
        self.ui = Ui_MD5()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        text = self.ui.plainTextEdit.toPlainText()
        try:
            self.ui.plainTextEdit_2.setPlainText(str(MD5(text)))
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Не удалось!", QtWidgets.QMessageBox.Ok)
            return None

    def btnClicked_2(self):
        if self.ui.plainTextEdit != '':
            self.ui.plainTextEdit.clear()
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        file = open(path, 'rb')
        text = file.read()
        file.close()
        try:
            self.ui.plainTextEdit_2.setPlainText(str(MD5(text)))
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Не удалось!", QtWidgets.QMessageBox.Ok)
            return None

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()

class SHA1Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(SHA1Window, self).__init__()
        self.ui = Ui_SHA1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        text = self.ui.plainTextEdit.toPlainText()
        try:
            self.ui.plainTextEdit_2.setPlainText(str(SHA1(text)))
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Не удалось!", QtWidgets.QMessageBox.Ok)
            return None

    def btnClicked_2(self):
        if self.ui.plainTextEdit != '':
            self.ui.plainTextEdit.clear()
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        file = open(path, 'rb')
        text = file.read()
        file.close()
        try:
            self.ui.plainTextEdit_2.setPlainText(str(SHA1(text)))
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Не удалось!", QtWidgets.QMessageBox.Ok)
            return None

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_2.clear()

class GOST94Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(GOST94Window, self).__init__()
        self.ui = Ui_GOST94()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
        self.ui.pushButton_2.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked_3)

    def btnClicked(self):
        if self.ui.plainTextEdit_3.toPlainText() != '':
            vector_init = self.ui.plainTextEdit_3.toPlainText()
            for i in range(len(vector_init)):
                if vector_init[i] != 0 and vector_init[i] != 1 and len(vector_init) != 256:
                    vector_init = '00000'.zfill(256)
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Вектор инициализации из 0 и 1!", QtWidgets.QMessageBox.Ok)
                    return None
        else:
            vector_init = '00000'.zfill(256)
        text = self.ui.plainTextEdit.toPlainText()
        try:
            self.ui.plainTextEdit_2.setPlainText(str(GOST94(text, vector_init)))
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Не удалось!", QtWidgets.QMessageBox.Ok)
            return None

    def btnClicked_2(self):
        if self.ui.plainTextEdit_3.toPlainText() != '':
            vector_init = self.ui.plainTextEdit_3.toPlainText()
            for i in range(len(vector_init)):
                if vector_init[i] != 0 and vector_init[i] != 1 and len(vector_init) != 256:
                    vector_init = '00000'.zfill(256)
                    QtWidgets.QMessageBox.critical(self, "Ошибка", "Вектор инициализации из 0 и 1!", QtWidgets.QMessageBox.Ok)
        else:
            vector_init = '00000'.zfill(256)
        if self.ui.plainTextEdit.toPlainText() != '':
            self.ui.plainTextEdit.clear()
        path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
        if path == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Откройте файл!")
            msgBox.exec_()
            return ("")

        file = open(path, 'rb')
        text = file.read()
        file.close()
        try:
            self.ui.plainTextEdit_2.setPlainText(str(GOST94(text, vector_init)))
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Не удалось!", QtWidgets.QMessageBox.Ok)
            return None

    def btnClicked_3(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_3.clear()
        self.ui.plainTextEdit_2.clear()

class RSAPodpisWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(RSAPodpisWindow, self).__init__()
        self.ui = Ui_RSAPodpisWind()
        self.ui.setupUi(self)
        self.ui.genPQ.clicked.connect(self.btnClicked_PQ)
        self.ui.calcCD.clicked.connect(self.btnClicked_CD)
        self.ui.signText.clicked.connect(self.btnClicked_SignText)
        self.ui.signFile.clicked.connect(self.btnClicked_SignFile)
        self.ui.checkText.clicked.connect(self.btnClicked_checkText)
        self.ui.checkFile.clicked.connect(self.btnClicked_checkFile)
        self.ui.auto_2.clicked.connect(self.btnClicked_Auto)
        self.ui.clear.clicked.connect(self.btnClicked_Clear)

    #генерация
    def btnClicked_PQ(self):
        self.ui.label_16.setVisible(False)
        primes = generator(10**100, 10**101, 2)
        p = primes[0]
        q = primes[1]
        self.ui.p.setPlainText(str(p))
        self.ui.q.setPlainText(str(q))
        self.ui.N.setPlainText(str(p * q))
        self.ui.N1.setPlainText(str(p * q))

    #генерация ключей
    def btnClicked_CD(self):
        self.ui.label_16.setVisible(False)
        if self.isCorrect() == None:
            return None

    #подписать текст
    def btnClicked_SignText(self):
        self.ui.label_16.setVisible(False)
        if self.isCorrect() == None:
            return None
        else:
            text = self.ui.textToPodpis.toPlainText()
            d = int(self.ui.d.toPlainText())
            N = int(self.ui.N.toPlainText())
            if self.ui.comboBox.currentText() == "MD5":
                self.ui.comboBox_2.setCurrentText("MD5")
                y = MD5(text)
            if self.ui.comboBox.currentText() == "SHA-1":
                self.ui.comboBox_2.setCurrentText("SHA-1")
                y = SHA1(text)
            if self.ui.comboBox.currentText() == "ГОСТ Р 34.11-94":
                self.ui.comboBox_2.setCurrentText("ГОСТ Р 34.11-94")
                y = GOST94(text, '00000'.zfill(256))
            s = degree(int(y, 16), d, N)
            self.ui.s.setPlainText(str(s))
            self.ui.s1.setPlainText(str(s))
            self.ui.textProverka.setPlainText(text)
            if int(y, 16) > N:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("h(m) должно быть меньше N!")
                msgBox.exec_()
                return None

    #подписать файл
    def btnClicked_SignFile(self):
        self.ui.label_16.setVisible(False)
        if self.isCorrect() == None:
            return None
        else:
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

            d = int(self.ui.d.toPlainText())
            N = int(self.ui.N.toPlainText())
            if self.ui.comboBox.currentText() == "MD5":
                self.ui.comboBox_2.setCurrentText("MD5")
                y = MD5(text)
            if self.ui.comboBox.currentText() == "SHA-1":
                self.ui.comboBox_2.setCurrentText("SHA-1")
                y = SHA1(text)
            if self.ui.comboBox.currentText() == "ГОСТ Р 34.11-94":
                self.ui.comboBox_2.setCurrentText("ГОСТ Р 34.11-94")
                y = GOST94(text, '00000'.zfill(256))
            s = degree(int(y, 16), d, N)
            self.ui.s.setPlainText(str(s))
            self.ui.s1.setPlainText(str(s))
            if int(y, 16) > N:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("h(m) должно быть меньше N!")
                msgBox.exec_()
                return None

            # path = QFileDialog.getOpenFileName(parent=None, caption='Выберите файл')[0]
            # if path == "":
            #     msgBox = QtWidgets.QMessageBox()
            #     msgBox.setWindowTitle("Ошибка")
            #     msgBox.setText("Откройте файл!")
            #     msgBox.exec_()
            #     return None
            # file = open(path, 'wb')
            # file.write(text)
            # for i in s:
            #     file.write(bytes([int(i)]))
            # file.close()
            # msgBox = QtWidgets.QMessageBox()
            # msgBox.setWindowTitle("Успешно")
            # msgBox.setText("Успешно выгружено!")
            # msgBox.exec_()
            # return ("")

    #проверить текст
    def btnClicked_checkText(self):
        self.ui.label_16.setVisible(False)
        e1 = int(self.ui.e1.toPlainText())
        N1 = int(self.ui.N1.toPlainText())
        s1 = int(self.ui.s1.toPlainText())
        text = self.ui.textProverka.toPlainText()

        try:
            if self.ui.comboBox_2.currentText() == "MD5":
                y = MD5(text)
            if self.ui.comboBox_2.currentText() == "SHA-1":
                y = SHA1(text)
            if self.ui.comboBox_2.currentText() == "ГОСТ Р 34.11-94":
                y = GOST94(text, '00000'.zfill(256))
            yInt = str(int(y, 16) % N1)
            w = degree(s1, e1, N1)
            if w == yInt:
                self.ui.resVerification.setPlainText('Верно')
                # self.ui.label_16.setVisible(True)
                # path = 'tree.gif'
                # gif = QtGui.QMovie(path)
                # self.ui.label_16.setMovie(gif)
                # gif.start()
            else:
                self.ui.resVerification.setPlainText('Неверно')
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Проверка не удалась!", QtWidgets.QMessageBox.Ok)
            return None

    #проверить файл
    def btnClicked_checkFile(self):
        self.ui.label_16.setVisible(False)
        e1 = int(self.ui.e1.toPlainText())
        N1 = int(self.ui.N1.toPlainText())
        s1 = int(self.ui.s1.toPlainText())
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

        try:
            if self.ui.comboBox_2.currentText() == "MD5":
                y = MD5(text)
            if self.ui.comboBox_2.currentText() == "SHA-1":
                y = SHA1(text)
            if self.ui.comboBox_2.currentText() == "ГОСТ Р 34.11-94":
                y = GOST94(text, '00000'.zfill(256))
            yInt = str(int(y, 16) % N1)
            w = degree(s1, e1, N1)
            if w == yInt:
                self.ui.resVerification.setPlainText('Верно')
                # self.ui.label_16.setVisible(True)
                # path = 'tree.gif'
                # gif = QtGui.QMovie(path)
                # self.ui.label_16.setMovie(gif)
                # gif.start()
            else:
                self.ui.resVerification.setPlainText('Неверно')
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Проверка не удалась!", QtWidgets.QMessageBox.Ok)
            return None

    #автозаполнение
    def btnClicked_Auto(self):
        self.ui.e1.setPlainText(self.ui.e.toPlainText())
        self.ui.N1.setPlainText(self.ui.N.toPlainText())
        self.ui.s1.setPlainText(self.ui.s.toPlainText())
        if self.ui.comboBox.currentText() == "MD5":
            self.ui.comboBox_2.setCurrentText("MD5")
        if self.ui.comboBox.currentText() == "SHA-1":
            self.ui.comboBox_2.setCurrentText("SHA-1")
        if self.ui.comboBox.currentText() == "ГОСТ Р 34.11-94":
            self.ui.comboBox_2.setCurrentText("ГОСТ Р 34.11-94")

    #очистить
    def btnClicked_Clear(self):
        self.ui.label_16.setVisible(False)
        self.ui.p.clear()
        self.ui.q.clear()
        self.ui.N.clear()
        self.ui.s.clear()
        self.ui.e.clear()
        self.ui.N1.clear()
        self.ui.e1.clear()
        self.ui.s1.clear()
        self.ui.textProverka.clear()
        self.ui.resVerification.clear()
        self.ui.d.clear()
        self.ui.textToPodpis.clear()

    def isCorrect(self):
        p = self.ui.p.toPlainText()
        q = self.ui.q.toPlainText()
        e = self.ui.e.toPlainText()
        if p:
            try:
                p = int(p)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число p!", QtWidgets.QMessageBox.Ok)
                self.ui.p.clear()
                return None
            if isPrime(p) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число р составное!", QtWidgets.QMessageBox.Ok)
                self.ui.p.clear()
                return None
        if q:
            try:
                q = int(q)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число q!", QtWidgets.QMessageBox.Ok)
                self.ui.q.clear()
                return None
            if isPrime(q) == False:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q составное!", QtWidgets.QMessageBox.Ok)
                self.ui.q.clear()
                return None
        if (p == q) and (p != '') and (q != ''):
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Число p == q!", QtWidgets.QMessageBox.Ok)
            self.ui.p.clear()
            self.ui.q.clear()
            return None
        if not p and not q:
            primes = generator(10**100, 10**101, 2)
            p = primes[0]
            q = primes[1]
            self.ui.p.setPlainText(str(p))
            self.ui.q.setPlainText(str(q))
            self.ui.N.setPlainText(str(p * q))
            self.ui.N1.setPlainText(str(p * q))
        elif not p:
            p = generator(10**100, 10**101, 1)[0]
            self.ui.p.setPlainText(str(p))
            self.ui.N.setPlainText(str(p * q))
            self.ui.N1.setPlainText(str(p * q))
        elif not q:
            q = generator(10**100, 10**101, 1)[0]
            self.ui.q.setPlainText(str(q))
            self.ui.N.setPlainText(str(p * q))
            self.ui.N1.setPlainText(str(p * q))
        if e:
            try:
                e = int(e)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Сгенерируете число в качестве открытого ключа!", QtWidgets.QMessageBox.Ok)
                self.ui.e.clear()
                return None
        if e:
            if e >= (p-1)*(q-1):
                QtWidgets.QMessageBox.critical(self, "Ошибка", "e > (p-1)*(q-1)!", QtWidgets.QMessageBox.Ok)
                self.ui.e.clear()
                e = find_e(p, q)
                self.ui.e.setPlainText(str(e))
                self.ui.e1.setPlainText(str(e))
                d = find_d(e, p, q)
                self.ui.d.setPlainText(str(d))
                self.ui.N.setPlainText(str(p * q))
                self.ui.N1.setPlainText(str(p * q))
                return None
            if gcd(e, (p-1)*(q-1)) != '1' and (gcd(e, p-1) == gcd(e, q-1)) != '1' and exgcd(e, (p-1)*(q-1)) == 'Обратный элемент не существует!':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите другое е!", QtWidgets.QMessageBox.Ok)
                self.ui.e.clear()
                e = find_e(p, q)
                self.ui.e.setPlainText(str(e))
                self.ui.e1.setPlainText(str(e))
                d = find_d(e, p, q)
                self.ui.d.setPlainText(str(d))
                self.ui.N.setPlainText(str(p * q))
                self.ui.N1.setPlainText(str(p * q))
                return None
            else:
                d = find_d(e, p, q)
                self.ui.d.setPlainText(str(d))
                self.ui.N.setPlainText(str(p * q))
                self.ui.N1.setPlainText(str(p * q))
        if not e:
            e = find_e(p, q)
            d = find_d(e, p, q)
            self.ui.e.setPlainText(str(e))
            self.ui.e1.setPlainText(str(e))
            self.ui.d.setPlainText(str(d))
            self.ui.N.setPlainText(str(p*q))
            self.ui.N1.setPlainText(str(p*q))
        return True

class GamalPodpisWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(GamalPodpisWindow, self).__init__()
        self.ui = Ui_GamalPodpisWind()
        self.ui.setupUi(self)
        self.ui.genPQ.clicked.connect(self.btnClicked_PQ)
        self.ui.calcCD.clicked.connect(self.btnClicked_CD)
        self.ui.signText.clicked.connect(self.btnClicked_SignText)
        self.ui.signFile.clicked.connect(self.btnClicked_SignFile)
        self.ui.checkText.clicked.connect(self.btnClicked_checkText)
        self.ui.checkFile.clicked.connect(self.btnClicked_checkFile)
        self.ui.auto_2.clicked.connect(self.btnClicked_Auto)
        self.ui.clear.clicked.connect(self.btnClicked_Clear)

    # генерация простых чисел
    def btnClicked_PQ(self):
        self.ui.label_19.setVisible(False)
        p, q = find_pq()
        self.ui.p.setPlainText(str(p))
        self.ui.p1.setPlainText(str(p))
        self.ui.q.setPlainText(str(q))

    #генерация параметров
    def btnClicked_CD(self):
        self.ui.label_19.setVisible(False)
        if self.isCorrect() == None:
            return None

    #подписать текст
    def btnClicked_SignText(self):
        self.ui.label_19.setVisible(False)
        if self.isCorrect() == None:
            return None
        else:
            text = self.ui.textToPodpis.toPlainText()
            p = int(self.ui.p.toPlainText())
            g = int(self.ui.g.toPlainText())
            Xa = int(self.ui.Xa.toPlainText())
            k = int(self.ui.k.toPlainText())
            if self.ui.comboBox.currentText() == "MD5":
                self.ui.comboBox_2.setCurrentText("MD5")
                y = MD5(text)
            if self.ui.comboBox.currentText() == "SHA-1":
                self.ui.comboBox_2.setCurrentText("SHA-1")
                y = SHA1(text)
            if self.ui.comboBox.currentText() == "ГОСТ Р 34.11-94":
                self.ui.comboBox_2.setCurrentText("ГОСТ Р 34.11-94")
                y = GOST94(text, '00000'.zfill(256))
            yInt = int(y, 16)
            r = int(degree(g, k, p))
            u = (yInt - Xa * r) % (p - 1)
            s = int(exgcd(k, p - 1)) * u % (p - 1)
            self.ui.s.setPlainText(str(s))
            self.ui.s1.setPlainText(str(s))
            self.ui.r.setPlainText(str(r))
            self.ui.r1.setPlainText(str(r))
            self.ui.textProverka.setPlainText(text)
            if yInt > p:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("h(m) должно быть меньше p!")
                msgBox.exec_()
                return None

    # подписать файл
    def btnClicked_SignFile(self):
        self.ui.label_19.setVisible(False)
        if self.isCorrect() == None:
            return None
        else:
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

            p = int(self.ui.p.toPlainText())
            Xa = int(self.ui.Xa.toPlainText())
            k = int(self.ui.k.toPlainText())
            g = int(self.ui.g.toPlainText())
            if self.ui.comboBox.currentText() == "MD5":
                self.ui.comboBox_2.setCurrentText("MD5")
                y = MD5(text)
            if self.ui.comboBox.currentText() == "SHA-1":
                self.ui.comboBox_2.setCurrentText("SHA-1")
                y = SHA1(text)
            if self.ui.comboBox.currentText() == "ГОСТ Р 34.11-94":
                self.ui.comboBox_2.setCurrentText("ГОСТ Р 34.11-94")
                y = GOST94(text, '00000'.zfill(256))
            yInt = int(y, 16)
            r = int(degree(g, k, p))
            u = (yInt - Xa * r) % (p - 1)
            s = int(exgcd(k, p - 1)) * u % (p - 1)
            self.ui.s.setPlainText(str(s))
            self.ui.s1.setPlainText(str(s))
            self.ui.r.setPlainText(str(r))
            self.ui.r1.setPlainText(str(r))
            if yInt > p:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setWindowTitle("Ошибка")
                msgBox.setText("h(m) должно быть меньше p!")
                msgBox.exec_()

    # проверить текст
    def btnClicked_checkText(self):
        self.ui.label_19.setVisible(False)
        p1 = int(self.ui.p1.toPlainText())
        g1 = int(self.ui.g1.toPlainText())
        s1 = int(self.ui.s1.toPlainText())
        r1 = int(self.ui.r1.toPlainText())
        Ya1 = int(self.ui.Ya1.toPlainText())
        text = self.ui.textProverka.toPlainText()
        try:
            if self.ui.comboBox_2.currentText() == "MD5":
                y = MD5(text)
            if self.ui.comboBox_2.currentText() == "SHA-1":
                y = SHA1(text)
            if self.ui.comboBox_2.currentText() == "ГОСТ Р 34.11-94":
                y = GOST94(text, '00000'.zfill(256))
            yInt = int(y, 16)
            left = (int(degree(Ya1, r1, p1)) * int(degree(r1, s1, p1))) % p1
            right = int(degree(g1, yInt, p1))
            if left == right:
                self.ui.resVerification.setPlainText('Верно')
                # path = 'tree1.gif'
                # gif = QtGui.QMovie(path)
                # self.ui.label_19.setMovie(gif)
                # gif.start()
            else:
                self.ui.resVerification.setPlainText('Неверно')
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Проверка не удалась!", QtWidgets.QMessageBox.Ok)
            return None

    # проверить файл
    def btnClicked_checkFile(self):
        self.ui.label_19.setVisible(False)
        p1 = int(self.ui.p1.toPlainText())
        g1 = int(self.ui.g1.toPlainText())
        s1 = int(self.ui.s1.toPlainText())
        r1 = int(self.ui.r1.toPlainText())
        Ya1 = int(self.ui.Ya1.toPlainText())
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
        try:
            if self.ui.comboBox_2.currentText() == "MD5":
                y = MD5(text)
            if self.ui.comboBox_2.currentText() == "SHA-1":
                y = SHA1(text)
            if self.ui.comboBox_2.currentText() == "ГОСТ Р 34.11-94":
                y = GOST94(text, '00000'.zfill(256))
            yInt = int(y, 16)
            left = (int(degree(Ya1, r1, p1)) * int(degree(r1, s1, p1))) % p1
            right = int(degree(g1, yInt, p1))
            if left == right:
                self.ui.resVerification.setPlainText('Верно')
                # path = 'tree1.gif'
                # gif = QtGui.QMovie(path)
                # self.ui.label_19.setMovie(gif)
                # gif.start()
            else:
                self.ui.resVerification.setPlainText('Неверно')
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Проверка не удалась!", QtWidgets.QMessageBox.Ok)
            return None

    # автозаполнение
    def btnClicked_Auto(self):
        self.ui.label_19.setVisible(False)
        self.ui.p1.setPlainText(self.ui.p.toPlainText())
        self.ui.g1.setPlainText(self.ui.g.toPlainText())
        self.ui.s1.setPlainText(self.ui.s.toPlainText())
        self.ui.r1.setPlainText(self.ui.r.toPlainText())
        if self.ui.comboBox.currentText() == "MD5":
            self.ui.comboBox_2.setCurrentText("MD5")
        if self.ui.comboBox.currentText() == "SHA-1":
            self.ui.comboBox_2.setCurrentText("SHA-1")
        if self.ui.comboBox.currentText() == "ГОСТ Р 34.11-94":
            self.ui.comboBox_2.setCurrentText("ГОСТ Р 34.11-94")

    # очистить
    def btnClicked_Clear(self):
        self.ui.label_19.setVisible(False)
        self.ui.p.clear()
        self.ui.q.clear()
        self.ui.g.clear()
        self.ui.s.clear()
        self.ui.s1.clear()
        self.ui.k.clear()
        self.ui.r.clear()
        self.ui.r1.clear()
        self.ui.Xa.clear()
        self.ui.Ya.clear()
        self.ui.p1.clear()
        self.ui.g1.clear()
        self.ui.Ya1.clear()
        self.ui.textProverka.clear()
        self.ui.resVerification.clear()
        self.ui.textToPodpis.clear()

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
                self.ui.p1.setObjectName(str(p))
        if p and not q:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите сначала q!", QtWidgets.QMessageBox.Ok)
            return None
        if not p and not q:
            p, q = find_pq()
            self.ui.p.setPlainText(str(p))
            self.ui.p1.setPlainText(str(p))
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
                self.ui.g1.setPlainText(str(g))
                return None
        if not g:
            g = find_g(q, p)
            self.ui.g.setPlainText(str(g))
            self.ui.g1.setPlainText(str(g))
        Xa = self.ui.Xa.toPlainText()
        Ya = self.ui.Ya.toPlainText()
        if Xa:
            try:
                Xa = int(Xa)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.Xa.clear()
                return None
        else:
            Xa = find_X(int(p))
            self.ui.Xa.setPlainText(str(Xa))
        if Ya:
            try:
                Ya = int(Ya)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.Ya.clear()
                return None
        else:
            Ya = degree(int(g), int(Xa), int(p))
            self.ui.Ya.setPlainText(Ya)
            self.ui.Ya1.setPlainText(Ya)
        if Xa and not Ya:
            try:
                Xa = int(Xa)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.Ya.clear()
                return None
            Ya = degree(int(g), int(Xa), int(p))
            self.ui.Ya.setPlainText(Ya)
            self.ui.Ya1.setPlainText(Ya)
        k = self.ui.k.toPlainText()
        if k:
            try:
                k = int(k)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.k.clear()
                return None
            if int(k) > int(p) - 1:
                k = int(k) % (int(p)-1)
                self.ui.k.setPlainText(str(k))
            if gcd(int(k), int(p)-1) != '1':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "k должно быть взаимнопростым с p - 1!", QtWidgets.QMessageBox.Ok)
                self.ui.k.clear()
                return None
        else:
            k = find_k(p)
            self.ui.k.setPlainText(str(k))
        return True

class GOSTPodpisWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(GOSTPodpisWindow, self).__init__()
        self.ui = Ui_GOSTPodpisWind()
        self.ui.setupUi(self)
        self.ui.genPQ.clicked.connect(self.btnClicked_PQ)
        self.ui.genPQ.clicked.connect(self.btnClicked_PQ)
        self.ui.calcCD.clicked.connect(self.btnClicked_CD)
        self.ui.signText.clicked.connect(self.btnClicked_SignText)
        self.ui.signFile.clicked.connect(self.btnClicked_SignFile)
        self.ui.checkText.clicked.connect(self.btnClicked_checkText)
        self.ui.checkFile.clicked.connect(self.btnClicked_checkFile)
        self.ui.auto_2.clicked.connect(self.btnClicked_Auto)
        self.ui.clear.clicked.connect(self.btnClicked_Clear)

    #генерация !!неверно
    def btnClicked_PQ(self):
        p, q = gen_PQ()
        self.ui.p.setPlainText(str(p))
        self.ui.q.setPlainText(str(q))
        self.ui.p1.setPlainText(str(p))
        self.ui.q1.setPlainText(str(q))

    #генерация параметров
    def btnClicked_CD(self):
        if self.isCorrect() == None:
            return None

    #подписать текст
    def btnClicked_SignText(self):
        if self.isCorrect() == None:
            return None
        else:
            text = self.ui.textToPodpis.toPlainText()
            p = int(self.ui.p.toPlainText())
            q = int(self.ui.q.toPlainText())
            a = int(self.ui.a.toPlainText())
            Xa = int(self.ui.Xa.toPlainText())
            y = GOST94(text, '00000'.zfill(256))
            yInt = int(y, 16) % q
            k, r, s = find_krs(a, p, q, yInt, Xa)
            self.ui.s.setPlainText(str(s))
            self.ui.s1.setPlainText(str(s))
            self.ui.r.setPlainText(str(r))
            self.ui.r1.setPlainText(str(r))
            self.ui.k.setPlainText(str(k))
            self.ui.textProverka.setPlainText(text)
            # if yInt > q:
            #     msgBox = QtWidgets.QMessageBox()
            #     msgBox.setWindowTitle("Ошибка")
            #     msgBox.setText("h(m) должно быть меньше q!")
            #     msgBox.exec_()
            #     return None

    # подписать файл
    def btnClicked_SignFile(self):
        if self.isCorrect() == None:
            return None
        else:
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

            p = int(self.ui.p.toPlainText())
            Xa = int(self.ui.Xa.toPlainText())
            q = int(self.ui.q.toPlainText())
            a = int(self.ui.a.toPlainText())
            y = GOST94(text, '00000'.zfill(256))
            yInt = int(y, 16) % q
            k, r, s = find_krs(a, p, q, yInt, Xa)
            self.ui.s.setPlainText(str(s))
            self.ui.s1.setPlainText(str(s))
            self.ui.r.setPlainText(str(r))
            self.ui.r1.setPlainText(str(r))
            self.ui.k.setPlainText(str(k))
            # if yInt > q:
            #     msgBox = QtWidgets.QMessageBox()
            #     msgBox.setWindowTitle("Ошибка")
            #     msgBox.setText("h(m) должно быть меньше q!")
            #     msgBox.exec_()
            #     return None

    # проверить текст
    def btnClicked_checkText(self):
        p1 = int(self.ui.p1.toPlainText())
        q1 = int(self.ui.q1.toPlainText())
        a1 = int(self.ui.a1.toPlainText())
        s1 = int(self.ui.s1.toPlainText())
        r1 = int(self.ui.r1.toPlainText())
        Ya1 = int(self.ui.Ya1.toPlainText())
        text = self.ui.textProverka.toPlainText()
        try:
            y = GOST94(text, '00000'.zfill(256))
            yInt = int(y, 16)
            if r1 <= 0 or r1 >= q1:
                self.ui.resVerification.setPlainText('Подпись недействительна (0 < r < q)')
            if s1 <= 0 or s1 >= q1:
                self.ui.resVerification.setPlainText('Подпись недействительна (0 < s < q)')
            yIntInv = int(exgcd(yInt, q1))
            w = int(degree(yInt, q1 - 2, q1))
            #u1 = (s1 * yIntInv) % q1
            u1 = (s1*w) % q1
            #u2 = (((-r1 * yIntInv) % q1) + q1) % q1
            u2 = ((q1 - r1)*w) % q1
            v = ((int(degree(a1, u1, p1)) * int(degree(Ya1, u2, p1))) % p1) % q1
            if v == r1:
                self.ui.resVerification.setPlainText('Верно')
            else:
                self.ui.resVerification.setPlainText('Неверно')
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Проверка не удалась!", QtWidgets.QMessageBox.Ok)
            return None

    # проверить файл
    def btnClicked_checkFile(self):
        p1 = int(self.ui.p1.toPlainText())
        q1 = int(self.ui.q1.toPlainText())
        a1 = int(self.ui.a1.toPlainText())
        s1 = int(self.ui.s1.toPlainText())
        r1 = int(self.ui.r1.toPlainText())
        Ya1 = int(self.ui.Ya1.toPlainText())
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
        try:
            y = GOST94(text, '00000'.zfill(256))
            yInt = int(y, 16)
            if r1 <= 0 or r1 >= q1:
                self.ui.resVerification.setPlainText('Подпись недействительна (0 < r < q)')
            if s1 <= 0 or s1 >= q1:
                self.ui.resVerification.setPlainText('Подпись недействительна (0 < s < q)')
            yIntInv = int(exgcd(yInt, q1))
            w = int(degree(yInt, q1 - 2, q1))
            #u1 = (s1 * yIntInv) % q1
            u1 = (s1*w) % q1
            #u2 = (((-r1 * yIntInv) % q1) + q1) % q1
            u2 = ((q1 - r1)*w) % q1
            v = ((int(degree(a1, u1, p1)) * int(degree(Ya1, u2, p1))) % p1) % q1
            if v == r1:
                self.ui.resVerification.setPlainText('Верно')
            else:
                self.ui.resVerification.setPlainText('Неверно')
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Проверка не удалась!", QtWidgets.QMessageBox.Ok)
            return None

    # автозаполнение
    def btnClicked_Auto(self):
        self.ui.p1.setPlainText(self.ui.p.toPlainText())
        self.ui.q1.setPlainText(self.ui.q.toPlainText())
        self.ui.a1.setPlainText(self.ui.a.toPlainText())
        self.ui.Ya1.setPlainText(self.ui.Ya.toPlainText())
        self.ui.s1.setPlainText(self.ui.s.toPlainText())
        self.ui.r1.setPlainText(self.ui.r.toPlainText())

    # очистить
    def btnClicked_Clear(self):
        self.ui.p.clear()
        self.ui.q.clear()
        self.ui.a.clear()
        self.ui.s.clear()
        self.ui.s1.clear()
        self.ui.k.clear()
        self.ui.r.clear()
        self.ui.r1.clear()
        self.ui.Xa.clear()
        self.ui.Ya.clear()
        self.ui.p1.clear()
        self.ui.a1.clear()
        self.ui.q1.clear()
        self.ui.Ya1.clear()
        self.ui.textProverka.clear()
        self.ui.resVerification.clear()
        self.ui.textToPodpis.clear()

    def isCorrect(self):
        p = self.ui.p.toPlainText()
        q = self.ui.q.toPlainText()
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
            if len(bin(q)[2:]) <= 254 or len(bin(q)[2:]) >= 256:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q должно быть 2**254 < q < 2**256!", QtWidgets.QMessageBox.Ok)
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
            if len(bin(int(p))[2:]) <= 509 or len(bin(int(p))[2:]) >= 512:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q должно быть 2**509 < p < 2**512!", QtWidgets.QMessageBox.Ok)
                self.ui.p.clear()
                return None
        if p and q:
            if (int(p) - 1) % int(q) != 0:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число q должно делителем p - 1!", QtWidgets.QMessageBox.Ok)
                self.ui.q.clear()
                return None
        if not p and not q:
            p, q = gen_PQ()
            self.ui.p.setPlainText(str(p))
            self.ui.p1.setPlainText(str(p))
            self.ui.q.setPlainText(str(q))
            self.ui.q1.setPlainText(str(q))
        a = self.ui.a.toPlainText()
        if a:
            try:
                a = int(a)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.a.clear()
                return None
            if int(a) <= 1 or int(a) >= int(p) - 1:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Число а должно быть 1 < a < p - 1!", QtWidgets.QMessageBox.Ok)
                self.ui.a.clear()
                return None
            if degree(int(a), int(q), int(p)) != '1':
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите другое а!", QtWidgets.QMessageBox.Ok)
                self.ui.a.clear()
                return None
            else:
                self.ui.a1.setPlainText(str(a))
        if not a:
            a = find_a(int(p), int(q))
            self.ui.a.setPlainText(str(a))
            self.ui.a1.setPlainText(str(a))
        Xa = self.ui.Xa.toPlainText()
        Ya = self.ui.Ya.toPlainText()
        if Xa:
            try:
                Xa = int(Xa)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.Xa.clear()
                return None
        else:
            Xa = randint(1, int(q) - 1)
            self.ui.Xa.setPlainText(str(Xa))
        if Ya:
            try:
                Ya = int(Ya)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.Ya.clear()
                return None
        else:
            Ya = degree(a, int(Xa), int(p))
            self.ui.Ya.setPlainText(Ya)
            self.ui.Ya1.setPlainText(Ya)
        if Xa and not Ya:
            try:
                Xa = int(Xa)
            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка", "Введите число!", QtWidgets.QMessageBox.Ok)
                self.ui.Ya.clear()
                return None
            Ya = degree(a, int(Xa), int(p))
            self.ui.Ya.setPlainText(Ya)
            self.ui.Ya1.setPlainText(Ya)
        return True

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())