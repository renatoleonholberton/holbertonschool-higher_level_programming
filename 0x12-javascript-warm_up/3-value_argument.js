#!/usr/bin/node

const argv = require('process').argv;
let msg = 'No argument';

if (argv[2]) {
  msg = argv[2];
}

console.log(msg);
