import MySQLdb

conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='baidu',port=3306)
cur=conn.cursor()

sql = "insert into test(name, score) values(%s, %s);"
file = open("./test.txt")
while 1:
    #line = file.readline()
        
    lines = file.readlines()
    if not lines:
        break
    values = []
    for line in lines:
        line = line.strip('\n')
        arr = line.split(',')
        print arr
        #print arr[0],"+",arr[1]

        #count = cur.execute('select * from test')
        #results=cur.fetchmany(count)
        #for r in results:
        #    print r

        #sql = "insert into test(name, score) values(%s, %s);"
        value = (arr[0], arr[1])
        #print value
        values.append(value)

    try:
        cur.executemany(sql, values)

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
    conn.commit()
cur.close()
conn.close()

