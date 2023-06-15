#!/usr/bin/node
/*
 * a function that returns the reversed version of a list:
 * ou are not allow to use the built-in method reverse
 */

exports.esrever = function (list) {
  const res = [];
  for (let i = list.length - 1; i >= 0; i--) {
    res.push(list[i]);
  }
  return res;
};
