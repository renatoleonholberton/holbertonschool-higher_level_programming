#!/usr/bin/node

const argv = require('process').argv;
const fs = require('fs');
const rq = require('request');

const url = argv[2];
const filepath = argv[3];

rq(url, function (err, data, body) {
  if (err) { return; }

  fs.writeFile(filepath, body, 'utf8', function (werr, wdata) {});
});
