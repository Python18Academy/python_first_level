class AnonymousSurvey:
    """Собирает анонимные ответы на опросник"""

    def __init__(self, question):
        """Содержит вопрос, и подготавливает список для ответов"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Показать вопрос"""
        print(self.question)

    def store_response(self, new_response):
        """Сохраняет у нас ответ"""
        self.responses.append(new_response)

    def show_results(self):
        """Показывает все ответы которые должны быть даны"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")