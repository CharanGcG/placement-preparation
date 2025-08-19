# One Memorable Example to Explain OOPS (Banking System)

### Example: **"Banking System"**

1. **Encapsulation (Protecting data)**
   - A customer’s **account balance** is private.  
   - You can access or modify it only through **methods** like `deposit()` or `withdraw()`.  
   - → This ensures data security and controlled access.

2. **Abstraction (Hiding implementation details)**
   - A customer just uses **ATM functions** like `withdrawMoney()` or `checkBalance()`, without knowing the **internal database queries or authentication process**.  
   - → Complexity is hidden, only essential operations are visible.

3. **Inheritance (Building hierarchy)**
   - `Account` can be a **base class**.  
   - `SavingsAccount`, `CurrentAccount`, `LoanAccount` can **inherit** from it, adding their own specific features.  
   - → This avoids code duplication and promotes reuse.

4. **Polymorphism (Same action, different behavior)**
   - The method `calculateInterest()` works differently in **SavingsAccount vs LoanAccount**.  
   - → Same method call, but output changes according to the object type.  

***

## Java Code Example (Banking System with OOPS)

```java
// Base class
class Account {
    private double balance; // Encapsulation

    public Account(double balance) {
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
        } else {
            System.out.println("Insufficient balance!");
        }
    }

    public double getBalance() {  // Encapsulation - controlled access
        return balance;
    }

    // Polymorphic method
    public double calculateInterest() {
        return 0; // Default, will be overridden
    }
}

// Inheritance: SavingsAccount extending Account
class SavingsAccount extends Account {
    public SavingsAccount(double balance) {
        super(balance);
    }

    @Override
    public double calculateInterest() { // Polymorphism
        return getBalance() * 0.04; // 4% interest
    }
}

class CurrentAccount extends Account {
    public CurrentAccount(double balance) {
        super(balance);
    }

    @Override
    public double calculateInterest() {
        return getBalance() * 0.02; // 2% interest
    }
}

// Abstraction: User interacts with high-level methods only
public class BankingSystem {
    public static void main(String[] args) {
        Account acc1 = new SavingsAccount(1000);
        Account acc2 = new CurrentAccount(2000);

        acc1.deposit(500);
        acc2.withdraw(300);

        System.out.println("Savings Acc Balance: " + acc1.getBalance());
        System.out.println("Interest: " + acc1.calculateInterest());

        System.out.println("Current Acc Balance: " + acc2.getBalance());
        System.out.println("Interest: " + acc2.calculateInterest());
    }
}
```

***

### Interview-Ready Summary:
“In a **Banking System**, OOPS fits perfectly:  
- Account balance is **encapsulated**,  
- ATM operations give **abstraction** to customers,  
- Different account types use **inheritance**,  
- Interest calculation shows **polymorphism**.  
This makes the system secure, reusable, and extensible.”  

***