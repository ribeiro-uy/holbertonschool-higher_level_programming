#!/usr/bin/node
/*
  Prints 3 lines: but by using an array of string and a loop
*/

let i = 0;
const argument = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
while (argument[i]) {
  console.log(argument[i]);
  i++;
}
