/* 
    Author: Santiago Mendivil Alvarez
    Description: In this file we will cover all the basic syntax for a C# 
        program. We are going to dive into printing something, 
        input something, using variables, data types and operators

*/
using System;

class HelloWorld()
{
    static void Main()
    {
        ///////Printing and reading from the console
        Console.WriteLine("Write something to the console: ");

        string name = Console.ReadLine() ?? string.Empty;

        Console.WriteLine($"Hello, {name} ");


        ///////Variables 
        // The convention for variable naming is camelCase
        // The syntax for declaring variables is: 
        // <data_type> <variable_name> = <value>; 


        ///////Integer 
        // An integer is a number that does not have any decimal places. It is a whole number.
        sbyte a = -128;
        Console.WriteLine("The variable a contains " + a);
        byte b = 255;
        Console.WriteLine("The variable b contains " + b);
        short c = 32767;
        Console.WriteLine("The variable c contains " + c);
        ushort d = 65535;
        Console.WriteLine("The variable d contains " + d);
        int e = 2147483647;
        Console.WriteLine("The variable e contains " + e);
        uint f = 4294967295;
        Console.WriteLine("The variable f contains " + f);
        long g = 9223372036854775807;
        Console.WriteLine("The variable g contains " + g);
        ulong h = 18446744073709551615;
        Console.WriteLine("The variable h contains " + h);


        ///////Float 
        // Floats are floating point numbers with a storage size of 4 bytes, which means that these numbers 
        // can hold decimal places. 
        float i = 256.4788f;
        Console.WriteLine("The variable i contains " + i);
        double j = 2545645645.6647;
        Console.WriteLine("The variable j contains " + j);
        decimal k = 0.33333333333333333333333333357m;
        Console.WriteLine("The variable k contains " + k);


        ///////Casting
        // Casting is the process of converting a value from one data type to another.
        // There are two types of casting: implicit casting and
        // explicit casting. The implicit casting is done automatically by the compiler,
        // while the explicit casting is done by the programmer. 
        float myFloat = 76.467f;
        int myInt = (int)myFloat;

        Console.WriteLine("The variable myInt contains " + myInt);

        ///////Converting from string 
        string var = Console.ReadLine() ?? string.Empty;

        double radius = double.Parse(var);

        // This can be specified in the following way too 
        int value = int.Parse(Console.ReadLine() ?? string.Empty);
    }
}