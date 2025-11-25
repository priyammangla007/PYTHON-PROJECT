● Problem Statement
The goal is to develop a simple digital tool to replace manual, paper-based library inventory systems. This addresses inefficiencies such as difficulty in tracking books, potential for data loss, and time-consuming manual record updates. The system should provide a basic, intuitive interface for managing available books.

● Scope of the Project
The scope of this project is a local, single-user desktop application designed for managing book inventory within a small library or personal collection.
Inclusions:
Adding new book records (Title, Author, Status).
Viewing all existing book records in a table format.
Deleting book records by ID.
Using built-in Python libraries (tkinter for GUI and sqlite3 for database).

Exclusions:
User authentication or member management.
Book loaning/borrowing functionality (checkout/check-in).
Advanced search, filtering, or sorting capabilities.
Multi-user network access.

● Target Users
The primary users of this application are:
Librarians: Responsible for day-to-day management of the book inventory.
Library Staff/Volunteers: Individuals tasked with cataloging new donations or removing discarded books.

● High-Level Features
The system provides the following core functionalities:
Database Management: Automatic creation of a library.db SQLite file upon first run.
Add Book Interface: A dedicated GUI window to input book title and author details.
View Inventory: A Toplevel window displaying all books in a structured Treeview (table) widget.
Delete Book Functionality: A simple interface to remove a specific book record using its unique database ID.
User Feedback: Implementation of tkinter message boxes for success confirmations and error handling.


.