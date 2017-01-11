from studentfile import StudentFileReader, StudentCSVFileReader, \
    StudentFileWriter, StudentFileTerminalWriter

CSV_FILE_NAME = "students.csv"
CSV_FILE_OUT_NAME = "students_outtest.csv"

def main():
    reader = StudentCSVFileReader( CSV_FILE_NAME )
    reader.open()
    studentList = reader.fetchAll()
    reader.close()

    sortKey = raw_input( "Input the sort key:" )
    studentList.sort( key = lambda rec: getattr( rec, sortKey ) )

    writer = StudentFileWriter( CSV_FILE_OUT_NAME )
    studentDisplay = StudentFileTerminalWriter( "terminal" )
    writer.open()
    studentDisplay.open()
    writer.writeRecord( studentList[ 0 ] )
    studentDisplay.writeRecord( studentList[ 0 ] )
    writer.writeAll( studentList[ 1: ] )
    studentDisplay.writeAll( studentList[ 1: ] )
    writer.close()
    studentDisplay.close()

main()
