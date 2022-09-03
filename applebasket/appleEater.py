from abc import ABC, abstractmethod

class AppleEater(ABC):
    ''' ABSTRACT CLASS: '''

    @abstractmethod
    def eating(self):
        ''' ABSTRACT METHOD: TO BE DEFINED FOR ALL CHILD CLASSES'''
        pass

