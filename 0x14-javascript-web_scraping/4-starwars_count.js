#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (err) throw err;
  let count = 0;
  const film = JSON.parse(body).results;
  for (const movie of film) {
    for (const char of movie.characters) {
      if (char.endsWith('18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
