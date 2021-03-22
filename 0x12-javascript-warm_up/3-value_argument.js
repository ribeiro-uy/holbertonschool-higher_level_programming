#!/usr/bin/node
/*
  Prints the first argument passed to it
*/

let numArguments = 0;
let argument = '';
process.argv.forEach((val, index) => {
  numArguments += 1;
  argument = val;
});
if (numArguments >= 3) console.log(argument);
else if (numArguments === 2) console.log('No argument');
