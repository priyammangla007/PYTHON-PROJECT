import sqlite3
from tkinter import *
from tkinter import ttk, messagebox


# --- Database Setup ---

def database_connection():
    """Connects to the SQLite database and creates the table if it doesn't exist."""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn, cursor


# --- Backend Functions ---

def add_book_backend(title, author):
    """Adds a new book record to the database."""
    if not title or not author:
        messagebox.showerror("Error", "Title and Author cannot be empty.")
        return False
    conn, cursor = database_connection()
    try:
        cursor.execute("INSERT INTO books (title, author, status) VALUES (?, ?, ?)", (title, author, 'Available'))
        conn.commit()
        messagebox.showinfo("Success", "Book added successfully.")
        return True
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
        return False
    finally:
        conn.close()


def view_books_backend():
    """Retrieves all book records from the database."""
    conn, cursor = database_connection()
    cursor.execute("SELECT * FROM books")
    records = cursor.fetchall()
    conn.close()
    return records


def delete_book_backend(book_id):
    """Deletes a book record from the database by ID."""
    conn, cursor = database_connection()
    try:
        cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        conn.commit()
        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Book deleted successfully.")
            return True
        else:
            messagebox.showerror("Error", "Book ID not found.")
            return False
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
        return False
    finally:
        conn.close()


# --- GUI Functions ---

def clear_entries(entries):
    """Clears all provided entry widgets."""
    for entry in entries:
        entry.delete(0, END)


def add_book_gui(window):
    """GUI to add a new book."""
    window.title("Add Book")
    window.geometry("300x200")

    Label(window, text="Title:", font=("Arial", 12)).pack(pady=5)
    title_entry = Entry(window, width=30)
    title_entry.pack(pady=5)

    Label(window, text="Author:", font=("Arial", 12)).pack(pady=5)
    author_entry = Entry(window, width=30)
    author_entry.pack(pady=5)

    def submit_add():
        if add_book_backend(title_entry.get(), author_entry.get()):
            clear_entries([title_entry, author_entry])

    Button(window, text="Add Book", command=submit_add).pack(pady=10)


def view_books_gui(window):
    """GUI to view all books in a Treeview."""
    window.title("View Books")
    window.geometry("600x400")

    tree = ttk.Treeview(window, columns=("ID", "Title", "Author", "Status"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.heading("Status", text="Status")

    tree.column("ID", width=50, anchor=CENTER)
    tree.column("Title", width=200)
    tree.column("Author", width=150)
    tree.column("Status", width=100, anchor=CENTER)

    # Add scrollbar
    scrollbar = Scrollbar(window, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    tree.pack(expand=True, fill=BOTH)

    # Insert data
    for record in view_books_backend():
        tree.insert("", END, values=record)


def delete_book_gui(window):
    """GUI to delete a book by ID."""
    window.title("Delete Book")
    window.geometry("300x150")

    Label(window, text="Enter Book ID:", font=("Arial", 12)).pack(pady=10)
    id_entry = Entry(window, width=10)
    id_entry.pack(pady=5)

    def submit_delete():
        try:
            book_id = int(id_entry.get())
            if delete_book_backend(book_id):
                id_entry.delete(0, END)
        except ValueError:
            messagebox.showerror("Error", "Invalid Book ID. Please enter a number.")

    Button(window, text="Delete Book", command=submit_delete).pack(pady=10)


# --- Main Application Window ---

def main_window():
    root = Tk()
    root.title("Library Management System")
    root.geometry("400x300")
    root.configure(bg="#f0f0f0")

    Label(root, text="Library Management System", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=20)

    # Functions to open new windows for each feature
    def open_add_window():
        new_window = Toplevel(root)
        add_book_gui(new_window)

    def open_view_window():
        new_window = Toplevel(root)
        view_books_gui(new_window)

    def open_delete_window():
        new_window = Toplevel(root)
        delete_book_gui(new_window)

    Button(root, text="Add Book", command=open_add_window, width=20, bg="#4CAF50", fg="white").pack(pady=10)
    Button(root, text="View All Books", command=open_view_window, width=20, bg="#2196F3", fg="white").pack(pady=10)
    Button(root, text="Delete Book", command=open_delete_window, width=20, bg="#f44336", fg="white").pack(pady=10)
    Button(root, text="Exit", command=root.destroy, width=20, bg="#ff9800", fg="white").pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main_window()
