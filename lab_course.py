import math

mult_funct = [age, class_size, beauty_score, proffess_eval, course_eval]

def class_size(x):
    if x <= 30:
        return 30
    if x <= 50:
        return 50
    if x <= 100:
        return 100
    if x <= 200:
        return 200

    return 300

def beauty_score(x):
    if x <= 3:
        return 3
    if x <= 4:
        return 4
    if x <= 5:
        return 5
    if x <= 6:
        return 6

    return 7
    return math.ceil(x)

def age(x):
    if x <= 30:
        return 30
    if x <= 40:
        return 40
    if x <= 50:
        return 50
    if x <= 60:
        return 60
    if x <= 70:
        return 70
    return (math.ceil(x/10))*10

def course_eval(x):
    if x >= 4:
        return "good"
    return "bad"

def proffess_eval(x):
    if x >= 4:
        return 4
    if x >= 3:
        return 3
    if x >= 2:
        return 2

def main(readname, writename):
    readfile = open(readname)
    writefile = open(writename, "w")

    a = 0
    #first line has the various attributes hence reading the first line gets us those
    for line in readfile:
        if a != 0:
            writefile.write("\n")

        attrs = line.rstrip().split(",")

        for i in range(len(attrs)):
            attr = attrs[i]

            try:
                attr = float(attr)
            except ValueError:
                pass

            writefile.write(str(mult_funct[i](attr)) + ("," if i != (len(attrs) - 1) else ""))

        a = 1

if __name__ == "__main__":
    main("../StudentEvaluations.csv", "../NewStudEval.csv")
