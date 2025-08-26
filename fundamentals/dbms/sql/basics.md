# 📘 SQL Beginner Notes – One-Stop Revision Guide  

***

## 1. Introduction to SQL & Databases
- **Definition:**  
SQL (Structured Query Language) is the standard language used to interact with relational databases.  
- **Explanation:**  
It allows you to create tables, insert data, query (fetch) data, update records, and manage database structure.  
- **Analogy:** Think of a **database as a library**, tables as **bookshelves**, rows as **entries in a book**, and SQL as the **librarian language** to fetch/organize/update books.  

Example:  
```sql
-- Select all data from a table called Students
SELECT * FROM Students;
```
This fetches every row and column from the `Students` table.

***

## 2. SQL Data Types
- **Definition:** Types of values that can be stored in a table column.  
- **Common Types:**  
  - `INT` → integers (1, 100)  
  - `DECIMAL(p,s)` → fixed-point numbers (12.34)  
  - `VARCHAR(n)` → strings of variable length ("Alice")  
  - `CHAR(n)` → fixed-length strings ("A")  
  - `DATE`, `TIME`, `DATETIME` → date/time values  
  - `BOOLEAN` → TRUE/FALSE  

***

## 3. DDL Commands: CREATE, DROP, ALTER  
DDL (**Data Definition Language**) → defines database structure  

### CREATE
```sql
CREATE TABLE Students (
  StudentID INT PRIMARY KEY,
  Name VARCHAR(50),
  Age INT
);
```
👉 Creates a table named `Students`.

### ALTER
```sql
ALTER TABLE Students ADD Email VARCHAR(100);
```
👉 Adds a new column `Email`.

### DROP
```sql
DROP TABLE Students;
```
👉 Deletes the table permanently.

***

## 4. DML Commands: INSERT, UPDATE, DELETE  
DML (**Data Manipulation Language**) → modifies data  

### INSERT
```sql
INSERT INTO Students (StudentID, Name, Age)
VALUES (1, 'Alice', 20);
```

### UPDATE
```sql
UPDATE Students SET Age = 21 WHERE StudentID = 1;
```

### DELETE
```sql
DELETE FROM Students WHERE StudentID = 1;
```

***

## 5. SELECT Basics (Projection, Filtering, Sorting)
**Projection = selecting columns**, **Filtering = WHERE condition**, **Sorting = ORDER BY**.  

```sql
SELECT Name, Age FROM Students WHERE Age > 18 ORDER BY Age DESC;
```
👉 Fetch `Name` & `Age` for students above 18, sorted by Age (highest first).

***

## 6. WHERE, DISTINCT, ORDER BY, LIMIT
- **WHERE** → filters rows  
- **DISTINCT** → removes duplicates  
- **ORDER BY** → sorts results  
- **LIMIT n** → restricts row count  

Example:
```sql
SELECT DISTINCT Age FROM Students
WHERE Age >= 18
ORDER BY Age ASC
LIMIT 5;
```

***

## 7. Aggregate Functions (COUNT, SUM, AVG, MIN, MAX)
Used for summaries.  

```sql
SELECT COUNT(*) AS TotalStudents, AVG(Age) AS AvgAge
FROM Students;
```
👉 Returns number of students and their average age.

***

## 8. GROUP BY and HAVING
- **GROUP BY** → groups rows based on column(s).  
- **HAVING** → like WHERE but applied after grouping.  

```sql
SELECT Age, COUNT(*) AS CountPerAge
FROM Students
GROUP BY Age
HAVING COUNT(*) > 1;
```
👉 Finds age groups where more than 1 student exists.

***

## 9. Joins (Combining Multiple Tables)

- **INNER JOIN** → common records only  
- **LEFT JOIN** → all left + matching right  
- **RIGHT JOIN** → all right + matching left  
- **FULL JOIN** → all records from both  

Example:
```sql
SELECT S.Name, C.CourseName
FROM Students S
INNER JOIN Courses C
ON S.StudentID = C.StudentID;
```
👉 Shows students with enrolled courses.  

