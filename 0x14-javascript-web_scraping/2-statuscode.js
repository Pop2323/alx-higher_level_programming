#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request.get(URL, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
