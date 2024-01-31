#!/usr/bin/node

const request = require(request);
const movieId = process.argv[2];
API = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
    if (error) {
        console.error(error);
    } else {
        console.log(JSON.parse(body).title);
    }
});