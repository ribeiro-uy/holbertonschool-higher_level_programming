#!/usr/bin/node
/*
  Script that searches the second biggest integer in the list of arguments.
*/

const argument = [];
const lastIndex = process.argv.length;
process.argv.forEach((val, index) => {
  argument[index] = val;
});
argument.sort();
console.log(parseInt(argument[lastIndex - 2]));
// -2 because the length doesn't take the 0 index
