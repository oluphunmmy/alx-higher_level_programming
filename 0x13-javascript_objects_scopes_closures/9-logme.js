#!/usr/bin/node
/* function that prints the number of arguments already printed and the new
 * argument value */

let c = 0;
exports.logMe = function (item) {
  console.log(c + ': ' + item);
  c++;
};
