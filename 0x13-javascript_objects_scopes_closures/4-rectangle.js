#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let r, c;
    for (c = 0; c < this.height; c++) {
      let res = '';
      for (r = 0; r < this.width; r++) {
        res += 'X';
      }
      console.log(res);
    }
  }

  rotate () {
    let temp = 0;
    temp = this.height;
    temp.height = temp.width;
    temp.width = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
