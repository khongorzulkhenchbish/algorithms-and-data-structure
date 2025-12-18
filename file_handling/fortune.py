"""
"fortune" cli command

Fortune is a program that displays a random message from a database of quotations that first appeared in Version 7 Unix. Distributions of fortune are usually bundled with a collection of themed files, containing sayings like those found on fortune cookies (hence the name), quotations from famous people, jokes, or poetry.

This problem consists of writing said "fortune" command.  It will take no arguments for simplicity and print a single random message from the quotations database. The random should be uniformly weighted so that each fortune in the database has the same "equal" chance to be printed.

The quotations database is a text file that contains at least one fortune like the following:

===START FILE===(This part is not inside the file)
Notice From Management:
All Leave will be suspended until morale improves!
%
Dumb terminal
%
Parkinson's Law:  Work expands to fill the time allotted it.
%
%
The Law, in its majestic equality, forbids the rich, as well as the poor,
to sleep under the bridges, to beg in the streets, and to steal bread.
            -- Anatole France
%
CPUs running at 150%
%
% really is an ugly character!
%
50% of the time it works every time!
%
.______.
|      |
| ASCII|
| BOX  |
.______.
%
%     
%
===END FILE===(This part is not inside the file)
"""

def fortune():

    texts = []
    try:
        with open("db.txt", "r") as file:

            for line in file:
                line.strip() # %,\n
                # CPUs running at 150%
                if line[0].isalphanum():
                    text.append(line)
                    continue
                
                # A valid terminator has:
                # line[0] always is %
                # line[1] is always \n
                # % \n
                # aknfv
                # ['%', '\n'] # valid => len(line) => 2 <-- is terminator
                # ['%', ' ', '\n'] # invalid => len(line) => 3

                # ['%', ' ', '\n'] # invalid => len(line) => 3
                # ['%', 'abc', '\n'] # invalid => len(line) => 3
                if line[0] == "%" and len(line) == 2 and line[1] == '\n':
                    # This is terminator
                    ...
                    continue

                # .______.
                # |      |
                # | ASCII|
                # | BOX  |
                # .______.
                texts[-1] += "\n"
                texts[-1] += line
                # still valid line-  % really is an ugly character!
            
    except FileNotFoundError:
        print("file not found")


"""

%
I am a teapot
%

Foo
% is a symbol used in math
% can also be a modulus symbol in C lang
Bye

%

$ fortune

Foo
% is a symbol used in math
% can also be a modulus symbol in C lang
Bye



Example Output from the bash shell on linux:

bash# fortune
CPUs running at 150%
bash# fortune
bash# fortune
The Law, in its majestic equality, forbids the rich, as well as the poor,
to sleep under the bridges, to beg in the streets, and to steal bread.
            -- Anatole France
bash# fortune
% really is an ugly character!
bash# fortune
Notice From Management:
All Leave will be suspended until morale improves!
bash#
"""