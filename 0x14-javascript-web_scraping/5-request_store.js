#!/usr/bin/node
// Contents of webpage and stores in a file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(file, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
