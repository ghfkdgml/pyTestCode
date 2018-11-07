import psycopg2 as pg

#conn=pg.connect("host=127.0.0.1 dbname=logsee user=postgres password=netcruz!1 port=5432")
#cur=conn.cursor()
#
#try:
#    cur.execute('create table if not exists "TEST" (num integer,name char(5));')
#    cur.execute('select * from "TEST";')
#    cur.execute('insert into "TEST"(num,name) values (%d,%s);'%(3,"e"))
#
#except Exception,e:
#    print e
#
#conn.commit()
#
#conn.close()

class DBMaker():
    def __init__(self,ip,dbname,user,passwd,port):
        self.conn=pg.connect('host=%r dbname=%r user=%r password=%r port=%r'%(ip,dbname,user,passwd,port))
        self.cur=self.conn.cursor()
    def dbInsert(self,table,value):
        if not self.conn or not self.cur:
            print 'connection not exist!'
            return
        try:
            self.cur.execute("""insert into %s values%r;"""%(table,value))
            print 'insert done!'
            self.conn.commit()
        except Exception, e:
            print 'insert failed ',e

    def dbSelect(self,table,column='*'):
        if not self.conn or not self.cur:
            print 'connection not exist!'
            return
        try:
            self.cur.execute("""select %s  from %s"""%(column,table))
            print self.cur.fetchall()

        except Exception, e:
            print 'no result! ',e

    def __del__(self):
        if self.conn:
            self.conn.close()



if __name__=='__main__':
    ip='127.0.0.1'
    dbname='logsee'
    user='postgres'
    password='netcruz!1'
    port='5432'
    test=DBMaker(ip,dbname,user,password,port)
    try:
        test.dbInsert('"TEST"',(4,'suho'))
        test.dbSelect('"TEST"')
    except Exception,e:
        print 'Fail ',e




