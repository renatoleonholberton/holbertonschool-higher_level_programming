#!/usr/bin/node

const argv = require('process').argv;
const num = Math.floor(Number(argv[2]));
let msg = 'Not a number';

if (!isNaN(num)) {
  msg = `My number: ${num}`;
}

console.log(msg);
