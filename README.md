# Library Management System (Python + CSV)

**One-line:** A lightweight Library Book Management System built with Python and CSV files for storage — supports book inventory, issue/return transactions, member management, and reporting.

---

## 1. Aim
Design and implement a simple, maintainable desktop application (Python + CSV) to manage library operations: register books and members, issue and return books, track fines, and produce circulation reports.

## 2. Problem Statement
Small institutes and clubs often manage library records manually on paper or spreadsheets. This is time-consuming and error-prone. The proposed system provides a reliable, easy-to-use software tool to maintain book inventory, transaction history, and member records using simple CSV storage.

## 3. Objectives
- Maintain `books.csv` with inventory details and availability.
- Maintain `members.csv` for library users.
- Record issue/return transactions in `transactions.csv` with timestamps and fine calculation.
- Provide CRUD operations for books and members, search, and reporting (daily/monthly circulation and overdue lists).
- Ensure usability, reliability, and simple deployment (single-machine, no DB server).

---

## 4. Functional Requirements (major modules)
The system includes at least three major functional modules:

### 4.1 Book Inventory Management
- **Functions:** add_book, edit_book, delete_book, search_books, list_books
- **Input:** ISBN/ID, title, author, category, copies
- **Output:** updates `books.csv`, GUI/list output

### 4.2 Member Management
- **Functions:** add_member, edit_member, delete_member, search_members
- **Input:** member_id, name, contact, join_date
- **Output:** updates `members.csv`, GUI confirmation

### 4.3 Issue/Return & Transaction Management
- **Functions:** issue_book(member_id, book_id), return_book(member_id, book_id), calculate_fine
- **Input:** member_id, book_id, transaction_date
- **Output:** updates `transactions.csv`, updates availability in `books.csv`

### 4.4 Reporting & Analytics (Supporting module)
- **Functions:** generate_issue_report(date_range), overdue_list(), member_history(member_id)
- **Output:** on-screen tables and exported CSV reports

### 4.5 Validation & Utilities (Supporting)
- **Functions:** validate_ids(), atomic_write_csv(), backup_data(), logging

---

## 5. Clear Input / Output Structure
**Books (input):** `book_id, ISBN, title, author, category, total_copies, available_copies`

**Members (input):** `member_id, name, contact, email, join_date`

**Transactions (output entries):** `txn_id, book_id, member_id, action, date, due_date, return_date, fine`

Actions:
- `ADD BOOK` → appends to `books.csv`
- `ISSUE BOOK` → appends to `transactions.csv` and decrements `available_copies` in `books.csv`
- `RETURN BOOK` → updates transaction (sets `return_date`), computes fine if overdue, increments `available_copies`
- `EXPORT REPORT` → filtered CSV based on date range/member/book

---

## 6. Logical Workflow (User Interaction)
1. Librarian opens the application; system loads CSV files (creates if missing).
2. Librarian registers members and adds books (one-time setup).
3. During circulation:
   - To issue: search member → search book → click ISSUE → confirm due date → system records transaction and updates availability.
   - To return: search transaction → click RETURN → system records return_date, calculates fine if any, updates availability.
4. Librarian generates reports (daily issues, overdue list) and exports CSV for records.

---

## 7. Non-Functional Requirements (≥4)
1. **Usability:** Simple GUI (Tkinter) with clear buttons and dialogs; common tasks ≤3 clicks.
2. **Reliability:** Atomic CSV writes and daily backups to prevent data loss.
3. **Performance:** Handle up to 2000 books and 2000 members; typical operations (search, issue, return) complete within 1 second.
4. **Maintainability:** Modular code with docstrings, README, and comments; use Git for version control.
5. **Error Handling:** Graceful messages for I/O errors, invalid IDs, and duplicate entries; logging to `app.log`.
6. **Security (basic):** Input validation, avoid executing values from CSV, and optional password for librarian actions.

---

## 8. Technical Expectations & Design
### 8.1 Architecture (high level)
- **Layers:** GUI (Tkinter) ↔ Controller/Service ↔ Storage (CSV utilities) ↔ Backup/Logging

