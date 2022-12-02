# This script is used to check if two lines intersect at a given point

def repeat_solving_line(x, y, line):  # Function created so you could run the same set of code twice
    line.strip()  # Clearing any spaces on the edges of "line"
    new_line = ""
    solved_equation = line + "\n"  # showing the initial line you typed
    for i in line:  # Will substitute "x" or "y" when it sees it while going through "line"
        if i == "x":
            if line[line.index(i) - 1] != " " and line.index(
                    i) != 0:  # If the item before "i" == " " and the index != 0
                new_line += "*" + str(x)
            else:  # If not than just put "x", and not "*x"
                new_line += str(x)
        elif i == "y":  # Does the same for "y"
            if line[line.index(i) - 1] != " " and line.index(i) != 0:
                new_line += "*" + str(y)
            else:
                new_line += str(y)
        else:  # If there is no "x" or "y", it will just add the character it is on
            new_line = new_line + i
    solved_equation += str(new_line) + "\n"  # showing the line with x and y values substituted
    new_line = new_line.split("=")  # Splits the two sides of the equation
    new_line = [eval(i.strip()) for i in new_line]  # Evaluates each side of the split equation
    equals_true = new_line[0] == new_line[1]  # Will check if the two sides of the equation are equal
    new_line = str(new_line[0]) + " = " + str(new_line[1])  # Adding equal sign to make it look better :)
    solved_equation += str(new_line) + "\n" + str(equals_true) + "\n"  # Updating solved_equation
    return solved_equation, equals_true  # Returns the solved equation and True or False


def contains_point(x, y, line1, line2):
    if (type(x) and type(y)) != int:  # Checks if x and y are integers
        return "Error: Invalid Types"
    full_line = str(repeat_solving_line(x, y, line1)[0]).strip('"') + "\n"  # Final Equation = equation in function
    full_line += str(repeat_solving_line(x, y, line2)[0]).strip('"') + "\n"  # (For both lines)
    if (str(repeat_solving_line(x, y, line1)[1]).strip('"')) == "True":  # Checking if both equations come out as True
        if (str(repeat_solving_line(x, y, line2)[1]).strip('"')) == "True":  # If equals Yes, check the other one
            is_true = "Yes"
        else:
            is_true = "No"
    else:
        is_true = "No"

    full_line += is_true  # Adds "Yes" or "No" to the final solution
    return full_line  # Returns the final solution!!


# The first parameter is your x position of the point, followed by the y position of the point.
# The next two parameters are the equations you would like to evaluate
# Put spaces between each term in the equation. For example: "2x - y = 7" would work, NOT "2x- y=7"
print(contains_point(3, -1, "x - 2y = 5", "2x - y = 7"))  # will print out the solution to the problem
