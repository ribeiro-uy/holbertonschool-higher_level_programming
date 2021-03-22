#!/usr/bin/node
/*
  Prints two arguments passed to it, in the following format: “ is ”
*/

const argument = [];
process.argv.forEach((val, index) => {
  argument[index] = val;
});
console.log(argument[2] + ' is ' + argument[3]);
