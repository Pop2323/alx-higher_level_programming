#!/usr/bin/node

const preSquare = require('./5-square');

class square extends preSquare {
  charPrint (c) {
    if (c) {
      let res = '';
      for (let i = 0; i < this.height; i++) {
        for (let y = 0; y < this.height; y++) {
          res = res + 'X';
        }
        console.log(res);
        res = '';
      }
    } else {
      super.res();
    }
  }
}

module.exports = square;
