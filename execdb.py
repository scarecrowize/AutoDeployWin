# -*- coding: utf-8 -*-
import sqlite3
import xlrd
import sys

DB = 'AutoDeploy.db'
sheet_index = 0
Excelname = 'machineinfo.xlsx'


class Execdb:
    def __init__(self,**kw):
        if 'machinetype' in kw.keys():
            self.machinetype = kw['machinetype']
        if 'addr' in kw.keys():
            self.addr = kw['addr']
        if 'role' in kw.keys():
            self.role = kw['role']
        if 'env' in kw.keys():
            self.env = kw['env']
        if 'apppath' in kw.keys():
            self.apppath = kw['apppath']
        if 'passwd' in kw.keys():
            self.passwd = kw['passwd']
    
    
    def createdb(self):
        conn = sqlite3.connect(DB)
        conn.text_factory = str
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS MACHINEINFO(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            MACHINETYPE VARCHAR(50) NOT NULL,
            ADDR VARCHAR(50) NOT NULL,
            ROLE VARCHAR(50) NOT NULL,
            ENV VARCHAR(50) NOT NULL,
            APPPATH VARCHAR(50) NOT NULL,
            PASSWD VARCHAR(50) NOT NULL);''')
        conn.close()
    
    
    def insertdb(self):
        conn = sqlite3.connect(DB)
        conn.text_factory = str
        cur = conn.cursor()
        cur.execute("INSERT INTO MACHINEINFO (MACHINETYPE,ADDR,ROLE,ENV,APPPATH,PASSWD) VALUES ('%s','%s','%s','%s','%s','%s') " % (self.machinetype,self.addr,self.role,self.env,self.apppath,self.passwd))
        conn.commit()
        conn.close()
    
        
    def selectbyrole(self):
        conn = sqlite3.connect(DB)
        conn.text_factory = str
        cur = conn.cursor()
        cur.execute("select * from MACHINEINFO WHERE ROLE = '%s'" % self.role)
        data = cur.fetchall()
        return data
    
    
    def selectbyaddr(self):
        conn = sqlite3.connect(DB)
        conn.text_factory = str
        cur = conn.cursor()
        cur.execute("select * from MACHINEINFO WHERE ADDR = '%s'" % self.addr)
        data = cur.fetchall()
        return data


class LoadExcel:
    def __init__(self):
        self.data = xlrd.open_workbook(Excelname)
        self.table = self.data.sheet_by_index(sheet_index)
    
    
    def getvalues(self):
        nrows = self.table.nrows
        colname = self.table.row_values(0)
        fulldata = []
        for i in range(1,nrows):
            row = self.table.row_values(i)
            if row:
                rowdata = {}
                for j in range(len(row)):
                    rowdata[colname[j]] = row[j]
                fulldata.append(rowdata)
        return fulldata


#insert Excel file data to sqlite3 database
def Exceltodb():
    exceldata = LoadExcel()
    kwargs = exceldata.getvalues()
    for args in kwargs:
        db = Execdb(**args)
        db.createdb()
        db.insertdb()



if __name__ == '__main__':
    sys.stderr.write('''You shouldn't be running this file directly,it is used as model.''')






















































































