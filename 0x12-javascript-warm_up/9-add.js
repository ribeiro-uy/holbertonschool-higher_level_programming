#!/usr/bin/node
/*
  Script that prints the addition of 2 integers
*/

const argument = [];

process.argv.forEach((val, index) => {
  argument[index] = val;
});
console.log(parseInt(argument[2]) + parseInt(argument[3]));
