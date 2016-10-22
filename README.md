# Repetition
An idea for an esoteric language.

Repetition is a language that's built on an infinite tape, with repeating digits "1234567890" in it (which is why the lang is called Repetition).

Features:

- Basic arithmetic (`+-*/`)
- Skipping numbers (`s`)
- Concatenation (`c`)
    - Separator for `s` & `c` (`|`)
- Integer -> ASCII (`a`)
- User input (`[]`)
- Variables
- Variable changing
- While loop (`{}`)

## Arithmetic:

Arithmetic in Repetition works like this:

An arithmetic operator takes two inputs, and does the operation on them. The "inputs" in question are the two numbers to the "left" and the "right" of the operator.

Each operator is inserted in between 2 numbers.

### Examples:

    +    (The + is inserted between 1 and 2, and adds them)
    Output: 3
    
    +-   (Everything is eval'd left-to-right in Repetition, so this evaluates to "(1 + 2) - 3")
    Output: 0
    
    **   (Evals to "(1 * 2) * 3")
    Output: 6
    
    +++/ (Evals to "(((1 + 2) + 3) + 4) / 5")
    Output: 2
    
    /    (Repetition uses floor division, so this evals to floor(1 / 2) = 0)
    Output: 0
    
## Skipping and Concats

"Skipping" in Repetition is represented by the character `s`. It "skips" a number in the tape, and then the operator is evaluated.

### Examples:

    s+    (The "s" skips the 1, so this evals to "2 + 3")
    Output: 5
    
    sss   (This skips 1, 2 and 3, so this evals to "4")
    Output: 4
    
Concatenation (represented by the character `c`) joins two numbers together.

### Examples:

    c     (The "c" concats 1 and 2, so this evaluates to "12")
    Output: 12
    
    sc    (The "s" skips 1, and the "c" concats 2 and 3)
    Output: 23
    
    cc+    (This evals to "123 + 4")
    Output: 127
    
    c+c    (This evals to "12 + 3", with the c concat'ing the "12 + 3" and the 4)
    Output: 154
    
## ASCII:

The ASCII operator (`a`) pops the current value as an ASCII character mod 256.

    c+sca    (The c concats 1 and 2, the s skips 3, and the c concats 4 and 5,
              so the value is "12 + 45" = 57, which is ASCII char "9")    
    Output: 9
    
    sc*a     (The s skips 1, the c concats 2 and 3, so this evals to "23 * 4"
              = 92, which is ASCII char "\")     
    Output: \
    
    c+sca*+a (The first part outputs a "9", and the second part evals to "(6 * 7) + 8"
              = 50, which is ASCII char "2")
              
    Output: 92
    
## User input:

User input is represented by two chars: `[]`. First it asks for the user input, and then any code inside the brackets is multiplied (or "repeated") by the integer input.

ASCII input is not supported.

## Examples:

    [+]
    Input: 5    (The code is now "+++++")
    Output: 21
    
    [+][-]
    Input: 5    (The code is now "+++++[-]")
    Input: 3    (The code is now "+++++---")
    Output: -3
    
    [[+]-]      (You're allowed to have nested input things:
                 the outer ones are input'd first)
    Input: 3    (The code is now [+]-[+]-[+]-)
    Input: 4    (The code is now ++++-[+]-[+]-)
    Input: 2    (The code is now ++++-++-[+]-)
    Input: 2    (The code is now ++++-++-++-)
    Output: 14
    
## Variable declaration and usage:

A variable is declared like so:

    b=+    (b is now equal to 1 + 2 = 3)
    
You can place a variable into the main code like so:

    b+++   (continuing on from last statement:
            since b = 3, and the current number in play is 3,
            this expression evals to "((3 + 3) + 4) + 5")
    Output: 15
    
So the full code:

    b=+    (You must have the var declaration on a separate line)
    b+++
    
## Changing variables:

You can change variables like this:

    ({var}|{code})
    
Where `{var}` is the variable, and `{code}` is the code that changes the variable.

### Example:

Let's assume that `b` is the same as above, and the number in play is `3`.

    (b|++)    (b = (b + 3) + 4)
    b
    Output: 10
    
## While loop:

The while loop is represented by `{}`, and is written like so:

    {{var}|{code}}
    
Where `{var}` is the variable that is being checked, and `{code}` is the code executed.

Any code inside the brackets are executed until the current variable is `<= 0`.

### Example:

    b=+    (b is now initiated to 3)
    +{b|-(b|-)} (The number is now set to 3, so the value is now
                 "3 + 4" = 7, and the while loop is exec'd like so: )
    {b|-(b|-)}  (Because b = 3, the while loop starts. The value is now 7 - 5
                 = 2, and b = 3 - 6 = -3)
    The while loop stops, because b <= 0.
    Output: 2
