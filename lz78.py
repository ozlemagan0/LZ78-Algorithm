import sys
import typing
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QPlainTextEdit


class Lz78Code:
    def __init__(self, i, c):
        self.i = i
        self.c = c

    def __str__(self) -> str:
        return f"<{self.i}, '{self.c}'>"


def encode(input_str: str) -> typing.List[Lz78Code]:
    ret = []
    prev_sub = ""
    sub_dict = {"": 0}
    for c in input_str:
        next_sub = prev_sub + c
        if next_sub not in sub_dict:
            i = sub_dict[prev_sub]
            output = Lz78Code(i, c)
            sub_dict[next_sub] = len(sub_dict)
            print(f"'{next_sub}'\t{str(output)}\t{len(sub_dict) - 1}")
            ret.append(f"'{next_sub}'\t{str(output)}\t{len(sub_dict) - 1}")
            prev_sub = ""
        else:
            prev_sub = next_sub
    return ret


def decode(input_ar: typing.List[Lz78Code]) -> str:
    ret = ""
    sub_dict = [""]
    for output in input_ar:
        entry = sub_dict[output.i] + output.c
        sub_dict.append(entry)
        ret += entry
    return ret


class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.addProperties()
        self.addProperties1()
        self.buton.clicked.connect(self.click)

    def addProperties(self):
        self.resize(400, 400)
        self.move(700, 100)
        self.setWindowTitle('LZ78 Algorithm')

    def addProperties1(self):
        self.label = QLabel("Enter Characters", self)
        self.label.setGeometry(100, 5, 200, 75)

        self.input = QLineEdit(self)
        self.input.setGeometry(100, 60, 200, 25)

        self.buton = QPushButton("Run", self)
        self.buton.setGeometry(100, 100, 200, 25)

        self.label = QLabel("Result:", self)
        self.label.setGeometry(100, 120, 200, 75)

        self.label = QPlainTextEdit(self)
        self.label.setGeometry(75, 170, 250, 190)

    def click(self):
        result = ""
        for i in encode(self.input.text()):
            result += f" {i} \n"
        self.label.clear()
        self.label.insertPlainText(result)


app = QApplication(sys.argv)
form = Windows()
form.show()
sys.exit(app.exec_())