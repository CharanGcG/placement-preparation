***

# 📕 Advanced SQL Notes – Complete One-Stop Revision  

***

## 1. Query Optimization Deep Dive  

### Execution Plans  
- **Definition:** A breakdown of how the database executes a query.  
- **Explanation:** The optimizer evaluates multiple strategies (index scan, nested loops, hash joins) and chooses the lowest-cost plan based on CPU, I/O, and memory cost.  
- **Example:**
```sql
EXPLAIN ANALYZE
SELECT Name FROM Students WHERE Age > 25;
```
👉 Shows whether DB does an **Index Scan** (fast) or **Seq Scan** (slow).  

⚠️ **Pitfall:** Without indexes, DB falls back to full table scans → costly at scale.  

***

### Query Rewriting by Optimizer  
- SQL is declarative — optimizer transforms queries for efficiency.  
- Example:  
```sql
SELECT * FROM Students WHERE Age + 1 = 30;
```
DB may rewrite internally to:  
```sql
SELECT * FROM Students WHERE Age = 29;
```

👉 Always write **sargable queries** (Search ARGument ABLE: don’t wrap column in functions).  

***

## 2. Index Strategies  

### Covering Index  
- **Definition:** An index that stores all queried columns, avoiding table access.  
```sql
CREATE INDEX idx_cover ON Orders(CustomerID, OrderDate, Amount);
```
Query:  
```sql
SELECT CustomerID, OrderDate, Amount FROM Orders WHERE CustomerID = 5;
```
👉 Served entirely from index — "index-only scan".  

***

### Composite Index  
- **Definition:** Index on multiple columns.  
- **Rule:** Order **matters** — (A,B) can optimize filters on A or (A,B), but not B alone.  

***

### Partial Index  
- **Definition:** Index only on subset of data.  
```sql
CREATE INDEX idx_active_users ON Users(LastLogin)
WHERE Active = true;
```
👉 Saves storage, speeds up queries on "active" users only.  

***

### Bitmap Index (OLAP systems)  
- **Definition:** Index that uses bitmaps instead of trees.  
- **Usage:** Data warehouses → excellent for low-cardinality columns (e.g., gender, yes/no flags).  

***

## 3. Partitioning & Sharding  

### Partitioning  
Splits **table into pieces within same DB instance**.  
- **Horizontal partitioning (sharding-lite):** by rows (e.g., Users_US, Users_EU).  
- **Vertical partitioning:** by columns (split wide tables).  

**Types:**  
- Range (by date range: Jan, Feb, Mar tables).  
- List (region = EU, US, Asia).  
- Hash (hash of UserID → bucket tables).  

⚠️ **Tradeoff:** Partitioning improves query speed but complicates inserts/update across partitions.  

***

### Sharding  
Splits data across **multiple servers**.  
- **Strategies:**  
  - **Hash-based sharding:** `hash(UserID) mod N`  
  - **Range sharding:** ID ranges per shard  
  - **Directory-based:** Lookup service decides node  

👉 Used in **distributed SQL systems** (e.g., Spanner, Vitess).  

***

## 4. Advanced Indexing Techniques  

- **B+ Tree (default):** Balanced tree, great for range queries.  
- **Hash Index:** O(1) equality lookup, bad for ranges.  
- **Full-text Index:** For search engine–like queries in text columns.  
```sql
SELECT * FROM Articles WHERE MATCH(content) AGAINST ('database optimization');
```
- **PostgreSQL Specific:**  
  - **GIN** (Generalized Inverted Index) → text search, JSONB.  
  - **GiST** (Generalized Search Tree) → spatial queries (GIS).  
  - **BRIN** (Block Range Index) → huge sequential data (time-series).  

***

## 5. Advanced Transaction Management  

### Isolation Anomalies  
- **Dirty Read:** Read uncommitted data.  
- **Non-Repeatable Read:** Same query returns different results within a transaction.  
- **Phantom Read:** New rows appear that match condition.  

***

### MVCC (Multi-Version Concurrency Control)  
- Readers see **snapshot** of data → no blocking.  
- Writers don’t block readers.  
👉 Used by PostgreSQL, Oracle.  

***

### Deadlock Handling  
- DB detects cycles in wait-for graphs.  
- **Resolution:** kill one transaction → rollback → retry logic.  

⚠️ **Pitfall:** Always keep **locks consistent order** to reduce deadlocks.  

***

## 6. Replication & High Availability  

- **Master-Slave (Primary-Replica):** Writes go to master, reads can be offloaded to replicas.  
- **Master-Master:** Both nodes accept writes → harder conflict resolution.  

**Replication types:**  
- **Synchronous replication:** Safe, slower (wait for replica ACK).  
- **Asynchronous replication:** Fast, but risk of data loss if master fails.  

**Failover:** Auto-switch traffic to standby replica when primary dies.  

***

## 7. Advanced Stored Procedures & Triggers  

