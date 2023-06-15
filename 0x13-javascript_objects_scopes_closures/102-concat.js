#!/usr/bin/node
//  a script that concats 2 files.

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const file = require('fs');
const textA = file.readFileSync(fileA, 'utf8');
const textB = file.readFileSync(fileB, 'utf8');
file.writeFileSync(fileC, textA + textB);
