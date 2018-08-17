from datetime import datetime

class Answer(object):
    '''answer class'''

    def __init__(self, answer_provided):

        self.answer_provided = answer_provided
        self.answer_date = datetime.now()

    def post_answer(self, id_count):

        return dict(
            answer=self.answer_provided,
            answer_id=id_count,
            answer_date=self.answer_date
        )
				
		