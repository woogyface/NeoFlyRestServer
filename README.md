# NeoFlyRestServer
Just a simple rest server to expose Neo Fly DB. Created in Python 3.9. May run with Python 2.x but i dunno. I don't touch dirty.

WARNING: SQL STATEMENTS ARE NOT CHECKED FOR SAFTY. YOU CAN DESTROY YOUR DB WITH THAT. MAKE A BACKUP!

1. Install Python 3.x
2. Install Flask
```
pip install Flask
```
3. Neo Fly needs to be started at least once so that the db exists at "C:\ProgramData\NeoFly\common.db"
4. Run the server with
```
python app.py
```
5. Run your sql with
```
127.0.0.1:5000/query/<sql statement>

i.e. 127.0.0.1:5000/query/SELECT * FROM balances
```
