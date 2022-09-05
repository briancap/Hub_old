import os.path

from integration.interface.BasicConnector import BasicConnector


class DelimitedFileConnector( BasicConnector ):

    #boolean defining what connector supports
    supports_import_accounts_full = True
    supports_import_accounts_delta = False
    supports_import_accounts_single = False

    #configuration for processing the file
    filename = "/home/briancap/Documents/hub_users.csv"
    has_header_row = True
    delimiter = ","

    #positions for each field

    connection = None
    
    def getConnection( self ):
        print( 'STARTING getConnection' )
    
        if os.path.isfile( self.filename ):
            self.connection = open( self.filename )
        
        print( 'ENDING getConnection' )


    def importAccounts( self ):
        print( 'STARTING importAccounts' )

        if( self.connection is None ):
            self.getConnection()
        
        rowCount = 0

        for line in self.connection:
            rowCount += 1

            #loop over every row in the file, first row will be skipped if it is a header
            if( ( self.has_header_row and rowCount > 1 ) or not self.has_header_row ):

                #single rows are split based off the global delimiter
                rowArray = line.split( self.delimiter )

                #loop over individual fields in a line, rstrip removes \n characters
                # there is always a \n in the last field of every row
                for field in rowArray :
                    field = field.rstrip()
                    print( field )


        #set connection to None so new connection can be established for potential other files
        self.connection.close()
        self.connection = None
        print( 'ENDING importAccounts' )
