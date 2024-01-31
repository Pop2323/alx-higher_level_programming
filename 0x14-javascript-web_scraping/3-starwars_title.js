#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const API = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(API, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
