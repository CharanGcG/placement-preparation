# Coding Round Experience

Two questions were given on two sheets. I had to solve the problems while discussing with the interviewer.

***

## Question 1

We have a dictionary `placeholders`, where each key is a placeholder. The value can either contain a direct value or can contain other placeholders. We need to find the final output of a template using the placeholders.

Example:  
- `"BRAND" : "Nike"`  // direct value  
- `"SHOE" : "$BRAND$ 's $SHOE_NAME$"` // contains other placeholders  

I understood from the problem statement that we need to use recursion, but I got confused and started using find-union, which was not right. The interviewer told me to move to the next question and then come back to it.

When I came back at last, I understood that this was similar to TFCS (Theoretical Foundations of Computations), where a symbol can give rise to either a final value or another symbol, so we need to use DFS to decode each placeholder. He told me my answer was correct; DFS was the expected answer.

***

## Question 2

Implement a category manager with these functions:  
- `addCategory(path, categoryId)`: Suppose the path `"/sneakers/nike/black"` is to be added, we can only add it if `"/sneakers/nike"` was already a category; else, we need to return `False`.  
- `getCategoryId(path)`: Return the category id for the given path.

I used a class `CategoryManager`. For the data structure, I used a dictionary to store `(w1, w2, ..., wn) : category id`, where `w1, w2, ..., wn` were the individual categories. I split them based on the `'/'` and made that tuple as a standalone category, so to check if the parent has a category, we only need to check if that tuple key is present or not.

***

Done!