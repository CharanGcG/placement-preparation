# Top 10 Node.js Interview Questions & Answers

---

1. **What is Node.js and where is it used?**  
   **Detailed Answer:**  
   Node.js is an open-source, cross-platform JavaScript runtime environment that allows you to run JavaScript code on the server side, outside of a web browser. It is used for building scalable network applications, handling I/O-intensive tasks, real-time web applications, APIs, and more.  
   **Why the Interviewer Asks This:**  
   To confirm the candidate knows what Node.js is fundamentally and its use cases. Common misconception: some think Node.js is a library or only for web servers, not realizing it’s a runtime environment.

---

2. **How does the Node.js event-driven architecture work?**  
   **Detailed Answer:**  
   Node.js uses an event-driven, non-blocking I/O model. Incoming requests are placed in an event queue, and the Event Loop processes each request, delegating blocking tasks to a thread pool as needed, thus allowing efficient handling of many connections at once.  
   **Why the Interviewer Asks This:**  
   To check if the candidate understands one of Node.js’s core differentiators. Many confuse event-driven with multi-threaded models or think everything runs in parallel.

---

3. **What is the difference between synchronous and asynchronous programming in Node.js?**  
   **Detailed Answer:**  
   Synchronous code blocks the execution until the current operation completes, while asynchronous code allows other operations to continue while the current task completes in the background, often using callbacks, promises, or async/await. Node.js emphasizes asynchronous programming for performance.  
   **Why the Interviewer Asks This:**  
   To identify understanding of how Node.js handles concurrency and performance. Mistaking Node.js for purely synchronous or not understanding callbacks is a red flag.

---

4. **Explain what the Event Loop is in Node.js.**  
   **Detailed Answer:**  
   The Event Loop is the mechanism in Node.js that processes incoming events and executes callback functions. It continuously checks the event queue and processes events, allowing Node.js to perform non-blocking I/O even though it runs on a single thread.  
   **Why the Interviewer Asks This:**  
   To make sure the candidate understands the inner mechanism that enables non-blocking behavior. Some confuse this with multi-threading or are unaware of its role.

---

5. **What are modules in Node.js and how do you use them?**  
   **Detailed Answer:**  
   Modules in Node.js are reusable pieces of code that can be included in other files using `require()`. Examples include built-in modules like `fs`, `http`, and custom modules. They help in organizing code and reusing functionality.  
   **Why the Interviewer Asks This:**  
   To assess if the candidate understands Node.js code structuring and use of built-in functionality. Some candidates don’t know how to create or use a module properly.

---

6. **What is npm, and why is it important in Node.js projects?**  
   **Detailed Answer:**  
   npm (Node Package Manager) is the default package manager for Node.js. It allows developers to install, manage, and share libraries (packages) necessary for Node.js projects, using a package.json file to track dependencies.  
   **Why the Interviewer Asks This:**  
   To check for understanding of how dependencies are managed in Node.js. Common misconception: thinking npm is only needed for big projects, or not knowing about package.json.

---

7. **How do you create a simple HTTP server in Node.js?**  
   **Detailed Answer:**  
   You can use the built-in `http` module to create a server:
   ```js
   const http = require('http');
   http.createServer((req, res) => {
     res.writeHead(200, {'Content-Type': 'text/plain'});
     res.end('Hello World\n');
   }).listen(3000);
   ```
   **Why the Interviewer Asks This:**  
   To confirm practical knowledge of core modules and basic server setup. Not knowing this suggests lack of basic hands-on experience.

---

8. **What is callback hell and how can it be avoided?**  
   **Detailed Answer:**  
   Callback hell refers to deeply nested callbacks that make code hard to read and maintain. It can be avoided using named functions, modularizing code, using Promises, or async/await for better readability and error handling.
   ```js
   // Using async/await instead of nested callbacks
   async function example() {
      const data = await someAsyncFunction();
   }
   ```
   **Why the Interviewer Asks This:**  
   To probe understanding of asynchronous patterns and code maintainability. Some think callbacks are the only way to handle async tasks in Node.js.

---

9. **What are streams in Node.js? Name a use case.**  
   **Detailed Answer:**  
   Streams are objects that let you read or write data piece by piece (chunks) instead of all at once. Types include Readable, Writable, Duplex, and Transform streams. Use case: reading/writing large files, data transfer over HTTP.
   **Why the Interviewer Asks This:**  
   Ensures familiarity with handling large data efficiently and not loading everything into memory. A common error is ignoring streams for large files, leading to memory issues.

---

10. **What is the purpose of the Buffer class in Node.js?**  
    **Detailed Answer:**  
    The Buffer class handles binary data directly, allocating raw memory outside the V8 heap. It’s essential when working with TCP streams, file I/O, or any situation where binary data must be handled efficiently.
    ```js
    const buf = Buffer.from('abc'); // creates a buffer from a string
    ```
    **Why the Interviewer Asks This:**  
    To ensure candidate understands binary data handling in Node.js. Misconception: thinking all data in Node.js is string or JSON; not knowing about buffers is a critical gap.

---

This set ensures candidates have a fundamental, practical understanding of Node.js, including crucial concepts and their real-world applications, as well as common misconceptions and technical pitfalls.

---

### References

[1] https://www.interviewbit.com/node-js-interview-questions/  
[2] https://www.simplilearn.com/tutorials/nodejs-tutorial/nodejs-interview-questions  
[3] https://www.youtube.com/watch?v=ruwx8R2nXyI  
[4] https://www.akalinfo.com/blog/node-js-interview-questions/  
[5] https://zerotomastery.io/blog/node-js-interview-questions/  
[6] https://www.geeksforgeeks.org/node-js/node-interview-questions-and-answers/  
[7] https://www.javacodegeeks.com/2024/08/15-essential-node-js-interview-questions.html  
[8] https://www.greatfrontend.com/blog/50-must-know-javascript-interview-questions-by-ex-interviewers  
[9] https://essinstitute.in/top-25-node-js-interview-questions-for-freshers/  
[10] https://gist.github.com/paulfranco/9f88a2879b7b7d88de5d1921aef2093b