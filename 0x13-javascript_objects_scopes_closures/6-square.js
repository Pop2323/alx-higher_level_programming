#!/usr/bin/node

const PreSquare = require('./5-square');

class Square extends PreSquare {
  charPrint (c) {
    if (c) {
      let res = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          res = res + c;
        }
        console.log(res);
        res = '';
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
