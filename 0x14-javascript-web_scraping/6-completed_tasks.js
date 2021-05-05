#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (response.statusCode === 200) {
    const done = {};
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (task.userId in done) {
          done[task.userId] += 1;
        } else {
          done[task.userId] = 1;
        }
      }
    }
    console.log(done);
  }
});
