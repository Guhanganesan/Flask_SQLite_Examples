# Flask_SQLite_Examples 

# Installation 

1. Go to C:\Python37\Scripts\ (make sure that virtualenv is available or not, if it is not availble you have install the virtualenv using command => pip install virtualenv)

2. Go to D:\myfolder (Create new empty folder as myfolder in D drive then move into the myfolder )

3. cd myfolder (move inside the folder)

4. D:\myfolder\ virtualenv venv (install the supporting packages..)

5. D:\myfolder\ cd venv (move inside the venv folder)

6. D:\myfolder\ venv\ mkdir myapp (create new folder as myapp )

7. D:\myfolder\ venv\ cd myapp ( move inside the folder)

8. D:\myfolder\venv \myapp\ touch app.py (create python app file)

9. D:\myfolder\venv \myapp \cd.. (go back)

10. D:\myfolder\ venv\ cd Scripts (go into scripts)

11. D:\myfolder\ venv\ Scripts\ activate

12. D:\myfolder\ venv\ Scripts\ cd.. (go back)

13. D:\myfolder\ venv\ pip install flask

14. D:\myfolder\ venv\ cd myapp (move into the myapp folder)

15. D:\myfolder\ venv\ myapp\ python app.py (run the app)

16. Check in your browser: http://127.0.0.1:5000/

17. To Change IP Address: python -m flask run --host=172.16.3.64


# Sqlit3 Installations

1. Download Precompiled Binaries for Windows => https://www.sqlite.org/download.html
2. After downloading the zip and extact in a new folder and place in C drive
3. Add path in sytem env varibales
4. check: cmd=> sqlite3 (ctrl+c)
5. Create Database: sqlite3 test.db
6. Create Table:  CREATE TABLE Employee(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS TEXT NOT NULL, SALARY REAL);
7. INSERT INTO Employee (NAME,AGE,ADDRESS,SALARY) VALUES ('Guhan', 32, 'India', 20000.00);
8. SELECT * FROM Employee;




