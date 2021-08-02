#!/usr/bin/node

const argv = require('process').argv;
let max = Number(argv[2]);
let secMax = 0;

if (argv.length > 3) {
  for (let i = 3; i < argv.length; i++) {
    const num = Number(argv[i]);

    if (num > max) {
      secMax = max;
      max = num;
    } else if (num > secMax) {
      secMax = num;
    }
  }
}

console.log(secMax);
