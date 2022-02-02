#!/usr/bin/node
// script that display the status code of a GET request.

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else console.log('code:', response && response.statusCode);
});
