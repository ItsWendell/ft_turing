# ft_turing in Python

The goal of this project is to write a program able to simulate a single headed, single
tape Turing machine from a machine description provided in json.


## Machine Descriptions

1. A machine able to compute an unary addition.
2. A machine able to decide whether its input is a palindrome or not. Before halting,
write the result on the tape as a ’n’ or a ’y’ at the right of the rightmost character
of the tape.
3. A machine able to decide if the input is a word of the language 0n1n, for instance the words 000111 or 0000011111. Before halting, write the result on the tape as a ’n’ or a ’y’ at the right of the rightmost character of the tape.
4. A machine able to decide if the input is a word of the language 0^(2n), for instance the words 00 or 0000, but not the words 000 or 00000. Before halting, write the result on the tape as a ’n’ or a ’y’ at the right of the rightmost character of the tape.
5. A machine able to run the first machine of this list, the one computing an unary addition. The machine alphabet, states, transitions and input ARE the input of the machine you are writing, encoded as you see
fit.