### 8.2 Data Structures & Algorithms
- Use dictionaries indexed by `book_id` and `member_id` for O(1) lookups in memory.
- Transactions processed sequentially; fine calculation uses date arithmetic.

### 8.3 Modularity & Files (≥5 modules)
Suggested project layout:
```
library_system/
├─ README.md
├─ requirements.txt
├─ run.py
├─ app/
│  ├─ __init__.py
│  ├─ gui.py
│  ├─ controller.py
│  ├─ storage.py
│  ├─ models.py
│  ├─ reports.py
│  ├─ utils.py
│  └─ tests/
│     ├─ test_storage.py
│     └─ test_controller.py
└─ data/
   ├─ books.csv
   ├─ members.csv
   ├─ transactions.csv
   └─ app.log
```

### 8.4 CSV Schema
**books.csv**
```
book_id,isbn,title,author,category,total_copies,available_copies
B001,9780140449136,The Odyssey,Homer,Classics,3,2
```

**members.csv**
```
member_id,name,contact,email,join_date
M001,Anita Sharma,9876543210,anita@example.com,2025-01-15
```

**transactions.csv**
```
txn_id,book_id,member_id,action,date,due_date,return_date,fine
T0001,B001,M001,issue,2025-11-10,2025-11-24,,0
```

---

## 9. UML and Diagrams (text versions to paste into drawing tools)
### 9.1 Use Case (actors & use cases)
- Actor: Librarian
- Use cases: Add/Edit/Delete Book, Add/Edit/Delete Member, Issue Book, Return Book, Search, Generate Reports

### 9.2 Class Diagram (key classes)
```
class Book:
  - book_id
  - isbn
  - title
  - author
  - category
  - total_copies
  - available_copies

class Member:
  - member_id
  - name
  - contact
  - email
  - join_date

class Transaction:
  - txn_id
  - book_id
  - member_id
  - action ('issue'|'return')
  - date
  - due_date
  - return_date
  - fine

class Storage:
  + load_books()
  + save_books()
  + load_members()
  + save_members()
  + append_transaction()

class Controller:
  + issue_book(book_id, member_id)
  + return_book(book_id, member_id)
  + search_books(query)
  + generate_report(filter)
```

### 9.3 Sequence Diagram (Issue book)
1. GUI -> Controller: request to issue(book_id, member_id, due_date)
2. Controller -> Storage: check book availability
3. Storage -> Controller: available? yes/no
4. Controller -> Storage: append transaction(issue) and decrement available_copies
5. Storage -> Controller: success
6. Controller -> GUI: show confirmation

---

## 10. Process Flow / Workflow Diagram (text)
1. Start app → Load CSVs (or create if missing)
2. Librarian chooses operation (Books / Members / Transactions / Reports)
3. For add/edit/delete: perform validation → update CSV
4. For issue: validate member and book → check availability → record transaction → update books.csv
5. For return: find pending issue transaction → set return_date → calculate fine → update books.csv
6. Generate reports or export CSV

---

## 11. Fine Calculation Rules (example)
- Loan period: 14 days default. Fine = ₹1 per day after due date (configurable). Fine stored in `transactions.csv`.

---

## 12. Testing & Validation Plan
- **Unit tests:** storage read/write, controller issue/return logic, fine calculations.
- **Integration tests:** full scenario: add book → add member → issue → return → check availability and transaction updated.
- **Edge cases:** issuing when `available_copies=0`, returning a non-issued book, duplicate member/book IDs, corrupted CSV headers.

---

## 13. Version Control & Deliverables
- Use Git repository with commits and a clear README containing setup and usage.
- Deliverables: source code, sample `data/` CSV files, design document (this file), test suite, presentation slides, and a demo video.

---

## 14. Timeline (2–3 weeks suggested)
- Week 1: Requirements, CSV schema, basic storage and models, add/edit/delete books & members
- Week 2: Issue/return logic, fine calculation, reporting & export, basic GUI
- Week 3: Testing, documentation, slides, final polish and demo

