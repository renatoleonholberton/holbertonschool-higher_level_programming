#!/usr/bin/node

const Sq = require('./5-square.js');

class Square extends Sq {
  charPrint (c = 'X') {
    if (!this.size) {
      return;
    }

    let side = '';

    for (let i = 0; i < this.size; i++) {
      side += c;
    }
    for (let i = 0; i < this.size; i++) {
      console.log(side);
    }
  }
}

module.exports = Square;
