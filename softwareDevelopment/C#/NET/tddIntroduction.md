# Table of contents 
- [Table of contents](#table-of-contents)
- [Test Driven Development](#test-driven-development)
  - [Create a Solution](#create-a-solution)

# Test Driven Development 

## Create a Solution 
From the terminal you must follow some steps that I will cover in this section which are the basics to start doing TDD.

1. First of all you need to have installed dotnet on you computer
2. Then in a folder we have to create a solution for the project 
```powershell
dotnet new sln -n SolutionName
```
3. Now that we have our solution we have to create a class library project 
```powershell 
dotnet new classlib -n ClassLibName 
```
4. After that we have to add the project to the solution 
```powershell 
dotnet sln add ClassLibName/ClassLibName.csproj
```
5. Then we need to create a unit test project 
```powershell 
dotnet new mstest -n ClassLibName.Tests
```
6. Now add the tests project to the solution 
```powershell 
dotnet sln add ClassLibName.Tests/ClassLibName.Tests.csproj
```
7. Finally we have to reference the class library inside the tests project
```powershell 
dotnet add ClassLibName.Tests/ClassLibName.Tests.csproj reference ClassLibName/ClassLibName.csproj
```


If everything was done step by step just run `dotnet build` if it returns a `Build Succeeded` message then everything was connected succesfully. 