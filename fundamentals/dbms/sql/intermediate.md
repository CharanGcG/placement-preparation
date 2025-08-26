# 📗 Intermediate SQL Notes – Complete One-Stop Revision  

***

## 1. Advanced Joins

### SELF JOIN  
- **Definition:** A table joined with itself.  
- **Explanation:** Useful when rows in the same table need comparison (e.g., employees with their managers).  
- **Example:**  
```sql
SELECT E1.Name AS Employee, E2.Name AS Manager
FROM Employees E1
JOIN Employees E2 ON E1.ManagerID = E2.EmployeeID;
```
👉 Matches employees with their managers from the same table.  

- **Pitfall:** Always use aliases to distinguish the same table.  

***

### CROSS JOIN  
- **Definition:** Cartesian product of two tables (all possible combinations).  
- **Explanation:** Rarely used, but useful for combinations (e.g., seat allocation, test datasets).  
- **Example:**  
```sql
SELECT S.Name, C.Course
FROM Students S
CROSS JOIN Courses C;
```
👉 Every student paired with every course.  

***

### NATURAL JOIN  
- **Definition:** Join automatically based on columns with the same names.  
- **Pitfall:** **Avoid in production** — too implicit, can break if schema changes.  
- **Example:**  
```sql
SELECT * FROM Students NATURAL JOIN Courses;
```

***

## 2. Advanced Subqueries  

### Correlated Subquery  
- **Definition:** Subquery that depends on a value from the outer query.  
- **Example:**  
```sql
SELECT Name, Age
FROM Students S
WHERE Age > (SELECT AVG(Age) FROM Students WHERE ClassID = S.ClassID);
```
👉 For each student, it checks avg age in their class.  

- **Pitfall:** Can be **slow** due to repeated evaluations.  

***

### EXISTS vs IN  
- **`IN`:** Checks if a value exists in a set.  
- **`EXISTS`:** Checks if subquery returns rows (more efficient in correlated situations).  

Example:  
```sql
-- Using IN
SELECT Name FROM Students WHERE StudentID IN (SELECT StudentID FROM Enrollments);

-- Using EXISTS
SELECT Name FROM Students S
WHERE EXISTS (SELECT 1 FROM Enrollments E WHERE E.StudentID = S.StudentID);
```

👉 Use `EXISTS` when subquery is large with filters; `IN` is fine for small/static sets.  

***

## 3. Window Functions  

- **Definition:** Functions that perform calculations **across a set of rows** related to the current row **without collapsing rows like GROUP BY**.  
- **Key Functions:**  
  - `ROW_NUMBER()`
  - `RANK()`
  - `DENSE_RANK()`
  - `LEAD()` / `LAG()`
  
- **Syntax:**  
```sql
SELECT Name, Age,
       ROW_NUMBER() OVER (PARTITION BY ClassID ORDER BY Age DESC) AS RowNum,
       RANK() OVER (PARTITION BY ClassID ORDER BY Age DESC) AS Rank,
       LAG(Age, 1) OVER (ORDER BY Age) AS Prev_Age
FROM Students;
```

👉 Gives row numbers, ranks within groups, and previous ages.  

- **Common Pitfall:** Beginners confuse **GROUP BY** (aggregates + collapses rows) with **WINDOW FUNCTIONS** (preserve all rows + add extra columns).  

***

## 4. Common Table Expressions (CTEs)  

### Non-Recursive CTE  
```sql
WITH TopStudents AS (
  SELECT Name, Age FROM Students WHERE Age > 20
)
SELECT * FROM TopStudents WHERE Name LIKE 'A%';
```

### Recursive CTE  
- Used for hierarchical data (e.g., employee reporting tree).  
```sql
WITH RECURSIVE OrgChart AS (
   SELECT EmployeeID, ManagerID, Name, 1 AS Level
   FROM Employees WHERE ManagerID IS NULL
   UNION ALL
   SELECT E.EmployeeID, E.ManagerID, E.Name, O.Level + 1
   FROM Employees E
   INNER JOIN OrgChart O ON E.ManagerID = O.EmployeeID
)
SELECT * FROM OrgChart;
```

***

## 5. Stored Procedures & Functions  

- **Stored Procedure:** Precompiled SQL code that performs actions.  
```sql
CREATE PROCEDURE GetStudentCount()
BEGIN
  SELECT COUNT(*) FROM Students;
END;
```
- **Function:** Returns a single value.  
```sql
CREATE FUNCTION GetTotalCourses(student_id INT)
RETURNS INT
RETURN (SELECT COUNT(*) FROM Enrollments WHERE StudentID = student_id);
```
👉 Use **procedures for actions**, **functions for returning a value**.  

***

## 6. Triggers  

- **Definition:** Code that executes automatically in response to `INSERT`, `UPDATE`, `DELETE`.  
- **Example:**  
```sql
CREATE TRIGGER BeforeInsertStudents
BEFORE INSERT ON Students
FOR EACH ROW
SET NEW.CreatedAt = NOW();
```
👉 Automatically sets `CreatedAt` timestamp before insert.  

