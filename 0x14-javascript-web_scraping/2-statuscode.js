#!/usr/bin/node
const request = require('request');
const http = process.argv[2];
request.get(http).on('response', function (response) {
  console.log('code:', response.statusCode);
});
