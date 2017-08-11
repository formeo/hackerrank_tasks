def get_attr_number(node):
    i=0    
    i+=len(node.attrib)    
    for child in node:
        i+=len(child.attrib)
        for clild2 in child:
            i += len(clild2.attrib)
    return (i)  
