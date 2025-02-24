# Table of contents 
- [Table of contents](#table-of-contents)
- [Strategy Pattern](#strategy-pattern)
  - [How it works](#how-it-works)
- [Use Cases](#use-cases)
- [Class Diagram](#class-diagram)
- [Example in a Django Project](#example-in-a-django-project)
  - [Define the Strategy Interface](#define-the-strategy-interface)
  - [Define Concrete Strategies](#define-concrete-strategies)
  - [Define the Context](#define-the-context)
  - [Usage example](#usage-example)


# Strategy Pattern 
The strategy pattern is one of the simpler patterns to comprehend. It allows grouping related algorithms under an abstraction, which the client codes against. The abstraction allows switching out one algorithm or policy for another without modifying the client. 

Fomally is defined as **encapsulating algorithms belonging to the same family and making them interchangeable. The consumers of the common interface that the algorithms implement allow switching out one algorithm for another seamlessly.**

## How it works
1. **Strategy Interface**: Defines a common interface for all supported algorithms. 
2. **Concrete Strategies**: Implement the strategy interface with specific algorithms. 
3. **Context**: Maintains a reference to a strategy object and delegates the algorithm's execution to the current strategy.

# Use Cases 
1. **Sorting Algorithms**: Switching between different sorting algorithms like quicksort or mergesort based on the dataset. 
2. **Payment Methods**: Selecting differetn payment methods like credit card, debit card or paypal at runtime. 
3. **Compression Algorithms**: Using different compression algorithms like ZIP or RAR based on the file type. 
4. **Validation Strategies**: Applying different validation rules based on the context. 

# Class Diagram 
![Strategy Pattern](images/strategy.png)

# Example in a Django Project 
Let's consider a scenario where you have a payment processing system, and you want to support multiple payment methods.

## Define the Strategy Interface
Create an interface that declares the method for processing payments. 

```python 
# strategies.py 
from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
```

## Define Concrete Strategies 
Implement the concrete strategies for different payment methods. 

```python 
# concrete_strategies.py
from .strategies import PaymentStrategy


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing credit card payment of {amount}")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing PayPal payment of {amount}")
```

## Define the Context 
Implement the context that maintains a reference to a strategy object and delegates the payment processing to the current strategy. 

```python 
# context.py


class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy 

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        self._strategy.pay(amount)
```


## Usage example 
```python
# views.py
from django.http import HttpResponse
from .context import PaymentContext
from .concrete_strategies import CreditCardPayment, PayPalPayment

def process_payment(request, method, amount):
    if method == "credit_card":
        strategy = CreditCardPayment()
    elif method == "paypal":
        strategy = PayPalPayment()
    else:
        return HttpResponse("Invalid payment method")

    context = PaymentContext(strategy)
    context.execute_payment(amount)

    return HttpResponse(f"Payment of {amount} processed using {method}")
```