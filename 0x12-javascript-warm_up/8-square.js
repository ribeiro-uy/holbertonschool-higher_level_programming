#!/usr/bin/node
/*
  Script that prints a square
*/

let numArguments = 0;
let printNum;
let times;
process.argv.forEach((val, index) => {
  numArguments++;
  if (numArguments === 3) {
    printNum = val;
  }
});
if (numArguments === 2) console.log('Mising size');
else if (isNaN(parseInt(printNum))) console.log('Missing size');
const temp = printNum;
while (printNum > 0) {
  times = temp;
  while (times > 0) {
    process.stdout.write('X');
    times--;
  }
  console.log();
  printNum--;
}
