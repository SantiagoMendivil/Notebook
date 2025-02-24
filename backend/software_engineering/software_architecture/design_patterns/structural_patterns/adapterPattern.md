# Table of contents 
- [Table of contents](#table-of-contents)
- [Adapter Pattern](#adapter-pattern)

# Adapter Pattern 
The adapter pattern works similar to a translator, when two people that speak different languages meet, they usually don't know how to communicate between them, there is where the translator comes in. 

Formally the adapter pattern is defined as allowing incompatible classes to work together by converting the interface of one class into another expected by the clients. 

![Class Diagram for Adapter Pattern](images/image.png)

## Using Adapter Pattern in a Django Project

Let's say you have a Django project where you need to integrate a third-party payment gateway that has a different interface than what your application expects. You can use the adapter pattern to create a bridge between your application and the payment gateway.

### Step 1: Define the Target Interface

First, define an interface that your application expects. For example, a `PaymentProcessor` interface:

```python
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses should implement this method")
```

### Step 2: Implement the Adaptee

Next, implement the third-party payment gateway class. This is the class with the incompatible interface:

```python
class ThirdPartyPaymentGateway:
    def make_payment(self, amount):
        print(f"Processing payment of {amount} through ThirdPartyPaymentGateway")
```

### Step 3: Create the Adapter

Now, create an adapter that implements the `PaymentProcessor` interface and translates the calls to the third-party payment gateway:

```python
class PaymentGatewayAdapter(PaymentProcessor):
    def __init__(self, gateway):
        self.gateway = gateway

    def process_payment(self, amount):
        self.gateway.make_payment(amount)
```

### Step 4: Use the Adapter in Your Django Views

Finally, use the adapter in your Django views to process payments:

```python
from django.shortcuts import render
from .adapters import PaymentGatewayAdapter, ThirdPartyPaymentGateway

def process_payment_view(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        gateway = ThirdPartyPaymentGateway()
        adapter = PaymentGatewayAdapter(gateway)
        adapter.process_payment(amount)
        return render(request, "payment_success.html")
    return render(request, "payment_form.html")
```

In this example, the `PaymentGatewayAdapter` allows your Django application to use the `ThirdPartyPaymentGateway` without changing its interface. This makes your code more flexible and easier to maintain.

### Integrating Stripe and PayPal with Adapter Pattern

Let's consider a scenario where you need to integrate both Stripe and PayPal payment gateways into your Django project. You can use the adapter pattern to create a unified interface for both payment gateways.

### Step 1: Define the Target Interface

First, define an interface that your application expects. For example, a `PaymentProcessor` interface:

```python
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses should implement this method")
```

### Step 2: Implement the Adaptees

Next, implement the Stripe and PayPal payment gateway classes. These are the classes with incompatible interfaces:

```python
class StripePaymentGateway:
    def charge(self, amount):
        print(f"Charging {amount} using Stripe")

class PayPalPaymentGateway:
    def send_payment(self, amount):
        print(f"Sending payment of {amount} using PayPal")
```

### Step 3: Create the Adapters

Now, create adapters that implement the `PaymentProcessor` interface and translate the calls to the respective payment gateways:

```python
class StripeAdapter(PaymentProcessor):
    def __init__(self, gateway):
        self.gateway = gateway

    def process_payment(self, amount):
        self.gateway.charge(amount)

class PayPalAdapter(PaymentProcessor):
    def __init__(self, gateway):
        self.gateway = gateway

    def process_payment(self, amount):
        self.gateway.send_payment(amount)
```

### Step 4: Use the Adapters in Your Django Views

Finally, use the adapters in your Django views to process payments:

```python
from django.shortcuts import render
from .adapters import StripeAdapter, PayPalAdapter, StripePaymentGateway, PayPalPaymentGateway

def process_payment_view(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        payment_method = request.POST.get("payment_method")

        if payment_method == "stripe":
            gateway = StripePaymentGateway()
            adapter = StripeAdapter(gateway)
        elif payment_method == "paypal":
            gateway = PayPalPaymentGateway()
            adapter = PayPalAdapter(gateway)
        else:
            return render(request, "payment_error.html")

        adapter.process_payment(amount)
        return render(request, "payment_success.html")
    return render(request, "payment_form.html")
```

