#!/usr/bin/node

let argInt = parseInt(process.argv[2]);
if (isNaN(argInt)) {
  console.log('Missing number of occurrences');
} else {
  while (argInt > 0) {
    console.log('C is fun');
    argInt--;
  }
}
