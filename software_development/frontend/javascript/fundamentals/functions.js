
// There are different ways on how to define a function in javascript
// 1. Function keyword 
function greet(name) {
    console.log(`Hello, ${name}!`);
}

// 2. Function Expressions 
const calculateArea = function (width, height) {
    const area = width * height;
    return area;
}

// 3. Arrow Functions
const add = (a, b) => a + b;

const rectangleArea = (width, height) => width * height;

const circleArea = radius => {
    let area = Math.PI * Math.pow(radius, 2);
    return area;
};

// 4. Function Constructor
const multiply = new Function('a', 'b', 'return a * b');

// 5. Generator Functions
function* count(max) {
    let i = 0;
    while (i < max) {
        yield i++;
    }
}

// 6. Immediately Invoked Function Expression (IIFE)
(function () {
    console.log('This function is invoked immediately');
})();

// 7. Recursive Functions
function factorial(n) {
    // For memory optimization, we can use the ternary operator
    // return n === 0 ? 1 : n * factorial(n - 1);

    // If the number is to big, just don't call the recursion 
    if (n > 1000) {
        return 'Number too big';
    }

    if (n === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

// 8. Callback Functions
function greetUser(name, callback) {
    callback(name);
}
