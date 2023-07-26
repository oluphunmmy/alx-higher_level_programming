#!/usr/bin/node
/*  a script that writes a string to a file. */
const arg = process.argv;
const fs = require('fs');

fs.writeFile(arg[2], arg[3], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
