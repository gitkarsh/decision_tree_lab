import regr_dtree
import sys
import csv

def self_test(tree):
    data = [["tenure track", "minority", "female", "english", "50", "30", "upper", "7", "4"],
            ["teaching", "not minority", "male", "english", "30", "30", "lower", "5", "3"],
            ["tenure track", "minority", "male", "english", "40", "30", "lower", "5", "4"]]

    for row in data:
        print(row, end="")
        print(" prediction = " + regr_dtree.classify(row, tree))

def main(col_names=None):
    # parse command-line arguments to read the name of the input csv file
    # and optional 'draw tree' parameter
    if len(sys.argv) < 2:  # input file name should be specified
        print ("Please specify input csv file name")
        return

    csv_file_name = sys.argv[1]

    data = []
    with open(csv_file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            data.append(row)

    print("Total number of records = ",len(data))
    tree = regr_dtree.buildtree(data, min_gain =0.003, min_samples = 5)

    regr_dtree.printtree(tree, '', col_names)

    max_tree_depth = regr_dtree.max_depth(tree)
    print("max number of questions=" + str(max_tree_depth))

    if len(sys.argv) > 2: # draw option specified
        import regr_dtree_tree_draw
        regr_dtree_draw.drawtree(tree, jpeg=csv_file_name+'.jpg')

    if len(sys.argv) > 3:  # create json file for d3.js visualization
        import json
        import regr_dtree_to_json
        json_tree = regr_dtree_to_json.dtree_to_jsontree(tree, col_names)
        print(json_tree)

        # create json data for d3.js interactive visualization
        with open(csv_file_name + ".json", "w") as write_file:
            json.dump(json_tree, write_file)

    self_test(tree)


if __name__ == "__main__":
    col_names = ['rank',
                 'ethnicity',
                 'gender',
                 'language',
                 'age',
                 'class_size',
                 'cls_level',
                 'bty_avg',
                 'prof_eval']
    main(col_names)