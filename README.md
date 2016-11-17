# Doxical

## An esoteric language.

Doxical is an esoteric language that is based on a grid.

## Characters:
- Directions (`^>v<`)
- Decimal and ASCII output (`acdp`)
- User input (`[]`)
- Variables
    - Alter variables (`()`)
- While loops (`{}`)

## Basic explaining:

Doxical is based off of a grid that stretches infinitely in all directions: north, south, east and west. A program in Doxical essentially manoeuvres a bot on that grid.

To move the bot, the keys `^>v<` are used to represent the 4 directions:
- North: `^`
- East: `>`
- South: `v`
- West: `<`

Examples of valid code is `^^^^`, which means "go north 4 times".

Moving back to a grid that was already moved on is forbidden, and results in the interpreter crashing - something like this:

    ^v
    
Results in illegal code, because you're moving back to a square you were already on.

Doxical also has a value (henceforth called the Value) and a counter. The counter goes up by 1 every time the bot moves, and resets to 0 if the bot goes over 9. The Value is altered by moving, like so:

- Move north: Add the counter to the value (`value += counter`).
- Move east: Subtract the counter from the value (`value -= counter`).
- Move south: Multiply the value by the counter (`value *= counter`).
- Move west: Divide the value by the counter (`value /= counter`).
    - Dividing is integer division in this case (`5/2 = 2`).
    - Also, dividing by 0 is forbidden (when the counter is `0` and you move west) - this results in the interpreter crashing.
    
### Example:

    ^^^^
    Value: 10
    
    <<
    Value: 0
    
## Variables:

There are 26 variables in Doxical, each represented by UPPERCASE LETTERS (`A-Z`). Each of them can be assigned a value like so:

    ^^^A
    Initiates A to 6 (1 + 2 + 3).
    
    B^^^
    Initiates B to 0.
    Value: 6
    
Every time you declare a variable, the Value resets to `0` - essentially popping it to the variable.

    ^^^A^
    The value is now 4, NOT 10.
    
The variable can be altered by reassigning it through popping the Value, or by altering the variable through moves:

    ^A(A^^^)
    A is now at 10.
    The first char after the "(", in this case A, shows what variable is to be changed.

## Output

Output is represented through 4 "flags":

- `a`: Appends the ASCII value of the `out_var` to the final output, and then outputs it all.
- `c`: Concat - appends the ASCII value of the `out_var` to the final output, and then does nothing.
- `d`: Appends the decimal value of the `out_var` to the final output, and then outputs it all.
- `p`: Plus - appends the decimal value of the `out_var` to the final output, and then does nothing.

The `out_var` is the character that's at the end of an output flag - which could be 1 of 3 choices:

- Uppercase character: `out_var` is equal to the value of the variable declared (see above).
- Space: `out_var` is equal to the Value.
- Any other character: `out_var` is equal to the Value. The next character is ignored.

The reason there's two characters for outputting the Value is because of this:

    ^^^ddBdB (the first B is meant to be a declaration)
    
So we have to introduce a new character to "split" the output of the Value and the declaration of `B`, like so:

    ^^^dd BdB (Outputs 6, 6, declares B to be 6, then outputs B)
    
## User input:

User input is represented through square brackets, `[]`. Only decimal input is currently supported, as what the user input does is "multiply" the code inside the brackets by that user input.

    [^]d
    Input: 2
    (Code becomes ^^d, "^" is repeated 2 times)
    
    [^>]
    Input: 3
    (Code becomes ^>^>^>, "^>" is repeated 3 times)
    
## While loops:

While loops are represented through curly brackets, `{}`. Any valid code can be placed in between the while loops - nested loops are supported as well. They execute until the "check variable" is below 0. The check variable is the first character in the while loop.

    B^^^A{A(A>)(B^)}
    Check variable = A, which is currently 6.
    First loop: A = 6 - 4 = 2, B = 0 + 5 = 5
    Second loop: A = 2 - 6 = -4, B = 5 + 7 = 12
    A is now below 0, so while loop stops. A = -4, B = 12
