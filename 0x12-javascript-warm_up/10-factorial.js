#!/usr/bin/node

const argv = require('process').argv;

function factorial (n) {
  if (isNaN(Number(n)) || n <= 1) {
    return 1;
  }

  return Number(n) * factorial(Number(n) - 1);
}

console.log(factorial(argv[2]));
