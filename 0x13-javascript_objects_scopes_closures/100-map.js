#!/usr/bin/node
/*
 * a script that imports an array and computes a new array.
 */

const array = require('./100-data').list;
const newArray = array.map((num, index) => (num * index));

console.log(array);
console.log(newArray);
