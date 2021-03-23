#!/usr/bin/node
/*
  Task 10:
  Converts a number from base 10 to another base passed as argument
*/

exports.converter = (base) => {
  return num => num.toString(base);
};
