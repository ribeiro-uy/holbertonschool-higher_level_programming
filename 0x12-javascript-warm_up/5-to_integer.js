#!/usr/bin/node
/*
  Prints two arguments passed to it, in the following format: “ is ”
*/

let numArguments = 0;
const argument = [];

process.argv.forEach((val, index) => {
  numArguments += 1;
  argument[index] = val;
});
if (numArguments === 2) console.log('Not a number');
else if (numArguments === 3) {
  if (isNaN(parseInt(argument[2]))) console.log('Not a number');
  else console.log('My number: ' + parseInt(argument[2]));
}
