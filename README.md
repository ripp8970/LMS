# Library Management System (LMS) in Core Java

This project implements a simple Library Management System (LMS) using Core Java. It allows users to manage books, including adding, removing, searching, borrowing, returning, and viewing available books.

## Project Overview

The Library Management System provides the following functionalities:

-   **Add New Books:** Add new book entries to the library.
-   **Remove Books:** Remove existing book entries from the library.
-   **Search for Books:** Search for books based on title or author.
-   **Borrow Books:** Allow users to borrow available books.
-   **Return Books:** Allow users to return borrowed books.
-   **View All Available Books:** Display a list of all books currently available in the library.

## Class Structure

The project consists of three main classes:

-   **`Book`:**
    -      Represents a single book in the library.
    -      Attributes: `title`, `author`, `isbn`, `isBorrowed`.
    -   Methods: getters and setters for attributes, `toString()` method.
-   **`Library`:**
    -      Manages the collection of `Book` objects.
    -      Attributes: `books` (an `ArrayList` of `Book` objects).
    -      Methods: `addBook()`, `removeBook()`, `searchBook()`, `borrowBook()`, `returnBook()`, `viewAvailableBooks()`.
-   **`LibraryManagementSystem`:**
    -      The main class that runs the application.
    -      Contains the `main()` method to interact with the user through a console-based interface.

## Notes

* This is a basic LMS and can be extended with more features.
* The code is very basic, and does not contain any security measures. It is highly recommended to add security measures before deploying this to a production environment.
* The code does not contain any form of input sanitization. This is a security risk, and should be addressed.
* The user interface is very basic. Consider adding CSS or a framework to improve the UI.
* Error handling can be improved.
* Consider using prepared statements to prevent SQL injection vulnerabilities.
* This code is a basic example and may require modifications to suit specific library requirements.