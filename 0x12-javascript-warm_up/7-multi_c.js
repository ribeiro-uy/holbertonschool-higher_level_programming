#!/usr/bin/node
/*
  Script that prints x times “C is fun”
*/

let numArguments = 0;
let printNum;

process.argv.forEach((val, index) => {
  numArguments += 1;
  if (numArguments === 3) {
    printNum = val;
  }
});
while (printNum > 0) {
  console.log('C is fun');
  printNum--;
}
