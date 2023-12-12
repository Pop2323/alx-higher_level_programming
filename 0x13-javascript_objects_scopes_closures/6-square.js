#!/usr/bin/node

const PreSquare = require('./5-square');

class Square extends PreSquare {
  charPrint (c) {
    if (c) {
      let res = '';
      for (let i = 0; i < this.height; i++) {
        for (let y = 0; y < this.width; y++) {
          res = res + 'X';
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
