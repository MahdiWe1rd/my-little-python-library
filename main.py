import sqlite3

class Book:
    def __init__(self, name, releaseYear, author):
        self.name = name
        self.releaseYear = releaseYear
        self.author = author

class Member:
    def __init__(self, name):
        self.name = name

class Author:
    def __init__(self, name):
        self.name = name




def view_table(con, cur, table_name):
    query = f"SELECT * FROM {table_name}"
    cur.execute(query)
    result = cur.fetchall()
    print(result)


def add_to_table(con, cur, table_name, values):
    query = f"INSERT INTO {table_name} VALUES ({', '.join('?' for _ in values)})"
    cur.execute(query, values)
    con.commit()


def delete_from_table(con, cur, table_name, condition):
    query = f"DELETE FROM {table_name} WHERE {condition}"
    cur.execute(query)
    con.commit()


def update_table(con, cur, table_name, set_clause, condition):
    query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
    cur.execute(query)
    con.commit()


def main():
    con = sqlite3.connect("Back.db")
    cur = con.cursor()


    while True:
        print("What do you want to do today?")
        print("1. View books")
        print("2. View members")
        print("3. View authors")
        print("4. Add book")
        print("5. Add member")
        print("6. Add author")
        print("7. Delete book")
        print("8. Delete member")
        print("9. Delete author")
        print("10. Update book")
        print("11. Update member")
        print("12. Update author")
        print("13. Exit")

        answer = input("Enter a number to perform an operation: ")

        if answer == "1":
            view_table(con, cur, "books")
        elif answer == "2":
            view_table(con, cur, "members")
        elif answer == "3":
            view_table(con, cur, "authors")
        elif answer == "4":
            name = input("Enter book name: ")
            release_date = input("Enter book release date: ")
            author = input("Enter book author: ")
            add_to_table(con, cur, "books", (name, release_date, author))
        elif answer == "5":
            name = input("Enter member name: ")
            add_to_table(con, cur, "members", (name,))
        elif answer == "6":
            name = input("Enter author name: ")
            add_to_table(con, cur, "authors", (name,))
        elif answer == "7":
            condition = input("Enter condition to delete book (e.g., name='Book Name'): ")
            delete_from_table(con, cur, "books", condition)
        elif answer == "8":
            condition = input("Enter condition to delete member (e.g., name='Member Name'): ")
            delete_from_table(con, cur, "members", condition)
        elif answer == "9":
            condition = input("Enter condition to delete author (e.g., name='Author Name'): ")
            delete_from_table(con, cur, "authors", condition)
        elif answer == "10":
            set_clause = input("Enter set clause to update book (e.g., name='New Name'): ")
            condition = input("Enter condition to update book (e.g., name='Old Name'): ")
            update_table(con, cur, "books", set_clause, condition)
        elif answer == "11":
            set_clause = input("Enter set clause to update member (e.g., name='New Name'): ")
            condition = input("Enter condition to update member (e.g., name='Old Name'): ")
            update_table(con, cur, "members", set_clause, condition)
        elif answer == "12":
            set_clause = input("Enter set clause to update author (e.g., name='New Name'): ")
            condition = input("Enter condition to update author (e.g., name='Old Name'): ")
            update_table(con, cur, "authors", set_clause, condition)
        elif answer == "13":
            break
        else:
            print("Invalid option. Please try again.")
        IFcontinue = input("Enter any character to continue : ")
        if IFcontinue != '':
            pass



if __name__ == "__main__":
    main()