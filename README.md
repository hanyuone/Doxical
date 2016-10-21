# Repetition
An idea for an esoteric language.

Repetition is a language that's built on an infinite tape, with repeating digits "1234567890" in it (which is why the lang is called Repetition).

Features:

- Basic arithmetic (`+-*/`)
- Skipping numbers (`s`)
- Concatenation (`c`)
- Integer -> ASCII (`a`)
- User input (`[]`)

## Arithmetic:

Arithmetic in Repetition works like this:

An arithmetic operator takes two inputs, and does the operation on them. The "inputs" in question are the two numbers to the "left" and the "right" of the operator.

Each operator is inserted in between 2 numbers.

### Examples:

    +    (The + is inserted between 1 and 2, and adds them)
    Output: 3
    
    ++-  (Everything is eval'd left-to-right in Repetition, so this evaluates to "(1 + 2) - 3")
    Output: 0
    
    ***  (Evals to "(1 * 2) * 3")
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
    
Both of these take precedence over arithmetic operators - if there are `s`'s and `c`'s to the right of any `+-*/`, the `s`'s and `c`'s get eval'd first.

### Examples:

    c+sc      (The c concats 1 and 2, the s skips 3, and the c concats 4 and 5,
               so the program evals to "12 + 45")
    Output: 57
    
    c+sc+cc   (Same as before, and c concats 6, 7 and 8. The left "block"
               is eval'd to this (see next line): )
              
    (c+sc)+cc (Which is then eval'd like so: )
    
    57+cc     (Which is then eval'd to "57 + 678")
    
    Output: 735
    
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

User input is represented by two chars: `[]`. First it asks for the user input, and then any code inside the brackets is multiplied by the integer input.

ASCII input is not supported.

    [+]
    Input: 5    (The code is now "+++++")
    Output: 21
    
    [+][-]
    Input: 5    (The code is now "+++++[-]")
    Input: 3    (The code is now "+++++---")
    Output: -3
