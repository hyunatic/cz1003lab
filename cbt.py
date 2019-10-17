def printTree(tree, level):
    if len(tree) == 1:
        print("  " * level, end=" ")
        print(tree[0])
    else:
        #Print Left tree
        printTree(tree[0], level + 1)

        print("  " * level, end=" ")
        print(tree[1])

        #Print Right Tree
        printTree(tree[2], level + 1)

t = [[[7],1,[9]],3,[[8],2,[4]]]
printTree(t , 0)