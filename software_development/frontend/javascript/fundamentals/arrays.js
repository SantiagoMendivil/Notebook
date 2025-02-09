// If we declare an array with const, it remain mutable. Meaning that 
// we can change the contents, not cannot reassign the variable. 

// Declaring an array
let cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'];


// Accessing elements in an array
console.log(cities);
console.log(`First element before changes: ${cities[0]}`);
console.log(`Last element before changes: ${cities[cities.length - 1]}`);


// Modifying elements in an array
cities[0] = 'San Francisco';
cities[cities.length - 1] = 'Miami';


// Adding elements to an array
cities.push('Seattle');

// Removing elements from an array (removes the last element)
cities.pop();

// Slice method returns a new array with a portion of the original array
let slicedCities = cities.slice(1, 3);

// Splice method changes the contents of an array by removing or 
// replacing existing elements and/or adding new elements
cities.splice(1, 2, 'Philadelphia', 'San Diego');

// Adds one or more elements to the beginning of an array
cities.unshift('Boston');

console.log(cities)