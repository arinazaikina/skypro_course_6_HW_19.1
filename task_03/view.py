import json


class MessageView:
    """
    Класс, описывающий отображение сообщений
    """
    @classmethod
    def show_message(cls, message: str) -> str:
        """
        Отображает сообщение в виде HTML заголовка первого уровня.
        :param message: текст сообщения
        """
        return f"<h1>{message}</h1>"

    @classmethod
    def show_success_message(cls, message: str) -> str:
        """
        Отображает сообщение об успешной отправке данных в формате JSON.
        :param message: текст сообщения
        """
        response = {
            "status": "success",
            "message": message
        }
        return json.dumps(response)
