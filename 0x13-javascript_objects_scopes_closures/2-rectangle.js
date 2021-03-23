#!/usr/bin/node
/*
  Task 2:
  Class Rectangle that defines a rectangle
*/
module.exports = class Rectangle {
  // Constructor
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
