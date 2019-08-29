from random import *
from console import fg, bg, fx 
import console
import os 
import render
from matrixLine import MatrixLine
import time  


import SQLconnector



conn = SQLconnector.connectToSource()
cursor = conn.cursor()
sql = "select p.PlayerID, GamerTag from participation p join players pl on p.playerID = pl.playerID order by NEWID ()"
cursor.execute(sql)
dimensions = render.get_terminal_size_windows()

os.system("cls")

for row in cursor.fetchall():
    var = MatrixLine(   row[0]+row[1],
                        (random()*dimensions[0])-random()*len(row[0]+row[1]),
                        random()*dimensions[1],
                        random()*1)
    var.start() 
    time.sleep(0.33)