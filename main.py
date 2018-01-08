#!/usr/bin/python
import extractor as run
import cmd
import sqlitedatabase
import sys


class Main(cmd.Cmd):
    prompt = 'marcos@digesto> '
    def do_greet(self, line):
        print ("hello")

    def do_show(self, line):
        if (sqlitedatabase.isTable()):
            sqlitedatabase.showTable()
        elif (line == 'arg'):
            print ("Table/Data not found, please run: python3 main.py download")
        else:
            print ("Table/Data not found, please type: download")

    def do_delete(self, line):
        sqlitedatabase.dropTable()

    def do_download(self, line):
        run.extractData()

    def do_h (self, line):
        print ("@Avaliable arguments:")
        print ("\t$python3 main.py download \t-> Extract and Download data from websites requested")
        print ("\t$python3 main.py show \t\t-> Show table of data downloaded if avaliable")
        print ("\t$python3 main.py delete \t-> Delete data and drop table from local SQlite3")
        print ("\t$python3 main.py cli \t\t-> Run in command line input mode")
        print ("\t$python3 main.py help \t\t-> Show help for using this crawler")

    def do_help (self, line):
        print ("@Avaliable commands:")
        print ("\tdownload \t-> Extract and Download data from websites requested")
        print ("\tshow \t\t-> Show table of data downloaded if avaliable")
        print ("\tdelete \t\t-> Delete data and drop table from local SQlite3")
        print ("\texit \t\t-> Exit command line input mode")

    def do_EOF(self, line):
        return True

    def do_exit(self, line):
        return True


if __name__ == '__main__':
    sqlitedatabase.makeConnection()
    if (len(sys.argv) <= 1 or len(sys.argv) >= 3):
        print ("=>Invalid arguments")
        Main().do_h('arg')
    elif (str(sys.argv[1]) == 'cli'):
        Main().do_help('arg')
        Main().cmdloop()
    elif (str(sys.argv[1]) == 'download'):
         Main().do_downloaddata('arg')
    elif (str(sys.argv[1]) == 'delete'):
         Main().do_deletedata('arg')
    elif (str(sys.argv[1]) == 'show'):
         Main().do_showdata('arg')
    else:
        print ("=>Invalid arguments")
        Main().do_h('arg')
    sqlitedatabase.closeConnection()
