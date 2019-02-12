import regr_dtree
import sys

if __name__ == "__main__":
    # fruits with their size and color
    fruits = [
        [4, 'red', 'apple'],
        [4, 'green', 'apple'],
        [1, 'red', 'cherry'],
        [1, 'green', 'grape'],
        [5, 'red', 'apple']
    ]

    tree = regr_dtree.buildtree(fruits)
    regr_dtree.printtree(tree, '', ["size", "color"])
    print("fruit [2, 'red'] is: ", regr_dtree.classify([2, 'red'], tree))
    print("fruit [4.5, 'red'] is: ", regr_dtree.classify([4.5, 'red'], tree))
    print("fruit [1.4, 'green'] is: ", regr_dtree.classify([1.4, 'green'], tree))

    max_tree_depth = regr_dtree.max_depth(tree)
    print("max number of questions="+str(max_tree_depth))
    if len(sys.argv) > 1: # draw option specified
        import dtree_draw
        dtree_draw.drawtree(tree, jpeg='fruits_dt.jpg')