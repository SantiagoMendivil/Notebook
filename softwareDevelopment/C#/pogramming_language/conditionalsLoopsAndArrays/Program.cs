/* 
    Author: Santiago Mendivil Alvarez
    Description: In this file we will cover all the conditionals, loops and 
        arrays in C#. We are going to dive into the if, else, else if, switch, 
        for, while, do while, foreach statements and arrays

*/

using System;

class ConditionalAndLoops
{
    static void Main()
    {
        ///////Conditionals 
        // Simple if-elseif-else statement
        double score;

        score = double.Parse(Console.ReadLine());
        Console.WriteLine($"The score is {score}");

        if (score >= 90)
        {
            Console.WriteLine("You got an A");
        }
        else if (score >= 80)
        {
            Console.WriteLine("You got a B");
        }
        else if (score >= 70)
        {
            Console.WriteLine("You got a C");
        }
        else if (score >= 60)
        {
            Console.WriteLine("You got a D");
        }
        else
        {
            Console.WriteLine("You got an F");
        }

        //////Switch statement
        char grade = 'A';

        switch (grade)
        {
            case 'A':
                Console.WriteLine("You got an A");
                break;
            case 'B':
                Console.WriteLine("You got a B");
                break;
            case 'C':
                Console.WriteLine("You got a C");
                break;
            case 'D':
                Console.WriteLine("You got a D");
                break;
            case 'F':
                Console.WriteLine("You got an F");
                break;
            default:
                Console.WriteLine("Invalid grade");
                break;
        }


        ///////Ternary Operators 
        // condition ? first_expression_if_true : second_expression_if_false;
        //example 1 will execute as x is greater than y
        int x = 5;
        int y = 4;
        Console.WriteLine((x > y) ? "x is greater than y" : (x < y) ? "x is less than y" : (x == y) ? "x is equal to y" : "No result");

        ///////Arrays 
        // Static arrays 
        // dataType arrayName[arraySize]; 
        int staticArray[5];

        // Dynamic arrays 
        // dataType[] arrayName = new dataType[arraySize];
        int[] dynamicArray = new int[10];

        // Initializing Static Arrays 
        int[] staticArrayDeclaration = { 1, 2, 3, 4, 5 };

        // Initializing Dynamic Arrays 
        int[] dynamicArrayDeclaration = new int[3] { 1, 2, 3 };

        ///////Multidimensional Arrays
        int[,] multiArray = new int[3, 3];

        // Initialize a multidimensional array
        int[,] array2D = new int[2, 2] { { 1, 2 }, { 3, 4 } };
    }
}