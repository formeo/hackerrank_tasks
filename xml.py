import sys
import xml.etree.ElementTree as etree

# def get_attr_number(node):
#     tree = etree.ElementTree()
#     tree.parse(node)
#     root = tree.getroot()
#     print(root.attrib)
#     for child in root:
#       print(child.tag, child.attrib,len(child.attrib))

def get_attr_number(node):
    i=0
    for elem in node.findall(".//*[@attr]"):
        print(elem)
    i+=len(node.attrib)
    for child in node:

        i+=len(child.attrib)
        for clild2 in child:
            i += len(clild2.attrib)
    return (i)




tree = etree.ElementTree(etree.fromstring("<feed xml:lang='en'>\
  <title>HackerRank</title>\
  <subtitle lang='en'>Programming challenges</subtitle>\
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>\
  <updated>2013-12-25T12:00:00</updated>\
  <entry>\
  	<author gender='male'>Harsh</author>\
    <question type='hard'>XML 1</question>\
    <description type='text'>This is related to XML parsing</description>\
  </entry>\
</feed>"))
root = tree.getroot()
print(get_attr_number(root))
