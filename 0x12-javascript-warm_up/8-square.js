#!/usr/bin/node
const Var = process.argv[2];
if (isNaN(Var)) {
  console.log('Missing size');
} else {
  for (let c = 0; c < Var; c++) {
    console.log('X'.repeat(Var));
  }
}
