#!/usr/bin/node

const argv = require('process').argv;
const rq = require('request');
const url = argv[2];

rq(url, function (err, res, body) {
  console.log(`code: ${res && res.statusCode}`);
});
