#!/usr/bin/node

const argv = require('process').argv;
const rq = require('request');

const id = argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

rq(url, function (err, res, body) {
  if (err) { return; }

  const film = JSON.parse(body);
  for (const curl of film.characters) {
    rq(curl, (cerr, cdata, cbody) => {
      if (err) { return; }

      const actor = JSON.parse(cbody);
      console.log(actor.name);
    });
  }
});
