#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];
const fs = require('fs');

request(url).pipe(fs.createWriteStream(filename));
