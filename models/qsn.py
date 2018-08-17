from datetime import datetime

class Question(object):

    def __init__(self, title, content): 
        self.title = title
        self.content = content
        self.date_posted = datetime.now()
        self.questions = []
        
    def post_question(self,Id, heading, content,date_posted):
        new_question = {
            'Id': Id,
            'heading': heading,
            'content': content,
            'date_posted':date_posted}

        self.questions.append(new_question)
        return (self.questions)