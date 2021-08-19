# 0x10. Python - Network #0

**Useful links**
- [Common HTTP headers](https://www.whitehatsec.com/blog/list-of-http-response-headers/)
- [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)


## Tasks
## 0. cURL body size
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

- The size must be displayed in bytes
- You have to use `curl`

`File:` [0-body_size.sh](0-body_size.sh)


## 1. cURL to the end
Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response

- Display `only` body of a `200` status code `response`
- You have to use `curl`

`File:` [1-body.sh](1-body.sh)


## 2. cURL Method
Write a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response

`File:` [2-delete.sh](2-delete.sh)


## 3. cURL only methods

Write a Bash script that takes in a URL and displays all `HTTP methods` the server will accept.

`File:` [3-methods.sh](3-methods.sh)


## 4. cURL headers
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

- A header variable `X-HolbertonSchool-User-Id` must be sent with the `value` `98`
- You have to use `curl`

`File:` [4-header.sh](4-header.sh)


## 5. cURL POST parameters
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

- A variable email must be sent with the value `hr@holbertonschool.com`
- A variable subject must be sent with the value `I will always be here for PLD`
- You have to use `curl`

`File:` [5-post_params.sh](5-post_params.sh)


## 6. Find a peak
Write a function that finds a peak in a list of unsorted integers.

- Prototype: `def find_peak(list_of_integers):`
- You are not allowed to import any module
- Your algorithm must have the lowest complexity
- `6-peak.py` must contain the function
- `6-peak.txt` must contain the complexity of your algorithm

**Note:** there may be more than one peak in the list

`File:` [6-peak.py, 6-peak.txt](6-peak.py, 6-peak.txt)


## 7. Only status code
Write a Bash script that sends a request to a URL passed as an argument, and displays only the `status code` of the response.

- Not allowed to use any pipe, redirection, etc.
- Not allowed to use `;` and `&&`
- Have to use `curl`

`File:` [100-status_code.sh](100-status_code.sh)


## 8. cURL a JSON file
Write a Bash script that sends a `JSON POST` request to a URL passed as the first argument, and displays the body of the response.

- Your script must send a `POST` request with the `contents` of a `file`, passed with the `filename` as the `second argument` of the script, in the body of the request
- You have to use `curl`

`File:` [101-post_json.sh](101-post_json.sh)


## 9. Catch me if you can!
Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.

- Have to use `curl`
- Not allow to use `echo`, `cat`, etc. to display the final result

```shell
$ ./102-catch_me.sh ; echo ""
You got me!
$
```

`File:` [102-catch_me.sh](102-catch_me.sh)
