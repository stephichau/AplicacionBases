import psycopg2
import sys
import json

returnDict = {}

try:
    # Cambiar
    conn = psycopg2.connect("dbname=XX user=XX")
    cur = conn.cursor()
    cur.execute(sys.argv[1])
    if cur.statusmessage.startswith("SELECT"):
        returnDict["STATUS"] = "OK"
        returnDict["MESSAGE"] = cur.statusmessage

        columns = [column.name for column in cur.description]
        tuples = []

        t = cur.fetchone()
        while t:
            tuples.append(list(t))
            t = cur.fetchone()

        returnDict['columns'] = columns
        returnDict['tuples'] = tuples
        print(json.dumps(returnDict))
    else:
        returnDict["STATUS"] = "OK"
        returnDict["MESSAGE"] = cur.statusmessage
        conn.commit()
        print(json.dumps(returnDict))

except Exception as e:
    returnDict['STATUS'] = "ERROR"
    returnDict['MESSAGE'] = str(e)
    print(json.dumps(returnDict))
    conn.close()

conn.close()
