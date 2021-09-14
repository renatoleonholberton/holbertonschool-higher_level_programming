#!/usr/bin/node

const argv = require('process').argv;
const fs = require('fs');

const filepath = argv[2];
const data = argv[3];
fs.writeFile(filepath, data, 'utf8', function (err, data) {
  if (err) { console.log(err); }
});
