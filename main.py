
from bs4 import BeautifulSoup
import mysql.connector



# Parse the HTML content using BeautifulSoup
with open('example data.html', 'r') as file:
    doc = BeautifulSoup(file, 'html.parser')

list = []
# Find all elements with the tag 'tr' (rows of data)
rows = doc.find_all('tr')

# Go through each row and put all the columns into their own
for each_row in rows:
    columns = each_row.find_all('td')

    row_values = []
    for each_column in columns:
        row_values.append(each_column.text.strip())
    
    list.append(row_values)

list.remove(list[0])

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="admin",
  database="User_data"
)

SQLcursor = mydb.cursor()
'''
name
phone
email
address
postalZip
'''
#SQLcursor.execute("CREATE DATABASE User_Data") Create the database
SQLcursor.execute("CREATE TABLE Users (id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Phone VARCHAR(255), Email VARCHAR(255), Address VARCHAR(255), PostalZip VARCHAR(255))") # Create a table in the User_Data databse for the user's information

# Syntax for the SQL
sql = "INSERT INTO Users (Name, Phone, Email, Address, PostalZip) VALUES (%s, %s, %s, %s, %s)"


for each_list_item in list:
    values = (each_list_item)
    print(each_list_item)
    SQLcursor.execute(sql, values)



mydb.commit()


#test
    
#print(doc.prettify())
