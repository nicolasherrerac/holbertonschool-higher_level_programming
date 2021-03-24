#!/usr/bin/node
const fs = require('fs');
const a = fs.readFile(process.argv[2], 'utf8');
const b = fs.readFile(process.argv[3], 'utf8');
fs.writeFile(process.argv[4], a + b);
