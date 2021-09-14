#!/usr/bin/node

const argv = require('process').argv;
const rq = require('request');

const id = argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

rq(url, function (err, res, body) {
  if (err) { return; }

  const film = JSON.parse(body);
  console.log(film.title);
});
