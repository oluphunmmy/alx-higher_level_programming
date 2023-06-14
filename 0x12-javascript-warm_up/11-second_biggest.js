#!/usr/bin/node

const array = process.argv.slice(2);
if (array.length < 2) {
  console.log('0');
} else {
  console.log(array.sort().reverse()[1]);
}