---

## 15. Sample Python snippets (storage & controller)
### 15.1 Atomic CSV write utility (storage.py - snippet)
```python
import csv
import os

def atomic_write_csv(path, header, rows):
    tmp = path + '.tmp'
    with open(tmp, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    os.replace(tmp, path)
```

### 15.2 Issue book logic (controller.py - snippet)
```python
from datetime import date, timedelta

def issue_book(storage, book_id, member_id, loan_days=14):
    book = storage.get_book(book_id)
    if not book:
        raise ValueError('Book not found')
    if book['available_copies'] <= 0:
        raise ValueError('No copies available')
    member = storage.get_member(member_id)
    if not member:
        raise ValueError('Member not found')
    due = date.today() + timedelta(days=loan_days)
    txn = {
        'txn_id': storage.next_txn_id(),
        'book_id': book_id,
        'member_id': member_id,
        'action': 'issue',
        'date': date.today().isoformat(),
        'due_date': due.isoformat(),
        'return_date': '',
        'fine': 0
    }
    storage.append_transaction(txn)
    book['available_copies'] -= 1
    storage.save_books()
    return txn
```

---

## 16. Report Examples (ready to export)
- Daily issues: list of `transactions` where `action=issue` and `date=YYYY-MM-DD`.
- Overdue list: `transactions` with `action=issue` and `return_date` empty and `due_date` < today.
- Member history: all transactions filtered by `member_id`.

---

## 17. GitHub Repository Requirements
A GitHub repository must contain all project files and a clear **README.md** with the following structure.

### 📄 README.md (Template)
```
# Library Management System (Python + CSV)

## 📘 Project Overview
The Library Management System is a lightweight desktop application built using Python and CSV files for data storage. It helps librarians manage books, members, issue/return operations, and generate reports without requiring a complex database or server.

## ✨ Features
- Add, edit, delete books
- Add, edit, delete members
- Issue and return books
- Track due dates and fines
- Search books and members
- Generate daily and monthly reports
- Export reports as CSV
- Simple GUI using Tkinter
- Clean, modular Python code

## 🛠️ Technologies / Tools Used
- Python 3.x
- Tkinter (GUI)
- CSV (as database storage)
- Dataclasses (for models)
- Git (version control)
- Optional: pytest (for tests)

## 📦 Installation & Running the Project
### 1. Clone the Repository
```
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```
(If Tkinter is missing, install via OS package manager.)

### 3. Run the Application
```
python run.py
```

## 🧪 Testing Instructions
```
cd app/tests
pytest
```
- Tests include storage read/write, controller logic, and fine calculation.

## 📁 Project Structure
```
library-system/
├─ README.md
├─ run.py
├─ requirements.txt
├─ app/
│  ├─ gui.py
│  ├─ controller.py
│  ├─ storage.py
│  ├─ models.py
│  ├─ reports.py
│  ├─ utils.py
│  └─ tests/
├─ data/
│  ├─ books.csv
│  ├─ members.csv
│  └─ transactions.csv
```

## 🖼️ Screenshots (recommended)
Place screenshots in a `/screenshots` folder, for example:
- Home screen
- Book management page
- Issue/return screen
- Reports window

## 👨‍💻 Author
Your Name
Your Roll Number / Student ID
```

---

## 18. Appendices (what I can add next)
I can now add any of the following to the project document:
- Full working Python project (all modules + GUI) ready to run.
- A sample `data/` folder with 20 books and 10 members for demo.
- Unit tests using `pytest` and sample test results.
- Presentation slides (8–10) ready to download.

Tell me which appendix you want and I will attach it to this document.


## 📷 Screenshots

### **📘 Books Tab**
![Books Tab](sandbox:/mnt/data/Screenshot 2025-11-18 115940.png)

### **👥 Members Tab**
![Members Tab](sandbox:/mnt/data/Screenshot 2025-11-18 120026.png)

### **🔁 Transactions Tab**
![Transactions Tab](sandbox:/mnt/data/Screenshot 2025-11-18 120105.png)
