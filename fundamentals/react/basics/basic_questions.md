# Top 10 Basic React Interview Questions (with Detailed Answers & Why They're Asked)

---

### 1. **What is React?**

**Answer:**  
React is a **JavaScript library** developed by Facebook for building **user interfaces**, especially single-page applications. It enables developers to create reusable UI components, manage the view layer efficiently, and update the UI dynamically in response to data changes. React uses a declarative approach, making code more predictable and easier to debug.

**Why it’s asked:**  
To see if you confuse React with a framework (like Angular/Vue) and to check your understanding of its core purpose.

---

### 2. **What are Components in React?**

**Answer:**  
Components are the **fundamental building blocks** of a React application. They encapsulate logic, structure, and styling, allowing you to split the UI into independent, reusable pieces.  
- **Functional Components:** Simple functions that return JSX; can use hooks for state and lifecycle.
- **Class Components:** ES6 classes that extend `React.Component`; manage state and lifecycle via methods.
Components can be nested, reused, and composed to build complex UIs.

**Why it’s asked:**  
If you can’t explain components, you don’t know React.

---

### 3. **What is JSX?**

**Answer:**  
JSX (**JavaScript XML**) is a syntax extension for JavaScript that allows you to write HTML-like code within JavaScript files. JSX makes it easier to visualize the UI structure and integrates seamlessly with React’s rendering logic. Under the hood, JSX is transpiled to `React.createElement()` calls, which create virtual DOM nodes.

**Why it’s asked:**  
Because beginners often think JSX is HTML — it’s not.

---

### 4. **What is the Virtual DOM and how does React use it?**

**Answer:**  
The **Virtual DOM** is an in-memory representation of the real DOM elements. React creates a virtual DOM tree whenever the state of a component changes. It then uses a **diffing algorithm** to compare the new virtual DOM with the previous one, identifying the minimal set of changes needed. React then efficiently updates only those parts of the real DOM, improving performance and responsiveness.

**Why it’s asked:**  
To test understanding of React’s core performance advantage.

---

### 5. **What is the difference between Props and State?**

**Answer:**  
- **Props:** Short for "properties", props are **read-only data** passed from parent to child components. They allow components to be dynamic and reusable by accepting input values.
- **State:** State is **mutable data** managed within a component. It represents information that can change over time (e.g., user input, API responses). State changes trigger re-renders of the component.
Props are for external data; state is for internal, local data.

**Why it’s asked:**  
This is the bread-and-butter of React logic.

---

### 6. **What are Hooks in React?**

**Answer:**  
**Hooks** are special functions introduced in React 16.8 that let you use state and other React features in functional components.  
- Common hooks: `useState` (state management), `useEffect` (side effects), `useContext` (context API), etc.
Hooks simplify code, eliminate the need for class components, and promote code reuse via custom hooks.

**Why it’s asked:**  
If you don’t know hooks, you’re stuck in pre-2018 React.

---

### 7. **What is `useEffect` used for?**

**Answer:**  
`useEffect` is a hook that lets you perform **side effects** in functional components, such as data fetching, subscriptions, timers, or manually changing the DOM.  
- Runs after every render by default.
- Can be controlled with a dependency array:  
  - `[]` → runs once (on mount).
  - `[dep]` → runs when `dep` changes.
It replaces lifecycle methods like `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` in class components.

**Why it’s asked:**  
It’s the most commonly misused hook.

---

### 8. **What is the difference between Controlled and Uncontrolled Components?**

**Answer:**  
- **Controlled Components:** Form elements whose values are managed by React state. Changes are handled via event handlers and state updates.
- **Uncontrolled Components:** Form elements whose values are managed by the DOM itself. You access their values using refs.
Controlled components offer more control and validation; uncontrolled components are simpler for basic use cases.

**Why it’s asked:**  
To test understanding of forms in React.

---

### 9. **What is React Router and why do we use it?**

**Answer:**  
**React Router** is a popular library for handling **routing** in React single-page applications. It enables navigation between different views or pages without reloading the browser. React Router maps URL paths to components, supports nested routes, and provides navigation tools like `<Link>` and `<Navigate>`.

**Why it’s asked:**  
Navigation is essential in most real-world apps.

---

### 10. **What is the difference between React and other frameworks like Angular/Vue?**

**Answer:**  
- **React:** A library focused on building UI components. It’s lightweight, flexible, and relies on external libraries for routing and state management.
- **Angular:** A full-fledged framework with built-in solutions for routing, state, forms, and more. Uses TypeScript and has a steeper learning curve.
- **Vue:** A progressive framework that’s easier to learn than Angular, offers built-in features, and is suitable for both small and large apps.
React is chosen for its flexibility and ecosystem; Angular for its completeness; Vue for its simplicity.

**Why it’s asked:**  
To test if you understand where React fits in the ecosystem.

---

> **Tip:** Mastering these questions will help you confidently tackle most