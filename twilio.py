from twilio.rest import Client
import mysql.connector
import config

#Clients
msgClient = Client(config.account_sid, config.auth_token)
verifyClient = Client(config.account_sid, config.auth_token)

#Create two variables here that will store a full name and 
#phone number to input into validation call

mydb = mysql.connector.connect(
  host="104.236.37.73",
  user="test",
  passwd="Testing123!@#",
  database="cruzhax"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM clients")

result = mycursor.fetchone()

user = 'temp'

for x in result:
    user = x

mydb.close()

print(user)

# #verify
# caller_id = verifyClient.validation_requests.create(
#     friendly_name='First Last',
#     phone_number='+16692371199'
# )
# #Saves verification code sent to client
# verifyCode = caller_id.validation_code
# print(verifyCode)

#Send Message 
# message = msgClient.messages.create( 
#     from_='+14243795098',  
#     body='hey',     
#     to='+16263758987' 
# ) 
# print(message.sid)






# import tweepy
# import mysql.connector


# mydb = mysql.connector.connect(
#   host="104.236.37.73",
#   user="test",
#   passwd="Testing123!@#",
#   database="cruzhax"
# )

# mycursor = mydb.cursor()

# # sql = "INSERT INTO clients (name, phone) VALUES (%s, %s)"
# # val = ("Pablo Gaeta", "+16263758987")
# # mycursor.execute(sql, val)

# # mydb.commit()

# # print(mycursor.rowcount, "record inserted.")
# mycursor.execute("SELECT * FROM clients")

# result = mycursor.fetchall()

# for x in result:
#     print(x[0])

# mydb.close()