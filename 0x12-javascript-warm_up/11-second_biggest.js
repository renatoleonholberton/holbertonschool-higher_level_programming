#!/usr/bin/node

const argv = require('process').argv;
let max = Number(argv[2]);
let secMax = 0;

if (argv.length > 3) {
  for (const num of argv) {
    if (Number(num) > max) {
      secMax = max;
      max = Number(num);
    }
  }
}

console.log(secMax);
