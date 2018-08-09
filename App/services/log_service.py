from App.models import Log

def getAll():
    return Log.objects.all()

