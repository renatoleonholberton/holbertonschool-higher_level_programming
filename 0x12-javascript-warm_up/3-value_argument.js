#!/usr/bin/node

const argv = require('process').argv;
let msg = 'No argument';

if (typeof argv[2] !== 'undefined') {
  msg = argv[2];
}

console.log(msg);
