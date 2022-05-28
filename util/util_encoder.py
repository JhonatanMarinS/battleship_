from json import JSONEncoder

class UtilEncoder():
    def default(self, obj):
        return obj.__dict__


