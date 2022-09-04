from abc import ABC, abstractmethod

'''
Interface for all connectors. 
'''
class BasicConnector( ABC ):
    @abstractmethod
    def getConnection( self ):
        raise NotImplementedError

    '''
    @abstractmethod
    def importAccounts():
        raise NotImplementedError

    @abstractmethod
    def importGroups():
        raise NotImplementedError
    '''