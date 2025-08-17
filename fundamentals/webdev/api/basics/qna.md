# Top 10 API Interview Questions & Answers

---

1. **What is an API?**  
   **Detailed Answer:**  
   An API (Application Programming Interface) is a set of rules and protocols that allows one software application to communicate or interact with another. It defines how requests are made, the data formats, and the conventions for exchanging information.  
   **Why the Interviewer Asks This:**  
   To check the candidate's basic understanding of the term and concept, as it is foundational for any API-related role.  
   **Common Misconceptions:**  
   - Believing APIs are only used for web or HTTP requests—they exist in many software layers.

---

2. **What is the difference between REST API and SOAP API?**  
   **Detailed Answer:**  
   REST (Representational State Transfer) is an architectural style that uses HTTP protocols for communication and supports multiple data formats like JSON, XML. SOAP (Simple Object Access Protocol) is a protocol that only uses XML and defines strict standards for messaging security and transaction.  
   **Why the Interviewer Asks This:**  
   To test if you understand popular API paradigms and their trade-offs.  
   **Common Misconceptions:**  
   - Assuming REST is always better; SOAP is preferred for strict contracts and security.

---

3. **What is CRUD in the context of APIs?**  
   **Detailed Answer:**  
   CRUD stands for Create, Read, Update, Delete—the four basic operations an API typically allows on resources (data/entities).  
   **Why the Interviewer Asks This:**  
   To evaluate your understanding of how APIs manage data and the basic functionality all practical APIs should expose.  
   **Common Misconceptions:**  
   - Thinking APIs only allow data retrieval (Read).

---

4. **Explain the different HTTP methods commonly used in APIs.**  
   **Detailed Answer:**  
   The most common methods are:  
   - **GET:** Retrieve data.  
   - **POST:** Create new data.  
   - **PUT/PATCH:** Update existing data.  
   - **DELETE:** Remove data.  
   **Why the Interviewer Asks This:**  
   To check if the candidate knows how APIs instruct servers to perform actions.  
   **Common Misconceptions:**  
   - Mixing up POST and PUT use-cases or thinking GET can change data.

---

5. **What is an API endpoint?**  
   **Detailed Answer:**  
   An endpoint is a specific URL or URI that an API exposes for a particular function (such as `/users` for user data). It represents where requests are sent to access resources.  
   **Why the Interviewer Asks This:**  
   To test knowledge of the basic structure of API calls.  
   **Common Misconceptions:**  
   - Thinking endpoints are only for GET requests.

---

6. **How do API authentication and authorization differ?**  
   **Detailed Answer:**  
   Authentication verifies who the user/application is (identity), while authorization determines what permissions that entity has to access resources. Common methods involve API keys, bearer tokens, OAuth.  
   **Why the Interviewer Asks This:**  
   To assess security awareness—a critical element in API design.  
   **Common Misconceptions:**  
   - Believing authentication alone grants all access.

---

7. **What is status code 200, and what does it signify in API responses?**  
   **Detailed Answer:**  
   Status code 200 means the request was successful; the server processed it as expected.  
   **Why the Interviewer Asks This:**  
   To confirm the candidate can interpret API replies, especially success and error states.  
   **Common Misconceptions:**  
   - Equating all 2xx codes to success regardless of specific API behavior.

---

8. **What is API testing, and why is it important?**  
   **Detailed Answer:**  
   API testing is the process of verifying whether API endpoints work as intended—checking their reliability, security, and performance without needing a graphical user interface.  
   **Why the Interviewer Asks This:**  
   To see if you can apply theory to practice and ensure robust API development.  
   **Common Misconceptions:**  
   - Assuming API bugs only appear in the GUI, while backend behaviors matter most.

---

9. **Give an example of an API request and response.**  
   **Detailed Answer:**  
   **Request (GET):**  
   ```
   GET /users/1 HTTP/1.1
   Host: example.com
   ```
   **Response:**  
   ```json
   {
     "id": 1,
     "name": "Alice",
     "email": "alice@example.com"
   }
   ```
   **Why the Interviewer Asks This:**  
   To see if you can practically explain the flow and format of API calls.  
   **Common Misconceptions:**  
   - Skipping headers, not understanding response codes or formats.

---

10. **What is versioning in APIs and why is it important?**  
    **Detailed Answer:**  
    Versioning lets developers update APIs (adding/removing features) without breaking existing client integrations. Usually expressed as a path (`/api/v1/resource`) or via headers.  
    **Why the Interviewer Asks This:**  
    To test understanding of good maintenance and backward compatibility practices.  
    **Common Misconceptions:**  
    - Not considering updates, leading to broken apps for users when APIs change.

---

These ten questions cover the most critical, “make-or-break” basics expected in API interviews. Not answering them well is a strong signal of insufficient foundational API knowledge.

---

### References

[1] https://www.zoho.com/qengine/know/api-testing-interview-questions.html  
[2] https://www.indeed.com/career-advice/interviewing/api-interview-questions  
[3] https://www.wecreateproblems.com/interview-questions/rest-api-interview-questions  
[4] https://www.geeksforgeeks.org/software-testing/api-testing-interview-questions/  
[5] https://katalon.com/resources-center/blog/web-api-testing-interview-questions  
[6] https://www.interviewbit.com/rest-api-interview-questions/  
[7] https://www.simplilearn.com/top-api-testing-interview-questions-article  
[8] https://www.simplilearn.com/rest-api-interview-questions-answers-article  
[9] https://grotechminds.com/wp-content/uploads/2024/12/APITestingInterviewQuestions.pdf  
[10] https://www.turing.com/interview-questions/rest-api