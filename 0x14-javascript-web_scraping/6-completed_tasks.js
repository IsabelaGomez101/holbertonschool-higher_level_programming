#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const body_ = JSON.parse(body);
    const users = {};
    let i;
    for (i = 0; i < body_.length; i++) {
      const status = (body_[i].completed);
      const id = body_[i].userId.toString();
      if (status) {
        if (users[id]) {
          users[id]++;
        } else {
          users[id] = 1;
        }
      }
    }
    console.log(users);
  }
});
