classnames = ['elephant', 'bear', 'boar', 'elephant', 'leopard', 'tiger']
wanted = ['elephant', 'leopard', 'boar', 'tiger']

class ClassNames:
    @staticmethod
    def getAvailableClassNames():
        return classnames
    
    @staticmethod
    def getWantedClassNames():
        return wanted