#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = body.toString();
  fs.writeFile(file, data, 'utf8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
