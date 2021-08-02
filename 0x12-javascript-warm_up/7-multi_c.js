#!/usr/bin/node

const argv = require('process').argv;
let num = Math.floor(Number(argv[2]));

if (!isNaN(num)) {
  while (num-- > 0) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of ocurrences');
}
