#!/usr/bin/node

const argv = require('process').argv;
let max = Number(argv[2]);
let secMax = 0;

if (argv.length > 3) {
  for (let i = 3; i < argv.length; i++) {
    if (Number(argv[i - 1]) > max) {
      max = Number(argv[i - 1]);
    }
    if (Number(argv[i]) > secMax && Number(argv[i]) <= max) {
      secMax = Number(argv[i]);
    }
  }
}

console.log(secMax);
