tableData = [ ["apples", "oranges", "cherries", "bananas"], ["Alice", "Carol", "Bob", "David"], ["Dogs", "Cats", "Moose", "Goose"] ];

maxLen = 0;

for x in tableData : 
	for y in x : 
            maxLen = len(y) if maxLen < len(y) else maxLen;

formatString = "{:>" + str(maxLen) + "}";

for x in tableData : 
    for y in x :
        print formatString.format(y) ,
    print;