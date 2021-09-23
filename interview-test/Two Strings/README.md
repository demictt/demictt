# Two Strings
Given two strings, determine if they share a common [substring](https://en.wikipedia.org/wiki/Substring#:~:text=In%20formal%20language%20theory%20and,was%20the%20best%20of%20times%22.).
_A substring may be as small as one character._

### Example
```
s1 = “and”
s2 = “art”
```
These share the common substring “a”.
```
s1 = “be”
s2 = “cat”
``` 
These do not share a substring.

### Function Description
Complete the function ***twoStrings*** below.
<br />
***twoStrings*** has the following parameter(s):
```
string s1
string s2
```

### Returns
string: either `YES` or `NO`.

### Input Format
 `s1` and `s2` are both are strings.

### Constraints
 `s1` and `s2` consist of characters in the range ascii[a-z].

### Output Format
For each pair of strings, return `YES` or `NO`.

#### Sample Input
```
hello  
world
```
#### Sample Output
```
YES
```


- - - -


#### Sample Input
```
hi
world
```
#### Sample Output
```
NO
```
<br />

- - - -


```
def twoStrings(s1, s2):
	# write your code here
	# assume s1 and s2 already have strings stored
```
