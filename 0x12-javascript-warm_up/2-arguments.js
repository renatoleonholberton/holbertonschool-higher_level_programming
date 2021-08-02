#!/usr/bin/node

const argv = require('process').argv;
let msg = 'No argument';

if (argv.length === 3) {
  msg = 'Argument found';
} else if (argv.length > 3) {
  msg = 'Arguments found';
}

console.log(msg);
