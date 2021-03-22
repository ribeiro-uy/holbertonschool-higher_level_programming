#!/usr/bin/node
/*
  Function that increments and calls a function.
*/

function addMeMaybe (number, theFunction) {
  theFunction(++number);
}
module.exports.addMeMaybe = addMeMaybe;
