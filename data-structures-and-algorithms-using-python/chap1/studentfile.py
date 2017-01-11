# Implemetation of the StudentFileReader ADT using a text file as the
# input source in which each field is stored on a sperate line.
class StudentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0

class StudentFileReader:
    # Create a new student reader instance.
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None

    # Open a connection to the input file.
    def open(self):
        self._inputFile = open(self._inputSrc, "r")

    # Close the connection to the input file.
    def close(self):
        self._inputFile.close()
        self._inputFile = None

    # Extract all student records and store them in a list
    def fetchAll(self):
        theRecords = list()
        student = self.fetchRecord()
        while student != None:
            theRecords.append(student)
            student = self.fetchRecord()
        return theRecords

    # Extract the next student record from the file.
    def fetchRecord(self):
        # Read the first line of the record.
        line = self._inputFile.readline()
        if line == "":
            return None

        # If there is another record, create a storage object and fill it.
        student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._inputFile.readline().rstrip()
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())
        student.gpa = float(self._inputFile.readline())
        return student

class StudentCSVFileReader:
    def __init__( self, filename):
        self._inputSrc = filename
        self._inputFile = None

    def open( self ):
        self._inputFile = open(self._inputSrc, 'r')

    def close( self ):
        self._inputFile.close()
        self._inputFile = None

    def fetchRecord( self ):
        line = self._inputFile.readline()
        if line == '' :
            return None

        vals = line.split(',')
        student = StudentRecord()
        student.idNum = int(vals[0])
        student.firstName = vals[1].rstrip()
        student.lastName  = vals[2].rstrip()
        student.classCode = int(vals[3])
        student.gpa = float(vals[4])
        return student

    def fetchAll( self ):
        theRecords = list()
        student = self.fetchRecord()
        while student:
            theRecords.append(student)
            student = self.fetchRecord()
        return theRecords

class StudentFileWriter:
    def __init__( self, filename ):
        self._outputSrc = filename
        self._outputFile = None

    def open( self ):
        self._outputFile = open( self._outputSrc, 'w' )

    def close( self ):
        self._outputFile.close()
        self._outputFile = None

    def writeRecord( self, student ):
        s = "%d, %s, %s, %d, %.2f\n" % ( student.idNum, student.firstName, student.lastName, \
            student.classCode, student.gpa )
        self._outputFile.write(s)

    def writeAll( self, theRecords ):
        for student in theRecords:
            self.writeRecord( student )

class StudentFileTerminalWriter:
    def __init__( self, filename ):
        pass

    def open( self ):
        pass

    def close( self ):
        pass

    def writeRecord( self, student ):
        s = "%d, %s, %s, %d, %.2f" % ( student.idNum, student.firstName, student.lastName, \
            student.classCode, student.gpa )
        print s

    def writeAll( self, theRecords ):
        for student in theRecords:
            self.writeRecord( student )

