# Written Round Experience

15 MCQs, 3 coding questions, 1 hour, pen and paper, no laptops

***

## MCQs

- Computer networks  
- Python code – predict output (classes, try-catch)  
- SQL – indexing  
- MongoDB – when to use  
- ML model performance metrics  
- Tree used to implement first Bitcoin paper – Merkle tree  
- Similarly there were others

***

## Coding Questions

1. **You have n hubs; a seller comes in with some initial number of boxes, the promo is applied and it gets doubled, but he leaves a few fixed number of boxes at every hub. At the nth hub, the seller will be left with 0 boxes. Write a program to find the initial number of boxes** – I don’t know if this is the right interpretation of their phrasing of the question. I couldn’t answer this one, so I moved on to the next question.

2. **Implement a customer manager with three functions:**  
   - `addAmountSpent(customerId, amount)` – adds amount to the total amount of the customer  
   - `topK(k)` – retrieves the top k customers with highest amount spent  
   - `reset(customerId)` – resets amount to 0  
   I used a dictionary to store `customerId : amount` and a priority queue to store the amount in sorted order, so that the `topK` function can retrieve from the priority queue.

3. **Find the edge that causes the cycle in a graph where an edge is added to the graph incrementally**  
   As soon as I saw the figure and the terms “cycle” and “edges”, find-union came into my mind. I remembered learning about them in advanced data structures class, so I implemented the find-union data structure and detected the cycle.

***

I believe I had answered most of the MCQs correctly. I had written correct code implementations for the 2nd (10 marks) and 3rd (20 marks) coding questions, so I got shortlisted for the second round, which was a pure coding round.