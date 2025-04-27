/* 
    The ternary operator is useful when we have one line 
    if-else statements in order to save lines of code.
*/

// Basic If-Else statement
let isNight = true;

if (isNight) {
    console.log('Good night!');
} else {
    console.log('Good day!');
}

// Using Ternary operator
isNight ? console.log('Good night!') : console.log('Good day!');