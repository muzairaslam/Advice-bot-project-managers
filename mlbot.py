import sys
import openai
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import(
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QTextEdit
)

API_KEY = "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"

openai.api_key = API_KEY


class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()  

    # Method for widgets, label, textbox
    def init_ui(self):
        self.logo_label = QLabel()
        self.logo_pixmap = QPixmap('robot.jpg').scaled(150, 150)
        self.logo_label.setPixmap(self.logo_pixmap)
        self.input_label = QLabel("Ask a question:")
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type here ...")
        self.answer_label = QLabel("Answer: ")
        self.answer_field = QTextEdit()
        self.submit_button = QPushButton("Submit")
        self.popular_questions_group = QGroupBox("Popular Question")
        self.popular_questions_layout = QVBoxLayout()
        self.popular_questions = ["What is the current status of Marketing Project?",
                                  "What are the top priority tasks for this week?",
                                  "Can you generate a report on project progress for our stakeholders?"]
        self.question_buttons = []

        # create a layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        # Add logo
        layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)

        # Add input field
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.submit_button)
        layout.addLayout(input_layout)

        # Add answer field
        layout.addWidget(self.answer_label)
        layout.addWidget(self.answer_field)

        # Add popular question buttons
        for question in self.popular_questions:
            button = QPushButton(question)
            '''
            button.styleSheet(
                """
                QPushButton {
                background-color: #FFFFFF
                border: 2px solid #00AEFF
                }
                """
            )
            '''
            button.clicked.connect(lambda _, q = question: self.input_field.setText(q))
            self.popular_questions_layout.addWidget(button)
            self.question_buttons.append(button)
        self.popular_questions_group.setLayout(self.popular_questions_layout)
        layout.addWidget(self.popular_questions_group)


        # Set the layout
        self.setLayout(layout)    

        # Set window properties
        self.setWindowTitle("Project Managment Assistant Bot")
        self.setGeometry(200, 200, 600, 600)

        # connect the submit button to the function which queries Open AI's API
        self.submit_button.clicked.connect(self.get_answer)

    # method to get answer
    def get_answer(self):
        question = self.input_field.text()
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "You are an expert project manager with twenty years of experience. Answer the following questions in a concise way or in bullet points"}, # project manager role definition
                {"role": "user", "content": f'{question}'}, # question from our application
                ],
            max_tokens = 1024,
            n = 1, 
            stop = None,
            temperature = 0.7
        )
        # get the answer
        answer = response.choices[0].message.content # Get the text of the first choice
        self.answer_field.setText(answer)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())





'''
API_KEY = "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"

openai.api_key = API_KEY

response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "You are an expert project manager with twenty years of experience. Answer the following questions in a concise way or in bullet points"}, # project manager role definition
    {"role": "user", "content": "Plan a project for a time frame of 20 days in event management"}, # question from our application
  ]
)

# get the answer
answer = response.choices[0].message.content # Get the text of the first choice

print(answer)

'''