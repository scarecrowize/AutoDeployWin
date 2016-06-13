# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('AutoDeploy.db')

class Execdb:
    def __init__(self,*args):
        for arg in args:
            if arg.upper() == 'WINDOWS' :
                self.MachineType = arg
            elif len(arg.split('.')) ==4:
                self.Addr = arg
            elif arg in ['Agent','Task']:
                self.Role = arg
            elif arg in ["深圳1","深圳2","深圳3"]:
                self.Env = arg
            elif len(arg.split(':')) ==2:
                self.AppPath = arg
            else:
                print 'Error args for init Execdb'
    
    def insertdb(self):
        conn = sqlite3.connect('AutoDeploy.db')
        conn.text_factory = str
        conn.execute("INSERT INTO MACHINEINFO (MachineType,Addr,Role,Env,AppPath) VALUES ('%s','%s','%s','%s','%s') " % (self.MachineType,self.Addr,self.Role,self.Env,self.AppPath))
        conn.commit()
        conn.close()
        
    def selectdb(self):
        conn = sqlite3.connect('AutoDeploy.db')
        conn.text_factory = str
        data=conn.execute("select * from MACHINEINFO WHERE Role='%s'" % self.Role)
        return data
        

#db=Execdb('Agent')
#a=db.selectdb()
#for row in a:
#    for i in range(len(row)):
#        print row[i]

db=Execdb("Task","11.11.11.11","windows","深圳2","c:\programfile")
db.insertdb()

