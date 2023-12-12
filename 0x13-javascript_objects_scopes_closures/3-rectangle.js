#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let print = '';
    for (let row = 0; row < this.width; row++) {
      for (let col = 0; col < this.height; col++) {
        print = print + 'X';
      }
      console.log(print);
      print = '';
    }
  }
}

module.exports = Rectangle;
