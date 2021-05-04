#!/usr/bin/node
const request = require('request');
const urlId = process.argv[2];
request(urlId, function (response, body) {
  const filmList = (JSON.parse(body.body).results);
  let count = 0;
  for (const film in filmList) {
    for (const chars in filmList[film].characters) {
      if (filmList[film].characters[chars].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
