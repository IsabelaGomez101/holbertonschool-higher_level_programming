#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const url = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const body_ = JSON.parse(body);
    const result = body_.results;
    let nmovies = 0;
    let i;
    let j;
    for (i = 0; i < result.length; i++) {
      const c = (result[i].characters);
      for (j = 0; j < c.length; j++) {
        const id = c[j].endsWith('18/');
        if (id) {
          nmovies++;
        }
      }
    }
    console.log(nmovies);
  }
});