- **Stored Procedure Performance Impact:** Precompiled, reduce network round-trips.  
- **Real-world Pattern:** Audit logs — `BEFORE UPDATE` trigger storing old value in audit table.  

⚠️ Pitfall: Triggers at scale can create **hidden complexity & debugging nightmares**.  

***

## 8. Distributed SQL Concepts  

### CAP Theorem in SQL Systems  
- **C (Consistency)** — all nodes same view of data.  
- **A (Availability)** — each request gets a response.  
- **P (Partition tolerance)** — system works despite node/network failures.  

👉 Can’t have all 3 at once.  

### NewSQL Databases  
- **CockroachDB** → Postgres-compatible, scales like NoSQL.  
- **Google Spanner** → Global, synchronized clocks (TrueTime API).  

***

## 9. Security & Compliance  

- **Row-Level Security:** Restrict access row by row.  
```sql
CREATE POLICY student_policy
ON Students FOR SELECT
USING (UserID = current_user_id());
```

- **Data Masking:** Show partial sensitive data.  

- **Preventing SQL Injection:** Always use parameterized queries:  
```sql
SELECT * FROM Users WHERE email = ?;
```

- **Encryption:**  
  - At Rest → encrypted storage.  
  - In Transit → TLS for database connections.  

***

## 10. Advanced SQL Features  

### Recursive CTEs (Deep Graphs / Hierarchies)  
```sql
WITH RECURSIVE ancestors AS (
  SELECT id, parent_id FROM family WHERE id = 5
  UNION ALL
  SELECT f.id, f.parent_id FROM family f
  JOIN ancestors a ON f.id = a.parent_id
)
SELECT * FROM ancestors;
```

***

### Window Function Deep Dive  
```sql
SELECT Name,  
       NTILE(4) OVER (ORDER BY Age) AS Quartile,  
       SUM(Salary) OVER (ORDER BY HireDate ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS MovingSum  
FROM Employees;
```
👉 `NTILE` splits data into buckets, sliding frames allow moving averages.  

***

### Materialized Views  
- Auto-refresh heavy queries.  
- Great for caching aggregated results in BI/reporting.  

***

## 11. SQL in Big Data & Modern Ecosystems  

- **Hadoop/Hive:** SQL-like queries on distributed file systems.  
- **Spark SQL:** SQL on RDD/Dataframes with in-memory acceleration.  
- **Presto/Trino:** Query across **multiple data sources (federated SQL)**.  
- **BigQuery (Google):** Serverless SQL engine, columnar storage, optimized for analytics.  

***

# 📌 Advanced SQL Cheat Sheet  

| Concept                | Advanced Feature / Syntax / Example | Quick Recall Point |
|-------------------------|-------------------------------------|--------------------|
| Execution Plans         | `EXPLAIN ANALYZE SELECT...` | See DB strategy |
| Covering Index          | Index with all needed columns | Query served from index only |
| Composite Index         | `(A,B)` helps A or (A,B), not B alone | Column order matters |
| Partial Index           | `CREATE INDEX ... WHERE ...` | Index subset of rows |
| Bitmap Index            | Used in data warehouses | Good for low-cardinality |
| Partitioning            | RANGE, LIST, HASH | Faster reads, complex writes |
| Sharding                | Horizontal scaling | Split data across servers |
| B+Tree Index            | Default, range queries | General-purpose |
| Hash Index              | O(1) equality lookup | Bad for ranges |
| Full-text Index         | `MATCH() AGAINST()` | Text search |
| GIN/GiST/BRIN Index     | Postgres specialized indexes | JSONB / spatial / block |
| MVCC                    | Readers don’t block writers | Snapshot isolation |
| Isolation Levels        | READ COMMITTED → SERIALIZABLE | Tradeoff perf vs safety |
| Deadlock Handling       | DB kills one transaction | Retry logic required |
| Replication             | Master-slave / master-master | Sync = safe, Async = fast |
| Failover                | Auto-switch replica | HA system design |
| CAP Theorem             | Cannot have C, A, P all together | Tradeoff choice |
| NewSQL                  | Spanner, CockroachDB | SQL + scale |
| RLS (Row-level security)| `CREATE POLICY ...` | Fine-grained access |
| SQL Injection Defense   | Use prepared statements | Avoid string concat |
| Encryption              | At rest + In transit | Regulatory compliance |
| Recursive CTE           | `WITH RECURSIVE ...` | Hierarchical queries |
| NTILE / Sliding Frames  | `NTILE(4) OVER...` | Quartiles, moving window calc |
| Materialized Views      | Cached persisted query | Good for analytics |
| Big Data SQL            | Spark SQL, Presto, BigQuery | Federated/distributed SQL |

***

✅ This guide pulls together **all advanced SQL topics** expected in **system design + senior interviews**, with **use cases, tradeoffs, and pitfalls**.  

***
