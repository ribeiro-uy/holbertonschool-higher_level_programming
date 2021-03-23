#!/usr/bin/node
/*
  Task 5:
  Class Square that defines a square and inherits from Rectangle of 4-rectangle
*/

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  // Constructor
  constructor (size) {
    super(size, size);
  }
};
