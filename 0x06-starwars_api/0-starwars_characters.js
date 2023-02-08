#!/usr/bin/node

const request = require('request');
const ApiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const filmID = process.argv[2];
const movieUrl = `${ApiUrl}${filmID}/`;

request(movieUrl, async (err, response, body) => {
  if (!err) {
    const characters = JSON.parse(body);
    for (const charID in characters) {
      await new Promise((resolve, reject) => {
        request(characters[charID], (err, response, body) => {
          if (!err) {
            const character = JSON.parse(body);
            console.log(character.name);
            resolve();
          }
        });
      });
    }
  }
});
