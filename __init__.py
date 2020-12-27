from mycroft import MycroftSkill, intent_file_handler


class Ivypi(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ivypi.intent')
    def handle_ivypi(self, message):
        self.speak_dialog('ivypi')


def create_skill():
    return Ivypi()

