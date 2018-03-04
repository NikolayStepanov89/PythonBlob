import cx_Oracle

con = cx_Oracle.connect('PP_GNIVC/PP_GNIVC@192.168.10.221:1521/pp221')
cur = con.cursor()
cur.execute('SELECT NOTE FROM HISTORY_LOG where LOG_DATE>=SYSDATE-11')
res=cur.fetchall()
#my_file = open(r'C:\123\5555\snake.xml', 'w')
base_path=r'C:\123\5555'
j=1
#for i in range(j):
for k in res:
    print(k[0].read())
    my_file = open(base_path+'\\'+str(j)+'.xml','w')
    j=j+1
    my_file.write(k[0].read())
    my_file.close()
cur.close()
#con.close()
#con.close()
#con.close()
#con.close()
#con.close()
#con.close()
#con.close()