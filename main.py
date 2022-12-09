import sqlite3


def main():
    conn = sqlite3.connect('textbooks.db')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS book')
    cur.execute('DROP TABLE IF EXISTS publisher')
    cur.execute('DROP TABLE IF EXISTS author')

    cur.execute('''CREATE TABLE book (isbn TEXT PRIMARY KEY NOT
                   NULL, publisher_id TEXT, author_id TEXT, title TEXT, 
                   print_date TEXT, price REAL)''')

    cur.execute('''CREATE TABLE publisher (publisher_id INTEGER PRIMARY KEY NOT
                       NULL, pub_name TEXT, pub_city TEXT, pub_state TEXT, 
                       pub_zip TEXT)''')

    cur.execute('''CREATE TABLE author (author_id INTEGER PRIMARY KEY NOT
                           NULL, first_name TEXT, last_name TEXT, author_address TEXT, 
                           author_city TEXT, author_state TEXT, author_zip TEXT)''')

    book_list = [
        (9780135929032, "Pearson", "Gaddis", "Python Fifth Edition", "2020", 103.45),
        (9876446778888, "American Vision", "DeMar", "Last Days Madness", "2000", 45),
        (1298765434560, "Bethany House", "White", "The Forgotten Trinity", "2020", 16.99)
    ]

    cur.executemany("INSERT INTO book VALUES (?, ?, ?, ?, ?, ?)", book_list)

    pub_list = [
        (1, "Pearson", "Houston", "Texas", "12345"),
        (2, "American Vision", "Atlanta", "Georgia", "54321"),
        (3, "Bethany House", "Minneapolis", "Minnesota", "99999")
    ]

    cur.executemany("INSERT INTO publisher VALUES (?, ?, ?, ?, ?)", pub_list)

    author_list = [
        (1, "Tony", "Gaddis", "1234 Python Road", "Jacksonville", "Florida", "87654"),
        (2, "Gary", "DeMar", "5678 Postmil Avenue", "Atlanta", "Georgia", "54321"),
        (3, "James", "White", "5555 Coogi Lane", "Phoenix", "Arizona", "77777")
    ]

    cur.executemany("INSERT INTO author VALUES (?, ?, ?, ?, ?, ?, ?)", author_list)

    print("Display book data")
    cur.execute("SELECT * FROM book")
    results = cur.fetchall()
    print('ISBN          Publisher            Author     Title                     Date     Price')
    for row in results:
        print(f'{row[0]:10} {row[1]:20} {row[2]:10} {row[3]:25} {row[4]:5} {row[5]:8.2f}')

    print("\n=====================================================================\n")

    print("Display publisher data")
    cur.execute("SELECT * FROM publisher")
    results = cur.fetchall()
    print('Publisher ID   Publisher Name       City         State      Zip')
    for row in results:
        print(f'{row[0]}              {row[1]:20} {row[2]:12} {row[3]:10} {row[4]:5}')

    print("\n=====================================================================\n")

    print("Display original three author table records")
    cur.execute("SELECT * FROM author")
    results = cur.fetchall()
    print('Author ID  First Name      Last Name       Address              City            State      Zip')
    for row in results:
        print(f'{row[0]}          {row[1]:15} {row[2]:15} {row[3]:20} {row[4]:15} {row[5]:10} {row[6]:10}')

    print("\n=====================================================================\n")

    # Insert a new record into the author table
    cur.execute('INSERT INTO author VALUES (4, "Corrie", "ten Boom",  \
                                "19 Bartel St", "Haarlem", "Holland", "2237")')

    print("Display author table data again with newly inserted record")
    cur.execute("SELECT * FROM author")
    results = cur.fetchall()
    print('Author ID  First Name      Last Name       Address              City            State      Zip')
    for row in results:
        print(f'{row[0]}          {row[1]:15} {row[2]:15} {row[3]:20} {row[4]:15} {row[5]:10} {row[6]:10}')

    print("\n=====================================================================\n")

    # Update the city field where author_id = 3
    cur.execute('UPDATE author SET author_city = "Bedfordshire"  \
                                WHERE author_id = 3')

    print("Display author table data again with updated record")
    cur.execute("SELECT * FROM author")
    results = cur.fetchall()
    print('Author ID  First Name      Last Name       Address              City            State      Zip')
    for row in results:
        print(f'{row[0]}          {row[1]:15} {row[2]:15} {row[3]:20} {row[4]:15} {row[5]:10} {row[6]:10}')

    print("\n=====================================================================\n")

    # Delete the record from the author table where the author_id = 1
    cur.execute('DELETE FROM author WHERE author_id = 1')

    print("Display author table data again with deleted record")
    cur.execute("SELECT * FROM author")
    results = cur.fetchall()
    print('Author ID  First Name      Last Name       Address              City            State      Zip')
    for row in results:
        print(f'{row[0]}          {row[1]:15} {row[2]:15} {row[3]:20} {row[4]:15} {row[5]:10} {row[6]:10}')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
