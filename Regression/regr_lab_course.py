import math


def same(x):  # For attributes which we don't change
    return x


def course_evaluation(x):  # Course evaluation attribute
    if x >= 4:
        return "good"

    return "bad"


def age(x):  # Age attribute
    if x <= 30:
        return 30

    return (math.ceil(x/10))*10


def class_size(x):  # Class size attribute
    if x <= 30:
        return 30
    if x <= 50:
        return 50
    if x <= 100:
        return 100
    if x <= 200:
        return 200

    return 300


def beauty_score(x):  # Beauty score attribute
    if x <= 3:
        return 3
    if x > 6:
        return 7

    return math.ceil(x)


def prof_evaluation(x):  # Professor evaluation score attribute
    if x >= 4:
        return 4
    if x >= 3:
        return 3
    if x >= 2:
        return 2


# List of functions to execute corresponding to each attribute
change_fns = [same, same, same, same, age, class_size, same, beauty_score, prof_evaluation, course_evaluation]


def main(readname, writename):
    readfile = open(readname)
    writefile = open(writename, "w")

    c = 0
    for line in readfile:
        if c != 0:
            writefile.write("\n")

        # Get array of attribute values
        attributes = line.rstrip().split(",")

        # Iterate through attribute values
        for i in range(len(attributes)):
            attribute = attributes[i]

            try:
                attribute = float(attribute)
            except ValueError:
                pass

            writefile.write(str(change_fns[i](attribute)) + ("," if i != (len(attributes) - 1) else ""))

        c = 1


if __name__ == "__main__":
    main("StudentEvaluations.csv - StudentEvaluations.csv.csv", "../NewRegr.csv")