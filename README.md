# TestBricks


### What is this?

TestBricks is a lightweight and easy to use platform for knowledge testing programs.
This repository provides a library of classes and functions, that can help you to create
programs with GUI, using qt5 or GTK, for example.
Main language of this project in Python, but I will develop a C++ version very soon.


### How can I use it?

There are two branches: *python* and *cpp*. 
They contain source code of TestBricks library on the respective languages.
You can download them and import to your project.


### Code documentation

The package contains two files: *__init__.py* and *core.py*.
The first file is empty and can be useless, but it helps to create package
in older versions of Python. Second file is the main file of the library.


#### Classes description

##### Question

*Question (text, answer, value)* - Declares question structure.
text (str) - text (formulation) of the question
answer (str) - correct answer
value (int) - weight of the question (points, that will be added to student's test score in case of correct answer)

It has two methods:
*to_dict()* - returns a **dictionary** built from the question data
*to_list()* - returns a **list** from the question data

##### Test

*Test (name, subject, author, questions, allotted_time)* - Declares test structure.
name (str) - test name
subject (str) - subject of the test
author (str) - author name
questions (list) - array of Question objects
allotted_time (int) - allotted time in seconds

It has three methods:
*to_list()* - returns **list** of test questions
*to_dict()* - returns **dictionary** built from the test data
*save_to_file(path)* - saves test data to file using JSON format (path (str) - path for saving)


#### Global functions description

*get_test_from_file(path)* - returns **Test** object, built from file (path (str) - path to file)
