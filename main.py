import extractor as run
import cmd
import sqlitedatabase

class Main(cmd.Cmd):
    def do_greet(self, line):
        print ("hello")

    def do_showdata(self, line):
        if (sqlitedatabase.isTable()):
            sqlitedatabase.showTable()
        else:
            print ("Table/Data not found, please run: downloaddata")

    def do_deletedata(self, line):
        sqlitedatabase.dropTable()

    def do_downloaddata(self, line):
        run.extractData()

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    sqlitedatabase.makeConnection()
    run.extractData()
    print ("=>Avaliable commands:")
    print ("showdata, greet, help, downloaddata, deletedata, dumpdata, deleteentry(id), find_by_name(name), find_by_pricemo(100,300), find_by_pricehr(100,300)... and find_by_custom()")
    Main().cmdloop()
    sqlitedatabase.closeConnection()
