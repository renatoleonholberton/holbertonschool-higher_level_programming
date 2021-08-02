#!/usr/bin/node

const argv = require('process').argv;
const num = Math.floor(Number(argv[2]));

if (isNaN(num)) {
  console.log('Missing size');
} else {
  let row = '';
  for (let i = 0; i < num; i++) {
    row += 'X';
  }
  for (let i = 0; i < num; i++) {
    console.log(row);
  }
}
