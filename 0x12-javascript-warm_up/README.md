# 0x12. JavaScript - Warm up

**Install Node 10**
```shell
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install nodejs
```

**Install semi-standard**
```shell
$ sudo npm install semistandard --global
```

**Useful links**
- [Writing JavaScript Code](https://intranet.hbtn.io/rltoken/OdMLtl6Y9mpQkaoEqJCRSg)
- [Variables](https://intranet.hbtn.io/rltoken/iE6zaLw7pybp648IfRmk5Q)
- [Data Types](https://intranet.hbtn.io/rltoken/4td1BbZAYn4Dldi6k0CY7A)
- [Operators](https://intranet.hbtn.io/rltoken/OdMLtl6Y9mpQkaoEqJCRSg)
- [Operator Precedence](https://intranet.hbtn.io/rltoken/ALCoiVRvxmsjdqCUdWC_lg)
- [Controlling Program Flow](https://intranet.hbtn.io/rltoken/Nlfhdy6Thyu_WgtBSqoAUw)
- [Functions](https://intranet.hbtn.io/rltoken/Ta66PZ6_16K3q99oELvjkQ)
- [Objects and Arrays](https://intranet.hbtn.io/rltoken/osu583B5jskDVwmcm50-NQ)
- [Intrinsic Objects](https://intranet.hbtn.io/rltoken/osu583B5jskDVwmcm50-NQ)
- [Module patterns](https://intranet.hbtn.io/rltoken/mduSK-WOoRe6WohU1p2zZQ)
- [var, let and const](https://intranet.hbtn.io/rltoken/kNWuHjyUvjr74wU2hBqd_A)
- [JavaScript Tutorial](https://intranet.hbtn.io/rltoken/qkp1hdLiI8DJje88bxcL6w)
- [Modern JS](https://intranet.hbtn.io/rltoken/ieSajamJQ-Nv3XzcS_d5lA)


## 0. First constant, first print
Write a script that prints “JavaScript is amazing”:

- You must create a constant variable called myVar with the value `“JavaScript is amazing”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

*File:* [0-javascript_is_amazing.js](0-javascript_is_amazing.js)


## 1. 3 languages
Write a script that prints 3 lines:

- The first line: `“C is fun”`
- The second line: `“Python is cool”`
- The third line: `“JavaScript is amazing”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

*File:* [1-multi_languages.js](1-multi_languages.js)
   
   
## 2. Arguments
Write a script that prints a message depending of the number of arguments passed:

- If no arguments are passed to the script, print `“No argument”`
- If only one argument is passed to the script, print `“Argument found”`
- Otherwise, print “Arguments found”
- You must use console.log(...) to print all output
- You are not allowed to use var
- **Reference:** [process.argv](https://nodejs.org/api/process.html#process_process_argv)

*File:* [2-arguments.js](2-arguments.js)
   
   
## 3. Value of my argument
Write a script that prints the first argument passed to it:

- If no arguments are passed to the script, print `“No argument”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `length`
 
*File:* [3-value_argument.js](3-value_argument.js)
   
   
## 4. Create a sentence
Write a script that prints two arguments passed to it, in the following format: `“ is ”`

- You must use `console.log(...)` to print all output
- You are not allowed to use var

*File:* [4-concat.js](4-concat.js)
   
   
## 5. An Integer
Write a script that prints My number: `<first argument converted in integer>` if the first argument can be converted to an integer:

- If the argument can’t be converted to an integer, print `“Not a number”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `try/catch`

*File:* [5-to_integer.js](5-to_integer.js)
   
   
## 6. Loop to languages
Write a script that prints 3 lines: `(like 1-multi_languages.js)` but by using an array of string and a loop

- The first line: `“C is fun”`
- The second line: `“Python is cool”`
- The third line: `“JavaScript is amazing”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use any `if/else` statement
- You can use only one `console.log`
- You must use a loop `(while, for, etc.)`

*File:* [6-multi_languages_loop.js](6-multi_languages_loop.js)
   
   
## 7. I love C
Write a script that prints x times `“C is fun”`

- Where `x` is the first argument of the script
- If the first argument can’t be converted to an integer, print `“Missing number of occurrences”`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You can use only two `console.log`
- You must use a loop `(while, for, etc.)`

*File:* [7-multi_c.js](7-multi_c.js)
   
   
## 8. Square
Write a script that prints a square

- The first argument is the size of the square
- If the first argument can’t be converted to an integer, print `“Missing size”`
- You must use the character `X` to print the square
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You must use a loop `(while, for, etc.)`

*File:* [8-square.js](8-square.js)
   
   
## 9. Add
Write a script that prints the addition of 2 integers

- The first argument is the `first integer`
- The second argument is the `second integer`
- You have to define a function with this prototype: `function add(a, b)`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

*File:* [9-add.js](9-add.js)
   
   
## 10. Factorial
Write a script that computes and prints a factorial

- The first argument is integer `(argument can be cast as integer)` used for computing the factorial
- Factorial of `NaN` is `1`
- You must do it recursively
- You must use a function
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

*File:* [10-factorial.js](10-factorial.js)
   
   
## 11. Second biggest!
Write a script that searches the second biggest integer in the list of arguments.

- You can assume all arguments can be converted to integer
- If no argument passed, print `0`
- If the number of arguments is `1`, print `0`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`

*File:* 11-second_biggest.js(11-second_biggest.js)
  
  
## 12. Object
Update this script to replace the value `12` with `89`:

- You are not allowed to use `var`
```Javascript
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);
```

```Shell
$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
```
*File:* [12-object.js](12-object.js)
   
   
## 13. Add file
Write a function that returns the addition of 2 integers.

- The function must be visible from outside
- The name of the `function` must be `add`
- You are not allowed to use var

*File:* [13-add.js](13-add.js)
  
  
## 14. Const or not const
Write a file that modifies the value of `myVar` to `333`

```Javascript
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
```

```Shell
$ ./100-main.js
333
```

**Hint:** Scope

*File:* [100-let_me_const.js](100-let_me_const.js)
  
## 15. Call me Moby
Write a function that executes x times a function.

- The function must be `visible` from `outside`
- Prototype: `function (x, theFunction)`
- You are not allowed to use `var`


```Javascript
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
```

```Shell
$ ./101-main.js
C is fun
C is fun
C is fun
```

*File:* [101-call_me_moby.js](101-call_me_moby.js)
   
   
## 16. Add me maybe
Write a function that increments and calls a function.

- The function must be `visible` from `outside`
- Prototype: `function (number, theFunction)`
- You are not allowed to use `var`

```Javascript
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
```

```Shell
$ ./102-main.js
New value: 5
```

*File:* [102-add_me_maybe.js](102-add_me_maybe.js)
   
## 17. Increment object
Update this script by adding a new function `incr` that increments the integer `value`.

- You are not allowed to use `var`

```Javascript
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
```

```Shell
$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
```

*File:* [103-object_fct.js](103-object_fct.js)

