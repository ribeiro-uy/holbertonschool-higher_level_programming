#!/usr/bin/node
/*
  Script that searches the second biggest integer in the list of arguments.
*/

const argument = [];
const lastIndex = process.argv.length;
let newArgument = [];

process.argv.forEach((val, index) => {
  argument[index] = val;
});
newArgument = [...new Set(argument)];
newArgument.sort((a, b) => a - b);
if (lastIndex <= 2)
  console.log(0);
else if (lastIndex === 3)
  console.log(0);
else
  console.log(parseInt(newArgument[lastIndex - 2]));
  // -2 because the length doesn't take the 0 index
