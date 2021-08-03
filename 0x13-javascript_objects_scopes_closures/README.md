# 0x13. JavaScript - Objects, Scopes and Closures

**Usefull Links**
- [JavaScript object basics](https://intranet.hbtn.io/rltoken/OJ4pU6uHwfCrAclbZsk_Hg)
- [Object-oriented JavaScript](https://intranet.hbtn.io/rltoken/Uqv-UMsBUpHWQZXBf5fn0g)
- [Class - ES6](https://intranet.hbtn.io/rltoken/zMWxOmGWEsOCldCKeDswCA)
- [super - ES6](https://intranet.hbtn.io/rltoken/DTMKogwFYEgUnpLrNvTcfQ)
- [extends - ES6](https://intranet.hbtn.io/rltoken/fh2JHfNNa-HLnmfSdOo9TA)
- [Object prototypes](https://intranet.hbtn.io/rltoken/lrlwnQMM82RimJJcfLao5w)
- [Inheritance in JavaScript](https://intranet.hbtn.io/rltoken/LDpXxzBrdmmXAHoNrWwLxg)
- [Closures](https://intranet.hbtn.io/rltoken/qDa7F8060Jlhe3DZZitY4A)
- [this/self](https://intranet.hbtn.io/rltoken/ockP7FQKKmTRvfeAHw-XSw)
- [Modern JS](https://intranet.hbtn.io/rltoken/22mdHf9KeFhRQrLP-e1hPw)

## Tasks
## 0. Rectangle #0
Write an empty class Rectangle that defines a rectangle:

- You must use the `class` notation for defining your class

`File:` [0-rectangle.js](0-rectangle.js)
  
  
## 1. Rectangle #1
Write a class Rectangle that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`

`File:` [1-rectangle.js](1-rectangle.js)
  
  
## 2. Rectangle #2
Write a class Rectangle that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to `0` or not a `positive integer`, create an `empty object`

`File:` [2-rectangle.js](2-rectangle.js)
  
  
## 3. Rectangle #3
Write a class Rectangle that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments: `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to `0` or not a `positive integer`, create an `empty object`
- Create an instance method called `print()` that prints the rectangle using the character `X`

`File:` [3-rectangle.js](3-rectangle.js)
  
  
## 4. Rectangle #4
Write a class Rectangle that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments: `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to `0` or not a `positive integer`, create an `empty object`
- Create an instance method called `print()` that prints the rectangle using the character `X`
- Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
- Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by `2`

`File:` [4-rectangle.js](4-rectangle.js)
  
  
## 5. Square #0
Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

- You must use the `class` notation for defining your class and `extends`
- The constructor must take 1 argument: `size`
- The constructor of `Rectangle` must be called `(by using super())`

`File:` [5-square.js](5-square.js)
  
  
## 6. Square #1
Write a class Square that defines a square and inherits from Square of 5-square.js:

- You must use the `class` notation for defining your class and extends
- Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
- If `c` is undefined, use the character `X`

`File:` [6-square.js](6-square.js)
  
  
## 7. Occurrences
Write a function that returns the number of occurrences in a list:

- Prototype: `exports.nbOccurences = function (list, searchElement)`

```Javascript
#!/usr/bin/node
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["H", 12, "c", "H", "Holberton", 8], "H"));
```

```shell
$ ./7-main.js
1
4
2
```

`File:` [7-occurrences.js](7-occurrences.js)
  
  
## 8. Esrever
Write a function that returns the reversed version of a list:

- Prototype: `exports.esrever = function (list)`
- You are not allow to use the built-in method `reverse`

```Javascript
#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(["Holberton", 89, { id: 12 }, "String"]));
```
```shell
$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'Holberton' ]
```

`File:` [8-esrever.js](8-esrever.js)
  
  
## 9. Log me
Write a function that prints the number of arguments already printed and the new argument value. (see example below)

- Prototype: `exports.logMe = function (item)`
- Output format: `<number arguments already printed>: <current argument value>`

```Javascript
#!/usr/bin/node
const logMe = require('./9-logme').logMe;

logMe("Hello");
logMe("Holberton");
logMe("School");
```
```shell
$ ./9-main.js
0: Hello
1: Holberton
2: School
```

`File:` [9-logme.js](9-logme.js)
  
  
## 10. Number conversion
Write a function that converts a number from base 10 to another base passed as argument:

- Prototype: `exports.converter = function (base)`
- You are not allowed to import any file
- You are not allowed to declare any new variable `(var, let, etc..)`

```Javascript
#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));


myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));
```
```shell
$ ./10-main.js
2
12
89
2
c
59
```

`File:` [10-converter.js](10-converter.js)
  
  
## 11. Factor index
Write a script that imports an array and computes a new array.

- Your script must import list from the file `100-data.js`
- You must use a `map`. [Tips](https://intranet.hbtn.io/rltoken/aWmgrzMUMiiuFI_ivcgfKw)
- A `new list` must be created with each value `equal` to the value of the `initial list`, multipled by the index in the list
- Print both the initial list and the new list

```Javascript
#!/usr/bin/node
exports.list = [1, 2, 3, 4, 5];
```
```shell
$ ./100-map.js 
[ 1, 2, 3, 4, 5 ]
[ 0, 2, 6, 12, 20 ]
```

`File:` [100-map.js](100-map.js)
 
 
## 12. Sorted occurences
Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

- Your script must import dict from the file `101-data.js`
- In the new dictionary:
- A key is a number of occurrences
- A value is the list of user ids
- Print the new dictionary at the end

```Javascript
#!/usr/bin/node
exports.dict = {
  89: 1,
  90: 2,
  91: 1,
  92: 3,
  93: 1,
  94: 2
};
```
```shell
$ ./101-sorted.js 
{ '1': [ '89', '91', '93' ], '2': [ '90', '94' ], '3': [ '92' ] }
```

`File:` [101-sorted.js](101-sorted.js)
 
 
## 13. Concat files
Write a script that concats 2 files.

- The `first argument` is the file path of the `first source file`
- The `second argument` is the file path of the `second source file`
- The `third argument` is the file path of the `destination`

```shell
$ cat fileA
C is fun!
```
```shell
$ cat fileB
Python is Cool!!!
```
```
$ ./102-concat.js fileA fileB fileC
$ cat fileC
C is fun!
Python is Cool!!!
```
guillaume@ubuntu:~/0x13$ 

`File:` [102-concat.js](102-concat.js)
