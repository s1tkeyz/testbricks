import json

TB_CORE_VERSION = '1.0'


# Classes
class Question:
    text = ''
    answer = ''
    value = 0

    def __init__(self, _text, _answer, _value):
        self.text = _text
        self.answer = _answer
        self.value = _value

    # Utility functions
    def to_list(self):
        return [self.text, self.answer, self.value]

    def to_dict(self):
        return {
            'text': self.text,
            'answer': self.answer,
            'value': self.value,
        }


class Test:
    name = ''
    subject = ''
    author = ''
    questions = []
    allotted_time = 0

    # Constructor
    def __init__(self, _name, _subject, _author, _questions, _allotted_time):
        self.name = _name
        self.subject = _subject
        self.author = _author
        self.questions = _questions
        self.allotted_time = _allotted_time

    # Utility functions
    def to_list(self):
        return [question for question in self.questions]

    def to_dict(self):
        return {
            'name': self.name,
            'subject': self.subject,
            'author': self.author,
            'allotted_time': self.allotted_time,
            'questions': self.questions,
        }

    # IO operations
    def save_to_file(self, _path):
        file = open(_path, 'w')
        json.dump(self.to_dict(), file, indent=4)


# Functions
def get_test_from_file(_path):
    file_data = json.load(open(_path, 'r'))
    name = file_data['name']
    subject = file_data['subject']
    author = file_data['author']
    allotted_time = file_data['allotted_time']
    questions = [Question(qd['text'], qd['answer'], qd['value']) for qd in file_data['questions']]

    return Test(name, subject, author, questions, allotted_time)
