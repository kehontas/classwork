## Reading

Read chapter 2 from [*Think Python: How To Think Like a Computer Scientist*](http://www.greenteapress.com/thinkpython/html/thinkpython003.html)

## Playing with list slices

First, read [the Python list documentation](http://docs.python.org/tutorial/introduction.html#lists).

Assume that x has been assigned the following list:

    x = [3, 5, 7, 2, 4, 8, 100, 2]

For each of the following, try these in a Python interpreter and then
describe in English what they mean:

    (example) x[-1]
        x[-1] is 2. The index of -1 refers to the last element in the list.

    (a) x[2:4] # x[2:4] is 7,2. the indices 2 and 4 refer to the elements in the list
    (b) x[1:] # [1:] is everything element in the list excluding the zeroth element
    (c) x[:4] # x[:4] is the elemets startig from zeroth element up to the 4th
    (d) x[1:][2] # [1:][2] is 2. Starting from the element in the first index and then returning the second element after that
    (e) x[2:-2] # [2:-2] is 7,2,4,8. Startig from the second index skipping every two through the end of the list 
    (f) x[5:3] # [5:3] is nothing because it is starting at the element in the 5th inex skipping every 3 which is nothing
    (g) x[100] # [100] is an error because there is no 100th index
    (h) x[-100:100] # [-100:100] is the list because starting at the -100 index and then going to the 100th element is everything starting from the zeroth element
    (i) "surprise"[1:4] # [1:4] returns the string 'urp' because the reference is now "surpirse" adn not x therefore what is returned is the elemets in the indices 1-4

What's the difference between `x[2:3]` and `x[2]`?
x[2:3] returns the list of elements in the indices 2 - 3. x[2] returns the element in the twoeth index

## List sorting

In the provided file listsorter.py, write a program that prompts a
user for 5 numbers. Store those numbers in a list. Print out a list
containing those numbers from smallest to largest.  When you run the
program, you should get output like the following:

    Enter a number: 3
    Enter a number: 2
    Enter a number: 1
    Enter a number: 10000
    Enter a number: -5

    [-5, 1, 2, 3, 10000]

You may want to refer to [this section of the Python
docs](http://docs.python.org/tutorial/datastructures.html#more-on-lists) for
handy functions that you can call on lists.

You can assume that the user of this program will always enter a
number. Don't worry about handling non-number input.

## Practice with dicts

You're going to write a mini-database of favorite foods. Think of 5 people you
know and a food they like, e.g. "Naomi" and "brussels sprouts". In the file
fooddatabase.py, write a program that prompts the user for a name and prints out
that person's favorite food, e.g.

    What person do you want to know about? Naomi
    Naomi's favorite food is: brussels sprouts

Use a dictionary to store the association between people and
food. See:
[the dictionary docs](http://docs.python.org/tutorial/datastructures.html#dictionaries)
if you need a refresher on dictionaries.

For now, don't worry about what happens when your dictionary doesn't
have somebody's name in it. It's fine to have your program throw an
exception. Although, if you're interested in how you would handle
this, check out
[try statements](http://docs.python.org/reference/compound_stmts.html#try)

## Practice with finding information

Use the internet to figure out how to get python to give you a random
integer between 0 and 100.  Write down what function you would use:

In guessmynumber.py, write a program which picks a single random
integer between 0 and 100 and repeatedly asks the user to guess it.

 - When the user is correct, print "You win!" and end the program
 - When the user is incorrect, tell them whether their guess was
   too high or too low, and then let them guess again until they get it.

Hint:

    import foo

is a python statement that makes module foo available from your
program.  For example, if there is a function in foo called flip(),
then you would be able to write foo.flip() in your program.

## Manufactoria

Exercises #3, #4a, #4b

If you didn't finish [Manufactoria](http://pleasingfungus.com/Manufactoria/) puzzle #3, please finish it now.  Do both of the puzzles that branch from #3.
