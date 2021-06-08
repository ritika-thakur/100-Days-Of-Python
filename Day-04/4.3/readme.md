## Treasure Map


<a href="url"><img src="https://cdn.fs.teachablecdn.com/wiFJAkZZSG2RpGsxYgDO" align="left" height="400" width="400" ></a>

A program which will mark a spot with an X.
In the starting code, you will find a variable called ```map```.
This ```map``` contains a nested list.
When ```map``` is printed this is what the nested list looks like:
```
['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
```
In the starting code, we have used new lines (```\n```) to format the three rows into a square, like this:
```
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```
This is to try and simulate the coordinates on a real map. 


This program allows you to mark a square on the map using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:



<a href="url"><img src="https://cdn.fs.teachablecdn.com/PfApnWnTam1pLUeKbUWZ" align="right" height="400" width="600" ></a>

First it takes the user input and convert it to a usable format. 
Next, nested list is updated with an "X"

### Example Input 1

column 2, row 3 would be entered as:

```
23
```

### Example Output 1

```
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', 'X', '⬜️']
```

### Example Input 2

column 3, row 1 would be entered as:

```
31
```

### Example Output 2

```
['⬜️', '⬜️', 'X']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
```

![alt text](https://cdn.fs.teachablecdn.com/5hliFjyIR96LdestyfPd)

