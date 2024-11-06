#  Table of contents
- [Table of contents](#table-of-contents)

# Password Attacks 
While authentication and authorization sound similar, there is an important distinction between the two. **Authentication**is about proving your identity, while **authorization** is about what privileges someone has. For instance, logging into a computer is authentication, but whether or not you’re allowed to run a certain program once you’re logged in is authorization. Passwords are commonly used for authentication.

**Plaintext** refers to data that has NOT been encrypted or hashed, and is stored in an insecure, easily readable format.

**Hashing** is related to encryption, but the most important difference between the two is that encryption is reversible, while hashing is not.


# Storing Passwords 
## Plaintext 
The easiest and most obvious solution is to store the passwords in a plaintext file, and make sure that only you and the authentication system have permission to read that file. 

All it takes for the hacker to complete their objective is to somehow access the file. There are many ways to go about this, from privilege escalation to just tricking the system into accessing the file for them. However they go about it, once they have the file, they have the plaintext passwords.

## Encryption
The key used to encrypt the file needs to be stored somewhere so the authentication system can access it, and if the hacker can obtain the file containing the passwords, they can probably get the file containing the encryption key too.

## Hashing
Hashing the entire password file wouldn’t help you, but what you can do is hash each password within the file individually. Then, when a user enters a password, you hash the password they entered and compare it to the stored hash. If the hashes match, the password was correct. 

## Salting 
After thinking about it for a while, you realize that there’s no way to perfectly protect the passwords: As long as the attacker is able to make guesses and check if they’re correct, they will ALWAYS be able to crack a password eventually.