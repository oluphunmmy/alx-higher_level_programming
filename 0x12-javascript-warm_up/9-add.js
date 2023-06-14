#!/usr/bin/node

const argv2 = parseInt(process.argv[2]);
const argv3 = parseInt(process.argv[3]);
function add (a, b) {
  return (a + b);
}
console.log(add(argv2, argv3));
