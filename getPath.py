import os

def main():
    path = os.getcwd()

def createLog():
    if os.path.isdir('./logs'):
        pass
    else:
        os.mkdir('./logs')