import os


def main():
    path = os.getcwd()


def createLog():
    if os.path.isdir('../InitialProject/logs'):
        pass
    else:
        os.mkdir('../InitialProject/logs')
