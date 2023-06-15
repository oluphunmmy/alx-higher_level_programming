#!/usr/bin/node
/* a class Rectangle that defines a rectangle
 * The constructor must take 2 arguments w and h
 * Initializes the instance attribute width with the value of w
 * Initializes the instance attribute height with the value of h
 */

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
