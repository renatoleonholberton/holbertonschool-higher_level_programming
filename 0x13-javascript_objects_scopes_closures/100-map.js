#!/usr/bin/node

const ls = require('./100-data.js').list;

console.log(ls);
console.log(ls.map((ind, el) => el * ind));
