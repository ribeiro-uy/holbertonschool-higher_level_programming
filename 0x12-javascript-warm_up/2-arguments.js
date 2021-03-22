#!/usr/bin/node
/*
  That prints a message depending of the number of arguments passed
*/

let numArguments = 0;
process.argv.forEach((val, index) => {
  numArguments += 1;
});
if (numArguments === 3) console.log('Argument found');
else if (numArguments > 3) console.log('Arguments found');
else if (numArguments === 2) console.log('No argument');
