///////For of loop 
// It is like the linq loop of C# where you loop through an array with a variable
// that acts like the objects inside of the array. 
const hobbies = ['Programming', 'Reading', 'Gaming', 'Traveling'];

for (const hobby of hobbies) {
    console.log(hobby);
}


///////forEach method
// This method takes an argument of callback function. It is useful to evaluate
// a function into every element on a list 
const groceries = ['Milk', 'Eggs', 'Bread', 'Butter'];

groceries.forEach(function (groceryItem) {
    console.log(`I need to buy ${groceryItem}`);
})

// You can improve this foreach by using an arrow function
groceries.forEach(groceryItem => console.log(`I need to buy ${groceryItem}`));

// Or even better, you can use a function that you have already defined
function printGrocery(groceryItem) {
    console.log(`I need to buy ${groceryItem}`);
}

groceries.forEach(printGrocery);