maxdepth = 0
def depth(elem, level):
    global maxdepth
    def sup_depth(elem,level):
        return max([0] + [sup_depth(child,level) + 1 for child in elem])
    maxdepth = sup_depth(elem,level)
