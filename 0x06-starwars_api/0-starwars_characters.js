#!/usr/bin/node

const request = require('request');
const ApiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const filmID = process.argv[2];
const filmUrl = `${ApiUrl}${filmID}/`;

request(filmUrl, (err, response, body) => {
  if (!err) {
    const film = JSON.parse(body);
    const charactersUrls = film.characters;
    charactersUrls.forEach(url => {
      request(url, (err, response, body) => {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
