#!/usr/bin/node
const add1 = process.argv[2];
const add2 = process.argv[3];
function add (a, b) {
  console.log(a + b);
}
add(add1, add2);