*(Think of JOINs like overlapping circles in a Venn diagram.)*

***

## 10. Subqueries and Nested Queries
A query inside another query.  

```sql
SELECT Name FROM Students
WHERE Age > (SELECT AVG(Age) FROM Students);
```
👉 Finds students older than average age.  

***

## 11. Constraints
Rules applied to table columns.  
- **PRIMARY KEY** → uniquely identifies row  
- **FOREIGN KEY** → links to another table’s primary key  
- **UNIQUE** → prevents duplicates  
- **NOT NULL** → must have a value  
- **CHECK** → enforces condition  
- **DEFAULT** → auto value if not provided  

Example:  
```sql
CREATE TABLE Orders (
  OrderID INT PRIMARY KEY,
  StudentID INT,
  Amount DECIMAL(8,2) CHECK (Amount > 0),
  FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);
```

***

## 12. Indexes and Views
- **Index:** Speeds up searching.  
```sql
CREATE INDEX idx_name ON Students(Name);
```
- **View:** Virtual table of a saved query.  
```sql
CREATE VIEW AdultStudents AS
SELECT Name, Age FROM Students WHERE Age >= 18;
```

***

## 13. Transactions (ACID)  
- **Transaction = group of SQL statements that execute together.**  
- Supports **COMMIT** (save), **ROLLBACK** (undo), **SAVEPOINT** (checkpoint).  

Example:  
```sql
BEGIN;
UPDATE Students SET Age = 22 WHERE StudentID = 1;
ROLLBACK;  -- undo
COMMIT;    -- final save
```

***

## 14. Normalization Basics
- **1NF (First Normal Form):** No repeating groups → atomic values.  
- **2NF:** In 1NF + no partial dependency on composite key.  
- **3NF:** In 2NF + no transitive dependency (non-key depends only on key).  

👉 Goal: **reduce redundancy, improve consistency**.  

***

## 15. SQL vs NoSQL (Quick Note)
- **SQL (Relational):** Structured data, fixed schema, ACID properties (MySQL, PostgreSQL).  
- **NoSQL (Non-relational):** Flexible schema, document/graph/column stores, good for scale & unstructured data (MongoDB, Cassandra).  

***

# 📌 Final SQL Cheat Sheet (Quick Revision)

| Concept           | Key Syntax / Example | Quick Recall Point |
|-------------------|----------------------|--------------------|
| SELECT            | `SELECT col FROM table;` | Fetch data |
| WHERE             | `WHERE Age > 18` | Filters rows |
| DISTINCT          | `SELECT DISTINCT Age` | Removes duplicates |
| ORDER BY          | `ORDER BY Age DESC` | Sort results |
| LIMIT             | `LIMIT 5` | Restrict rows |
| INSERT            | `INSERT INTO table VALUES(...)` | Add data |
| UPDATE            | `UPDATE table SET col=val WHERE ...` | Modify data |
| DELETE            | `DELETE FROM table WHERE ...` | Remove data |
| CREATE TABLE      | Define table structure | DDL command |
| ALTER TABLE       | Modify structure | Add/Drop column |
| DROP TABLE        | Delete table permanently | Dangerous! |
| COUNT / SUM / AVG | Aggregate functions | For summaries |
| GROUP BY + HAVING | Group rows + filter groups | Post-aggregation filter |
| JOIN              | `INNER`, `LEFT`, `RIGHT`, `FULL` | Combine tables |
| Subquery          | Query inside query | Use with conditions |
| PRIMARY KEY       | Unique row identifier | Constraint |
| FOREIGN KEY       | Link between tables | Constraint |
| INDEX             | `CREATE INDEX ...` | Speeds searches |
| VIEW              | `CREATE VIEW ...` | Saved query |
| Transaction       | `BEGIN … COMMIT/ROLLBACK` | Safe operations |
| Normalization     | 1NF → 2NF → 3NF | Reduce redundancy |

***

✅ **Best Use:** Skim the cheat sheet daily, and practice queries from examples — this is the fastest prep cycle before interviews & tests.  

***
