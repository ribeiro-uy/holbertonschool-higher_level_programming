#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];
request(url, function (response, body) {
  fs.writeFile(fileName, body.body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
