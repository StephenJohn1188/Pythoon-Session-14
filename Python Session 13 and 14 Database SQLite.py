#!/usr/bin/env python
# coding: utf-8

# # Create Database

# In[1]:


import sqlite3


# Working with DB using SQL
# 
# 1. create a connection object
# 2. from the connection object, crate a cursor object
# 3. Using the cursor object, call the execute method with create table query as the parameter
# 

# In[2]:


db=sqlite3.connect('student_database.db')


# Cursor
# A cursor is a temporary work area created in system memory when a sql is execute

# In[3]:


cur=db.cursor()


# In[27]:


cur.execute("create table student(id int primary key,name text,marks int )")


# In[28]:


cur.execute("insert into student(id,name,marks) values(1,'John',90)")
db.commit()


# In[30]:


print(cur.rowcount,"Record(s) inserted")


# In[34]:


cur.execute("insert into student(id,name,marks) values(2,'Jaon',85)")
db.commit()


# In[4]:


results=cur.execute("select * from student")

for row in results:
    print(row)


# In[36]:


cur.execute("insert into student(id,name,marks) values(3,'Sam',85)")
db.commit()


# In[37]:


print(cur.rowcount,"Record(s) inserted")


# In[38]:


results=cur.execute("select * from student")

for row in results:
    print(row)


# In[44]:


results=cur.execute("select id,marks from student")

for row in results:
    print(row)
                    


# In[5]:


cur.execute("insert into student(id,name,marks) values(4,'Mark',10)")
db.commit()


# In[6]:


results=cur.execute("select id,marks from student")

for row in results:
    print(row)


# In[7]:


results=cur.execute("select * from student")

for row in results:
    print(row)


# In[10]:


result=cur.execute("Select * from student where id=1")
for i in result:
    print(i)


# In[11]:


result=cur.execute("Select * from student limit 5")
for i in result:
    print(i)


# In[12]:


result=cur.execute("Select * from student limit 3")
for i in result:
    print(i)


# In[13]:


result=cur.execute("Select name from student where id=3")
for i in result:
    print(i)


# In[14]:


result=cur.execute("Select * from student where name='John'")
for i in result:
    print(i)


# In[15]:


result=cur.execute("Select * from student where marks>80 and marks<90")
for i in result:
    print(i)


# In[17]:


results=cur.execute("select * from student")
results.fetchall()


# In[21]:


result=cur.execute("Select * from student order by name asc")

for i in result:
    print(i)


# In[22]:


result=cur.execute("Select * from student order by name desc")

for i in result:
    print(i)


# In[24]:


result=cur.execute("Select * from student where name='John' and marks=90")

for i in result:
    print(i)


# In[25]:


result=cur.execute("Select * from student where name='John' or marks=10")

for i in result:
    print(i)


# In[26]:


result=cur.execute("Select min(marks) from student")

for i in result:
    print(i)


# In[27]:


result=cur.execute("Select max(marks) from student")

for i in result:
    print(i)


# In[28]:


result=cur.execute("Select max(marks) from student")
result.fetchone()


# In[29]:


result=cur.execute("Select count(id) from student")

for i in result:
    print(i)


# In[31]:


result=cur.execute("Select * from student where marks between 80 and 90")

for i in result:
    print(i)


# In[32]:


result=cur.execute("Select * from student where marks is null")

for i in result:
    print(i)


# In[33]:


result=cur.execute("Select * from student where marks is not null")

for i in result:
    print(i)


# In[34]:


result=cur.execute("Select * from student where name like 'J%'")

for i in result:
    print(i)


# In[36]:


result=cur.execute("Select * from student where name like '_a%'")

for i in result:
    print(i)


# In[37]:


result=cur.execute("Select * from student where name like '%a%'")

for i in result:
    print(i)


# In[38]:


result=cur.execute("Select * from student where name like '___'")

for i in result:
    print(i)


# In[53]:


result=cur.execute("Select * from student where marks NOT in (90)")

for i in result:
    print(i)


# In[47]:


result=cur.execute("Select * from student where name NOT in ('John')")

for i in result:
    print(i)


# Update Record

# In[58]:


sql="update student set marks=81 where id in (3)"
cur.execute(sql)
db.commit()


# In[60]:


result=cur.execute("Select * from student where id=3")

for row in result:
    print(row)


# In[61]:


sql="update student set marks=75 where id in (1)"
cur.execute(sql)
db.commit()


# In[62]:


sql="update student set marks=80 where id in (2)"
cur.execute(sql)
db.commit()


# In[63]:


sql="update student set marks=15 where id in (4)"
cur.execute(sql)
db.commit()


# # Delete any unwanted records

# In[66]:


sql='delete from student where id=4'
cur.execute(sql)


# In[67]:


result=cur.execute("Select * from student")

for i in result:
    print(i)


# # Drop the Table

# In[68]:


sql='drop table student'
results=cur.execute(sql)


# In[69]:


result=cur.execute("Select * from student")

for i in result:
    print(i)

