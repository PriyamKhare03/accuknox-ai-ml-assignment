# Task 1
import requests
import sqlite3
db_name = "book.db"
API_URL = "https://www.googleapis.com/books/v1/volumes?q=fiction"

def fetch_book_from_api(url):
  response = requests.get(url)
  data = response.json()
  return data.get("items",[])


def create_database(db_name):
  conn = sqlite3.connect(db_name)
  cursor = conn.cursor()
  cursor.execute("""
  CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year TEXT
  )
  """)
  conn.commit()
  conn.close()

def insert_book_db(books):
  conn = sqlite3.connect(db_name)
  cursor = conn.cursor()
  for book in books:
    volume_Info = book.get('volumeInfo',{})
    title = volume_Info.get("title")
    author = ", ".join(volume_Info.get('authors',[]))
    year = volume_Info.get("publishedDate",'N/A')
    cursor.execute("""
            INSERT INTO books (title, author, year)
            VALUES (?, ?, ?)
        """, (title, author, year))

  conn.commit()
  conn.close()

def Display_books():
  conn = sqlite3.connect(db_name)
  cursor = conn.cursor()
  cursor.execute("""
  SELECT title,author,year FROM books;""")
  rows = cursor.fetchall()
  print("\nBooks stored in database:\n")
  for row in rows:
    print(row)
  conn.close()





if __name__ == "__main__":
  books_data = fetch_book_from_api(API_URL)

  create_database(db_name)
  insert_book_db(books_data)
  Display_books()
