from .model import Log


def getAll():
    return Log.objects.all()
