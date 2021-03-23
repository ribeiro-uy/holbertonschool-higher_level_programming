#!/usr/bin/node
/*
  Task 9:
  Function that prints the number of arguments already printed and the new argument value.
*/

let numArguments = 0;
exports.logMe = (item) => {
  console.log(`${num}: ${item}`);
  numArguments++;
};
