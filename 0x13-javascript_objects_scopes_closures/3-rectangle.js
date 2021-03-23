#!/usr/bin/node
/*
  Task 3:
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

  // Prints the rectangle using the character X
  print () {
    for (let index = 0; index < this.height; index++) {
      console.log('X'.repeat(this.width));
    }
  }
};
