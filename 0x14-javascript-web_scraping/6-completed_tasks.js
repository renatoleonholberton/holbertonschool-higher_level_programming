#!/usr/bin/node

const argv = require('process').argv;
const rq = require('request');

const url = argv[2];

rq(url, function (err, res, body) {
  if (err) { return; }

  const todos = JSON.parse(body);
  console.log(todos.reduce((acc, el) => {
    if (el.completed) {
      const count = acc[el.userId] || 0;
      acc[el.userId] = count + 1;
    }
    return acc;
  }, {}));
});