- **Use case:** Auditing, enforcing business rules.  
- **Pitfall:** Complex triggers can be hard to debug.  

***

## 7. Views (Normal vs Materialized)

- **Normal View:** Saved query; always fetches fresh data.  
- **Materialized View:** Stores physical data snapshot (needs refresh).  

Example:
```sql
CREATE VIEW YouthView AS
SELECT Name, Age FROM Students WHERE Age < 25;

-- Materialized (Postgres/Oracle)
CREATE MATERIALIZED VIEW SalesSummary AS
SELECT ProductID, SUM(Amount) FROM Sales GROUP BY ProductID;
```

***

## 8. Indexing  

- **Clustered Index:** Data physically stored in index order (only one per table).  
- **Non-Clustered Index:** Separate structure pointing to data rows.  

Example:  
```sql
CREATE INDEX idx_student_name ON Students(Name);
```

👉 Speeds up reads, but slows writes.  
- **B-Tree basics:** Balanced tree for logarithmic search.  

***

## 9. Query Optimization  

- **EXPLAIN / EXPLAIN ANALYZE:** Shows execution plan.  
```sql
EXPLAIN SELECT * FROM Students WHERE Age > 18;
```
👉 Helps detect full table scans, missing indexes, etc.  

***

## 10. Transactions & Concurrency  

- **ACID:** Atomicity, Consistency, Isolation, Durability.  
- **Isolation Levels:**  
  - READ UNCOMMITTED → Dirty reads allowed  
  - READ COMMITTED → Prevents dirty reads  
  - REPEATABLE READ → Prevents dirty & non-repeatable reads  
  - SERIALIZABLE → Full isolation (safest but slowest)  

***

## 11. Locks  

- **Shared lock (S):** Read-only, multiple allowed.  
- **Exclusive lock (X):** Write access, blocks others.  
- **Deadlock:** Two transactions hold locks that block each other → resolved by DB killing one.  

***

## 12. Error Handling in SQL  

- **TRY … CATCH** (SQL Server) or `EXCEPTION` blocks (PL/SQL).  
```sql
BEGIN TRY
   INSERT INTO Students VALUES (1, 'Alice', 20);
END TRY
BEGIN CATCH
   PRINT 'Error inserting record';
END CATCH;
```

***

## 13. Security Basics  

- **GRANT / REVOKE permissions:**  
```sql
GRANT SELECT, INSERT ON Students TO UserA;
REVOKE INSERT ON Students FROM UserA;
```

- Use **roles** for grouped permissions.  

***

## 14. SQL vs Procedural Code  

- **SQL is declarative** (you say *what* you want).  
- **Procedural code is imperative** (you say *how* step by step).  
👉 If task is set-based (aggregate, mass update) → SQL is best.  
👉 If involves loops/complex logic → procedural code (Python, Java, PL/pgSQL).  

***

# 📌 Intermediate SQL Cheat Sheet  

| Concept              | Key Syntax / Example | Quick Recall Point |
|----------------------|----------------------|--------------------|
| SELF JOIN            | `FROM Emp E1 JOIN Emp E2 ON...` | Compare rows in same table |
| CROSS JOIN           | `SELECT * FROM A CROSS JOIN B` | All combinations |
| NATURAL JOIN         | `SELECT * FROM A NATURAL JOIN B` | Uses common column names (avoid in prod) |
| Correlated Subquery  | `Age > (SELECT AVG(Age) WHERE ClassID=S.ClassID)` | Subquery depends on outer row |
| EXISTS vs IN         | `WHERE EXISTS (subquery)` | EXISTS better for large sets |
| Window Function      | `ROW_NUMBER() OVER(PARTITION BY...)` | Adds ranks/analytics without reducing rows |
| CTE                  | `WITH cte AS (...) SELECT * FROM cte` | Temporary named result set |
| Recursive CTE        | `WITH RECURSIVE ... UNION ALL ...` | For hierarchies |
| Stored Procedure     | `CREATE PROCEDURE proc()` | Precompiled actions |
| Function             | `CREATE FUNCTION fn() RETURNS ...` | Returns value |
| Trigger              | `CREATE TRIGGER ...` | Auto-action on DML |
| View                 | `CREATE VIEW v AS ...` | Saved query |
| Materialized View    | `CREATE MATERIALIZED VIEW ...` | Cached snapshot |
| Index                | `CREATE INDEX idx ON table(col)` | Faster reads, slower writes |
| EXPLAIN              | `EXPLAIN SELECT ...` | Show query plan |
| Transaction          | `BEGIN ... COMMIT` | ACID operations |
| Isolation Levels     | READ COMMITTED, SERIALIZABLE, etc. | Tradeoff perf vs safety |
| Locks                | Shared (read) / Exclusive (write) | Deadlocks possible |
| Error Handling       | TRY...CATCH / EXCEPTION | Capture DB errors |
| Security             | `GRANT SELECT ON ... TO user` | Control permissions |
| SQL vs Procedural    | Declarative vs Imperative | Use SQL for sets, code for logic |

***

✅ These notes cover **interview-depth intermediate SQL** concepts, with **pitfalls + examples + use-cases**.   

***
