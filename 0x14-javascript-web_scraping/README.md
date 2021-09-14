# 0x14. JavaScript - Web scraping

**Useful links**
- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
- [request module](https://github.com/request/request)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)
- [NodeJS File System](https://nodejs.org/api/fs.html#fs_filehandle_writefile_data_options)
- [request npm module](https://github.com/request/request)

**Install nodeJS**
```shell
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

**Install semi-standard**
```shell
$ sudo npm install semistandard --global
```

**Install request**
```shell
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks
## 0. Readme
Write a script that reads and prints the content of a file.

- The first argument is the `file path`
- The content of the file must be read in `utf-8`
- If an error occurred during the reading, print the `error object`

```shell
$ cat cisfun
C is super fun!
$ ./0-readme.js cisfun
C is super fun!

$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
$
```

`File:` [0-readme.js](0-readme.js|)


## 1. Write me
Write a script that writes a string to a file.

- The first argument is the `file path`
- The second argument is the string to write
- The content of the file must be written in utf-8
- If an error occurred during while writing, print the `error object`

```shell
$ ./1-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt ; echo ""
Python is cool
$
```

`File:` [1-writeme.js](1-writeme.js)


## 2. Status code
Write a script that display the status code of a `GET` request.

- The first argument is the `URL` to request
- The status code must be printed like this: `code: <status code>`
- You must use the module `request`

```shell
$ ./2-statuscode.js https://intranet.hbtn.io/status
code: 200
$ ./2-statuscode.js https://intranet.hbtn.io/doesnt_exist
code: 404
$
```

`File:` [2-statuscode.js](2-statuscode.js)


## 3. Star wars movie title
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

- The first argument is the `movie ID`
- You must use the `Star wars API` with the endpoint [!https://swapi-api.hbtn.io/api/films/:id]

```shell
$ ./3-starwars_title.js 1
A New Hope
$ ./3-starwars_title.js 5
Attack of the Clones
$
```

`File:` [3-starwars_title.js](3-starwars_title.js)


## 4. Star wars Wedge Antilles
Write a script that prints the number of movies where the character `“Wedge Antilles”` is present.

- The first argument is the API URL of the Star wars API: [!https://swapi-api.hbtn.io/api/films/]
 - Wedge Antilles is character ID `18`

```shell
$ ./4-starwars_count.js https://swapi-api.hbtn.io/api/films
3
$
```

`File:` [4-starwars_count.js](4-starwars_count.js)


## 5. Loripsum
Write a script that gets the contents of a webpage and stores it in a file.

- The first argument is the `URL` to request
- The second argument the `file path` to store the `body response`
- The file must be `UTF-8` encoded

```shell
$ ./5-request_store.js http://loripsum.net/api loripsum
$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>

...
$
```

`File:` [5-request_store.js](5-request_store.js)


## 6. How many completed?
Write a script that computes the number of tasks completed by `user id`.

- The first argument is the `API URL`: [!https://jsonplaceholder.typicode.com/todos]
- Only print users with completed task

```shell
$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
$
```

`File:` [6-completed_tasks.js](6-completed_tasks.js)


## 7. Who was playing in this movie?
Write a script that prints all characters of a Star Wars movie:

- The first argument is the `Movie ID`
- Display one character name by line

```shell
$ ./100-starwars_characters.js 3
Darth Vader
R2-D2
Luke Skywalker
Han Solo
Leia Organa
Chewbacca
Palpatine
Obi-Wan Kenobi
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Boba Fett
Ackbar
Arvel Crynyd
Mon Mothma
Nien Nunb
Wicket Systri Warrick
Bib Fortuna
C-3PO
Lando Calrissian
$
```

`File:` [100-starwars_characters.js](100-starwars_characters.js)


## 8. Right order
Write a script that prints all characters of a Star Wars movie:

- The first argument is the `Movie ID`
- Display one character name by line **in the same order** of the list `“characters”` in the `/films/` response

```shell
$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
$
```

`File:` [101-starwars_characters.js](101-starwars_characters.js)
