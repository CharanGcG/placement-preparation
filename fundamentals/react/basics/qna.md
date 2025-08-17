# Top 15 React.js Interview Questions & Answers

---

Below is a structured list of the **top 15 basic interview questions about React.js**. These questions target foundational knowledge and conceptual clarity, ensuring candidates grasp essential principles that underpin all React development.

---

## 1. What is React.js and why is it used?
**Detailed Answer:**  
React.js is an open-source JavaScript library for building user interfaces, particularly single-page applications where you need a fast, interactive experience. It allows developers to create reusable UI components and efficiently update the DOM (Document Object Model) when data changes.  
**Why the Interviewer Asks This:**  
To assess if the candidate has a basic conceptual understanding of React.js and its core purpose. Many confuse React with a framework, or don’t realize it’s primarily for UI building, which is a fundamental flaw.

---

## 2. What is a component in React?
**Detailed Answer:**  
In React, a component is an independent, reusable piece of UI defined as a JavaScript function or class. Each component can maintain its own state and accepts inputs called "props". Components are the building blocks of any React application.  
**Why the Interviewer Asks This:**  
To ensure the candidate understands the core building block of a React app. A common misconception is treating components as simply functions, without recognizing their self-contained logic and state.

---

## 3. Explain the difference between props and state in React.
**Detailed Answer:**  
Props are inputs to a component, passed from parent to child, and are read-only. State is managed internally by the component and can change over time. Modifying state triggers a re-render, while props are external and immutable within the component.  
**Why the Interviewer Asks This:**  
To distinguish between internal vs. external data management in React. Many freshers confuse props and state or think both can be changed within a component.

---

## 4. What is JSX?
**Detailed Answer:**  
JSX (JavaScript XML) is a syntax extension for JavaScript used in React to describe what the UI should look like. It lets you write HTML-like code within JavaScript, which then gets transpiled into regular JavaScript objects by tools like Babel.  
**Why the Interviewer Asks This:**  
Checks if the candidate understands why their React code looks like HTML but isn’t HTML. A common pitfall is confusing JSX with raw HTML.

---

## 5. Can you return multiple elements from a React component? How?
**Detailed Answer:**  
Yes, you can return multiple elements in React by wrapping them inside a parent element like a `<div>` or using React.Fragment (`<>...</>`), which doesn’t add extra nodes to the DOM.
```jsx
return (
  <>
    <h1>Title</h1>
    <p>Description</p>
  </>
);
```
**Why the Interviewer Asks This:**  
This checks the candidate’s practical knowledge of React’s render rules. Common misconception: trying to return two elements side by side without a parent.

---

## 6. What is the virtual DOM and how does React use it?
**Detailed Answer:**  
The virtual DOM is a lightweight copy of the actual DOM kept in memory. React updates the virtual DOM first, then efficiently updates only the changed parts of the actual DOM using a diffing algorithm, improving performance.  
**Why the Interviewer Asks This:**  
Ensures understanding of React’s performance optimization. Many candidates think React manipulates the real DOM directly, which is not true.

---

## 7. How do you handle events in React?
**Detailed Answer:**  
React handles events similarly to HTML but uses camelCase syntax and passes functions instead of strings. For example:
```jsx
<button onClick={() => alert('Clicked!')}>Click me</button>
```
**Why the Interviewer Asks This:**  
Tests if the candidate can use interactivity in React and spots misconceptions like using lowercase event names (`onclick` instead of `onClick`).

---

## 8. What is a controlled component in React?
**Detailed Answer:**  
A controlled component is an input form element whose value is controlled by React state. The input’s value is set via state, and every change is handled by an event handler that updates the state.
```jsx
const [value, setValue] = useState('');
<input value={value} onChange={e => setValue(e.target.value)} />
```
**Why the Interviewer Asks This:**  
To check understanding of form management. Common error: mixing uncontrolled and controlled components, leading to unpredictable UI.

---

## 9. How do you update state in React? Why shouldn’t you mutate state directly?
**Detailed Answer:**  
Use the `setState` method in class components or `setX` from `useState` in functional components to update state. You should not mutate state directly because it can lead to unexpected UI behavior and bugs; React uses state immutability to detect changes for re-rendering.
**Why the Interviewer Asks This:**  
To check knowledge of React’s state update mechanism and consequences of direct mutation. Many beginners do `state.value = x` instead of using setState.

---

## 10. Describe the React component lifecycle.
**Detailed Answer:**  
React components have lifecycle methods, such as `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` for class components. With functional components, similar effects can be handled with the `useEffect` hook.
```jsx
useEffect(() => {
  // code runs on mount and update
  return () => {
    // runs on unmount
  };
}, []);
```
**Why the Interviewer Asks This:**  
To test understanding of when and where to run side-effects. Many forget about cleanup or run code at the wrong stage.

---

## 11. What are hooks in React? Name a few commonly used ones.
**Detailed Answer:**  
Hooks are special functions introduced in React 16.8 that let you manage state and side-effects in functional components. Common hooks include `useState`, `useEffect`, `useContext`, `useReducer`, and `useRef`.
**Why the Interviewer Asks This:**  
Confirms up-to-date knowledge of modern React. Misconception: Hooks can only be used in class components (they can’t).

---

## 12. How does React handle conditional rendering?
**Detailed Answer:**  
You can render components or elements conditionally using JavaScript operators like if-else, logical `&&`, or ternary (`?`) within JSX.
```jsx
{isLoggedIn ? <Dashboard /> : <Login />}
```
**Why the Interviewer Asks This:**  
Checks ability to dynamically display UI. Some mistakenly try to use HTML-only methods.

---

## 13. How do you pass data from a child component to a parent component?
**Detailed Answer:**  
By passing a function from the parent to the child as a prop. The child calls this function with its data, and the parent receives it.
```jsx
// Parent
<Child onSubmit={handleSubmit} />

// Child
props.onSubmit(childData);
```
**Why the Interviewer Asks This:**  
Checks understanding of data flow in React (unidirectional). Beginners often try to pass props directly from child to parent, which is not possible.

---

## 14. What is the significance of keys in React lists?
**Detailed Answer:**  
Keys help React identify which items have changed, are added, or removed. They should be unique and stable for each list item. Using indexes as keys can cause bugs if the list changes order.
```jsx
{items.map(item => <li key={item.id}>{item.name}</li>)}
```
**Why the Interviewer Asks This:**  
Ensures understanding of performance and correctness. Many use array indexes as keys, which can lead to rendering bugs.

---

## 15. What is the Context API in React and when should you use it?
**Detailed Answer:**  
The Context API allows you to share values like themes or user data across the component tree without passing props down manually at every level. You use it when multiple components at different levels need access to the same data.
```jsx
const ThemeContext = React.createContext('light');

<ThemeContext.Provider value="dark">
  <App />
</ThemeContext.Provider>
```
**Why the Interviewer Asks This:**  
To check for awareness of state management across deeply nested components. Pitfall: Misusing context for all state management, leading to unnecessary re-renders.

---

These fifteen questions target foundational knowledge and conceptual clarity in React.js, ensuring candidates grasp essential principles that underpin all React development. Common misconceptions and practical code examples are included to reinforce understanding.