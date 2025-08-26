# Whatfix online assessment

It consisted of 15 questions: 13 core cs and 2 coding questions  
Platform: hackerearth, full screen mode, plagiarism detection enabled, but not webcam proctored  
Duration = 1 hour 30 minutes

---

**13 core questions:**  
based on java, c++, tree traversal, design patterns, etc

---

**2 coding questions:**

**50 mark question:**  
I have doubt in the question itself:  
You have been given n vertices numbered 0 to n-1, you have also been given a dependencies graph where (a,b) means task a depends on task b. You can have concurrent tasks up to M, and for each batch there is very negligible time cost, so if there are some x number of tasks which are independent we can complete it in one tick cycle. We need to find the minimum ticks required to complete all tasks.

*My doubt:* Even if m=2, 3 tasks which were independent were considered one tick in the example test case.

---

**20 mark question:**  
You have been given (x,y) coordinates of trees. Your task is to cut a tree such that the maximum distance between any two trees in the new set becomes minimum. The distance between two coordinates is defined as Manhattan distance:  
`manhattan(x1, y1, x2, y2) = |x1-x2| + |y1-y2|`