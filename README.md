- Moving Zeros To The End:

Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

- Simple Pig Latin:

Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched.
Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

- Valid Parentheses:

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, and false if it's invalid.
Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100
Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. 
Furthermore, the input string may be empty and/or not contain any parentheses at all. 
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

- Human Readable Time:

Write a function, which takes a non-negative integer (seconds) as input and 
returns the time in a human-readable format (HH:MM:SS)
HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
You can find some examples in the test fixtures.

- Directions Reduction:

Once upon a time, on a way through the old wild mountainous west,…
… a man was given directions to go from one point to another. 
The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild 
west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die 
of thirst!
How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following (depending on the language):
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]
You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay 
to the same place! So the task is to give to the man a simplified version of the plan. 
A better plan in this case is simply:
["WEST"]
or
{ "WEST" }
or
[West]
Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.
The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the 
final result is [] (nil in Clojure).
In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but 
they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].
Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless 
directions removed (W<->E or S<->N side by side).
The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {North, East, West, South}.
See more examples in "Sample Tests:"
Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", 
"WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result 
path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
if you want to translate, please ask before translating.
