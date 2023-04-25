from task_03.models import Message
from task_03.view import MessageView


class MessageController:
    """
    Класс, описывающий контроллер для работы с сообщениями.
    model и view - это атрибуты класса, которые содержат
    соответствующие модель и представление, используемые контроллером.
    """
    model = Message
    view = MessageView

    @classmethod
    def get_message(cls):
        """
        Возвращает сообщение приветствия в формате HTML,
        используя модель Message и представление MessageView.
        """
        message = cls.model.get_hello_message()
        return cls.view.show_message(message=message)

    @classmethod
    def get_success_message(cls):
        """
        Возвращает сообщение об успешной отправке данных в формате JSON,
        используя модель Message и представление MessageView.
        :return:
        """
        message = cls.model.get_success_message()
        return cls.view.show_success_message(message=message)
