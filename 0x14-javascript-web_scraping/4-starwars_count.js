#!/usr/bin/node

const argv = require('process').argv;
const rq = require('request');

const url = argv[2];

rq(url, function (err, res, body) {
  if (err) { return; }

  const films = JSON.parse(body);

  let count = 0;
  for (const film of films.results) { count += film.characters.reduce((acc, el) => el.match(/.*18.*/g) ? acc + 1 : acc, 0); }

  console.log(count);
});
