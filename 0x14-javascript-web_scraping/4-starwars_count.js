#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
const endPoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request({ url: endPoint, methods: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err)
  } else if (body) {
    // Wedge Antilles is character ID 18 - use this ID for filtering the
    // result of the API
    const json = JSON.parse(body);
    const charFilms = json.results.filter(
      x => x.characters.find(y => y.match(/\/people\/18\/?$/))
    );
    console.log(charFilms.length);
  }
});
