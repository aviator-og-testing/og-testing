Brainfuck is an esoteric programming language created by Urban Müller in 1993.
It uses only 8 commands: + - < > [ ] . ,
This program prints "Hello World" by manipulating memory cells and ASCII values.

Memory layout: Cell 0 holds 'H', cell 1 holds 'e', etc.
The program uses loops to efficiently set up the ASCII values.

++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.

How it works:
- Initialize cell 0 to 10 (used as loop counter)
- Loop 10 times to set up cells 1-4 with multiples of 10
- Cell 1 = 70 (close to 'H' = 72)
- Cell 2 = 100 (close to 'e' = 101)
- Cell 3 = 30 (close to space = 32)
- Cell 4 = 10 (used for newline)
- Fine-tune each cell and print with . command

Character breakdown:
H (72), e (101), l (108), l (108), o (111), space (32), W (87), o (111), r (114), l (108), d (100)
