#!/usr/bin/node
/*
  Task 6:
  Class Square that defines a square and inherits from Rectangle of 4-rectangle
*/

const oldSquare = require('./5-square');
module.exports = class Square extends oldSquare {
  charPrint (c) {
    if (c === undefined) { super.print(); } else {
      for (let index = 0; index < this.width; index++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
