import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """ Тест для класса AS"""

    def setUp(self):
        """
        Создать опрос и проверить на все е  го методы
        """
        question = "На каком языке вы захотите заговорить"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Проверяет что одиночный ответ был сохранен правильно"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """ Проверяет что каждый отдельный ответ был сохранен правильно"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()