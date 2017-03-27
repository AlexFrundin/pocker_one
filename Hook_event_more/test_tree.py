import os

rootDir = 'C:\\Users\\Freedom\\Documents\\GitHub\\pocker_one'
for dirName, subDir, fileName in os.walk(rootDir):
    item = QTreeWidgetItem(tree, [subDir])
    Q
