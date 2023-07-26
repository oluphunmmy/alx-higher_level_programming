#!/usr/bin/node
/* script that prints the number of movies where the character “Wedge Antilles”
is present The first argument is the API URL of the Star wars
API: https://swapi-api.hbtn.io/api/films/ Wedge Antilles is character ID 18
You must use the module request */

const arg = process.argv;
const requestURL = arg[2];
// const movieId = arg[3];
const req = require('request');
req(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const listFilms = (JSON.parse(body).results);
    let count = 0;
    for (let i = 0; i < listFilms.length; i++) {
      for (let j = 0; j < listFilms[i].characters.length; j++) {
        if (listFilms[i].characters[j].includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
