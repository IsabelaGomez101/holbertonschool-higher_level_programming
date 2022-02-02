#!/usr/bin/node
// script that prints all characters of a Star Wars movie.

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (error) {
          console.error('error:', error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
