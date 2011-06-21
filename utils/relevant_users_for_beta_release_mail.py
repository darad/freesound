import psycopg2
import time
from datetime import date
import json

def datetimeToSqlDate(date) :
    return str(date.year) + "-" + str(date.month) + "-" + str(date.day)

def run():
    
    tic = time.clock()
        
    # Connect to database
    DB_NAME = ""
    DB_USER = ""
    
    print "Connecting to " + DB_NAME + " database..." ,
    conn = psycopg2.connect("dbname=" + DB_NAME + " user=" + DB_USER)
    cur = conn.cursor()
    print "done!\n\n"
    
    # PARAMETERS
    date_threshold = date(2010, 6, 20) # Date of last visit must be greater thn date threshold
    uploaded_sounds_threshold = 100 # Minimum number of uploaded sounds
    
    cur.execute("""SELECT user_id, COUNT(DISTINCT id) FROM sounds_sound GROUP BY user_id ORDER BY COUNT(DISTINCT id) DESC""")
    users = cur.fetchall()
    
    data = []
    count = 0
    for user in users:
        if user[1] >= uploaded_sounds_threshold :
            # Retrieve user data and check lastlogin
            cur.execute("""SELECT id, username, email FROM auth_user WHERE last_login >= '""" + datetimeToSqlDate(date_threshold) + """' AND id = """ + str(user[0]))
            user_data = cur.fetchall()
            if len(user_data)>0 :
                data.append({'id': user_data[0][0], 'name': user_data[0][1], 'email': user_data[0][2], 'uploaded_sounds': user[1]})
                #print str(user_data[0][0]) + " " + user_data[0][1] + ": " + user_data[0][2] + " (" +  str(user[1]) + " sounds)"
                count += 1
     
    with open('beta_release_mails.json', mode='w') as f:
        json.dump(data, f, indent = 4)
        
    
    print data
    print "\nTotal number of users: " + str(count)
    
    
    
    print "\n"
    print "Closing connection to " + DB_NAME + " database..." ,
    cur.close()
    conn.close()
    print "done!\n\n"
    
    toc = time.clock()
    print '(performed in ' + str(toc-tic) + ' seconds)\n\n'

# Call the run() function (if exetued as a script)
if __name__ == '__main__':
    run()