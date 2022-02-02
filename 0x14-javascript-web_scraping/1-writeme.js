#!/usr/bin/node
//  script that writes a string to a file.

const file = process.argv[2];
const fs = require('fs');
const w = process.argv[3];

fs.writeFile(file, w, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
