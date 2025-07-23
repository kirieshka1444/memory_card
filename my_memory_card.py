
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup, QMessageBox)
from PyQt5 import QtGui
from random import shuffle, randint

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = [Question('Cколько всего частей игры STALKER', '4', '2', '3', '5'),
               Question('Кто появляется в каждой части STALKER', 'Шустрый', 'Шрам', 'Волкодав', 'Сидорович'),
               Question('Какой самый дешёвый артефакт в STALKER Тень чернобыля', 'Медуза', 'Каменный цветок', 'Мамины бусы', 'Пламя'),
               Question('Сколько всего уникальных оружий в STALKER Чистое небо', '26', '27', '33', '19'),
               Question('Самый лучший артефакт в STALKER Зов припяти', 'Пузырь', 'Медуза', 'Компас', 'Колобок')]
               

app = QApplication([])
window = QWidget()
window.setWindowTitle('Тест на знание игры STALKER')

btn_OK = QPushButton('Ответить')
lb_question = QLabel('Сколько будет 2+2')


Radiogroupbox = QGroupBox('Варианты ответов')

rbtn1 = QRadioButton('4')
rbtn2 = QRadioButton('5')
rbtn3 = QRadioButton('2')
rbtn4 = QRadioButton('1')

Radiogroup = QButtonGroup()
Radiogroup.addButton(rbtn1)
Radiogroup.addButton(rbtn2)
Radiogroup.addButton(rbtn3)
Radiogroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

Radiogroupbox.setLayout(layout_ans1)

Ansgroupbox = QGroupBox('Результаты теста')
lb_result = QLabel('Правильно/Неправильно')
lb_corect = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_corect, alignment = Qt.AlignCenter)
Ansgroupbox.setLayout(layout_res)


layout_card = QVBoxLayout()
layout_card.addWidget(lb_question, alignment = Qt.AlignCenter)
layout_card.addWidget(Radiogroupbox)
layout_card.addWidget(Ansgroupbox)
layout_card.addWidget(btn_OK, alignment = Qt.AlignCenter)
Radiogroupbox.hide()

window.setLayout(layout_card)



def show_result():
    Radiogroupbox.hide()
    Ansgroupbox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    Radiogroupbox.show()
    Ansgroupbox.hide()
    btn_OK.setText('Ответить') 
    Radiogroup.setExclusive(False) 
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    Radiogroup.setExclusive(True)


def test():
    if btn_OK.text() == "Ответить":
        show_result()
    else:
        show_question()

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_corect.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Малодчык!')
        window.score += 1
        window.mcgBox.setText(f'Статистика:\n  Всего вопросов {window.total} \n  правильных ответов: {window.score}')
        window.mcgBox.exec()
        print(f'Статистика:\n  Всего вопросов {window.total} \n  правильных ответов: {window.score}')
        print(f'  Рейтинг: {round(window.score / window.total, 2) * 100}%')
    else:
        if answers[1].isChecked or answers[2].isChecked or answers[3].isChecked():
            show_correct('Как же так!')
            window.mcgBox.setText(f'Статистика:\n  Всего вопросов {window.total} \n  правильных ответов: {window.score}')
            window.mcgBox.exec()
            print(f'Статистика:\n  Всего вопросов {window.total} \n  правильных ответов: {window.score}')
            print(f'  Рейтинг: {round(window.score / window.total, 2) * 100}%') 

def next_question():
    window.total += 1
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)
    

def klick_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.total = 0
window.score = 0

window.mcgBox = QMessageBox()
window.mcgBox.setIcon(QMessageBox.Information)
window.mcgBox.setText(f'Статистика:\n  Всего вопросов {window.total} \n  правильных ответов: {window.score}')
window.mcgBox.setWindowTitle('Тест на знание игры STALKER')
window.mcgBox.setStandardButtons(QMessageBox.Ok)


btn_OK.clicked.connect(klick_ok)



window.cur_question = -1
window.resize(400, 300)
next_question()
window.show()
app.exec()