#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const inf = process.argv[3];

fs.writeFile(file, inf, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
