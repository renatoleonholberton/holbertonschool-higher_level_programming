#!/usr/bin/node

const argv = require('process').argv;
const rq = require('request');

const id = argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

function printActors (actorsUrls, i) {
  if (i >= actorsUrls.length) { return; }

  const curl = actorsUrls[i];
  rq(curl, (err, data, body) => {
    if (err) { return; }

    const actor = JSON.parse(body);
    console.log(actor.name);

    printActors(actorsUrls, i + 1);
  });
}

rq(url, function (err, res, body) {
  if (err) { return; }

  const film = JSON.parse(body);
  printActors(film.characters, 0);
});
