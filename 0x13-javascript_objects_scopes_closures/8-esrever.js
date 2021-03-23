#!/usr/bin/node
/*
  Task 8:
  Function that returns the reversed version of a list
*/

exports.esrever = function (list) {
  return list.map((item, idx) => list[list.length - 1 - idx]);
};
