#!/usr/bin/node
/*
 * a class Square that defines a square and inherits from Square
 * Creates an instance method called charPrint(c) that prints the rectangle using the character c
 * If c is undefined, use the character X
 */

const Square1 = require('./5-square.js');
class Square extends Square1 {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
