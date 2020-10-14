# Integer Arithmetic and Testing!
In this repl we are going to learn about integer arithmetic and testing.

## Instructions:
Open the command shell by pressing Cmd+Shift+S on MacOS or Ctrl+Shift+S on other computers. Note that this is different from the Python output pane that's open by default. The command shell will open up below the Python one.

In the command shell type the word `pytest` and hit enter.


If it says "command not found" try typing `poetry update` and hitting enter. Then try again.

## Testing
1. Annotate the tests for div() found in test_divs.py
1. Fix the faulty test for int_div
1. Add at least 5 more tests (asserts) for int_div
1. Figure out what divs.mod (the mod() function in the file divs.py) does and write 5 tests for it.


## Lets use this stuff
1. In main.py fill in the function `sum(start, end)` so that it adds all the numbers from start to end (not including end but including start) and returns their sum.
1. Create a new file called test_main.py and write 5 tests to see if `sum` works correctly

1. In main.py fill in the function sum_even which should do the same thing as sum, except that it should ignore odd numbers (i.e. sum_even(1,5) => 6)
1. In test_main.py add 4 tests of sum_even

1. In main.py fill in the function list_even which should return a list of the even numbers in the given range
1. Write 3 tests


## Fizz Buzz
1. Fill in the function called fizz_buzz so that it returns a list containing all the numbers between 1 and limit except that all multiples of 3 should be replaced with the word Fizz, all multiples of 5 with the word Buzz and all multiples of 3 and 5 with FizzBuzz!
    - While you are at it I recommend printing out the numbers/fizz/buzz to make debugging easier
1. Write some tests to check that it is working correctly

### If you have made it this far you can probably claim mastery of integer arithmetic and competence in iteration

----------

## Rainfall averages
1. Write a function called `avg(xs)` which when given a list of daily rainfall in inches returns the average daily rainfall in feet.
1. Write some tests to make sure this works

## Primes!
1. Write a function (without importing anything) that checks if a number is Prime
    - The rule for primes is that they have exactly two divisors 1 and themselves (i.e. 7 can only be evenly divided by 1 and 7)
    - 1 is not a prime
1. Write a function that returns a list of the first n primes (where n is an argument)
1. Write some tests to make sure this work

### If you have made it this far you can probably claim mastery of iteration, and certainly competence in testing (maybe even mastery)

----------

## Extra stuff
If you enjoy this type of problem make an account at [Project Euler](https://projecteuler.net/) and see if you can do 1, 2, & 3