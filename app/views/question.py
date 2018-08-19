'''question views '''
from flask import make_response, jsonify, request, Blueprint
from flask.views import MethodView
from app.models.qsn import Question
from api.common.validators import does_object_exist, question_quality


question_blueprint = Blueprint('question', __name__)

questions = list()


class QuestionAsk(MethodView):
    ''' a class for asking question '''

    def post(self):
        ''' method for asking a question'''
        qsn_title = request.json.get('title')
        qsn_body = request.json.get('body')
        if not qsn_title:
            return make_response(jsonify({'message': 'Provide the title of the question'})), 400
        if not qsn_body:
            return make_response(jsonify({'message': 'Provide question body'})), 409
        if does_object_exist(questions, 'title', qsn_title):
            return make_response(jsonify(
                {'message': 'You have asked this question before'})), 409
        quality_check = question_quality(string1=qsn_title, string2= qsn_body)
        if quality_check:
            return make_response(jsonify({'message': quality_check})), 409
        id_count = 1
        for item in questions:
            id_count += 1
        question = Question(qsn_title, qsn_body)
        qsn_dict = question.serialize_question(id_count)
        questions.append(qsn_dict)
        return make_response(jsonify({'message': 'Succesfully asked a question'})), 201

    def get(self):
        '''fetching all questions'''
        


class FetchQuestion(MethodView):
    '''fetching a single question'''

    def get(self):
        ''' a method for fetching a single question'''


question_blueprint.add_url_rule(
    '/questions', view_func=AskQuestion.as_view('ask-question'), methods=['POST'])
question_blueprint.add_url_rule(
    '/questions', view_func=AskQuestion.as_view('fetch-questions'), methods=['GET'])
question_blueprint.add_url_rule(
    '/questions/<questionId>', view_func=FetchQuestion.as_view('fetch-question'), methods=['GET'])