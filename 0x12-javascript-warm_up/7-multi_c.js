#!/usr/bin/node
const Var = process.argv[2];
if (isNaN(Var)) {
  console.log.log('Missing number of occurrences');
} else {
  for (let c = 0; c < Var; c++) {
    console.log('C is fun');
  }
}
