import sqlite3 as sq
from tkinter import messagebox


# function for creating database
def create_database(db_name):
    '''
    INPUT- string name for the database\n
    OUTPUT-database instance
    '''
    try:
        db = sq.connect(db_name)
        print('Database created sucessfully')
        return db
    except Exception as e:
        return e

# function for creating cursor on database 
def get_cursor(db):
    '''
    INPUT-DATABASE INSTANCE\n
    OUTPUT-cursor instance
    '''
    try:
        return db.cursor() 
    except Exception as e:
        return e

# function for creating table in database
def create_table(db, cr, table, attrs, pk=None, fk=None):
    '''
    INPUT:- db-> database object\n
            cr-> cursor object\n
            table-> table name\n
            attrs-> dict of attributes(where key-> attribute name and value->type)\n
            pk-> string(attribute name)\n
            fk-> dictonary containing the following
            {\n
                'self_attr': 'value' -> This is the attr of the referencing table usually the pk\n
                'ref_table': 'value' -> This denotes the referenced table name (ex. books, students, etc)\n
                'ref_attr': 'value' -> This denotes the attribute of the referenced table (usually the pk of referenced table)\n
            }\n

    OUTPUT:- return None\n
    OUTCOME:- creates a table of the given name and with the given list of parameters
    '''
    temp_lst = []
    for item in list(attrs.items()):
        if item[0] == pk and pk!=None:
            temp_str = f'{item[0]} {item[1]} primary key'
        else:
            temp_str = item[0]+' '+item[1]
        temp_lst.append(temp_str)
    
    
    var = ', '.join(temp_lst)
    if fk!=None:
        var = var+f', foreign key ({fk["self_attr"]}) references {fk["ref_table"]} ({fk["ref_attr"]})'
    # print(var)

    try:
        cr.execute(f'CREATE TABLE {table}({var})')
    except Exception as e:
        print(e)        
    finally:
        db.commit()


def insert_normal(db, cr, data, table_name):
    try:
        v=''
        for i in data:
            temp_str = f'"{i}", '
            v+=temp_str
        v=v[:len(v)-2]
        stmnt=f"insert into {table_name} values({v})"

        cr.execute(stmnt)
        messagebox.showinfo("Success", 'Member inserted successfully')

    except Exception as e:
        print(e)
        messagebox.showerror("Error", e)
    db.commit()


# show all data
def show_func(cr, table):
    cr.execute('SELECT * FROM {}'.format(table))
    data = cr.fetchall()
    return data




