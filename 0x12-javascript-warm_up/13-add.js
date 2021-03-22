#!/usr/bin/node
/*
 Function that returns the addition of 2 integers
*/

function add (num1, num2) {
  return (num1 + num2);
}
// With NodeJS modules, to make something public, you have to export it
module.exports.add = add;
