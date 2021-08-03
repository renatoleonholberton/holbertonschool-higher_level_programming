#!/usr/bin/node

const argv = require('process').argv;
const fs = require('fs');

const d1 = fs.readFileSync(argv[2]);
const d2 = fs.readFileSync(argv[3]);

fs.writeFileSync(argv[4], d1 + d2);

/*
fs.readFile(argv[2], 'utf-8', (err, data) => {
  if (err) {
    return;
  }

  fs.readFile(argv[3], 'utf-8', (err2, data2) => {
    if (err2) {
      return;
    }

    fs.writeFile(argv[4], data + data2, () => {});
  })
})
*/
