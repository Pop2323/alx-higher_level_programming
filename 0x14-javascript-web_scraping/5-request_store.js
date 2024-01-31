#!/usr/bin/node

const fs = require("fs");
const request = require("request");

const requestURL = process.argv[2];
const fileName = process.argv[3];

request(requestURL, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        fs.writeFile(fileName, body, (err) => {
            if (err) {
                console.log(err);
            }
        });
    }
});

