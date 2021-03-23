#!/usr/bin/node
const add1 = parseInt(process.argv[2]);
const add2 = parseInt(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}
add(add1, add2);
