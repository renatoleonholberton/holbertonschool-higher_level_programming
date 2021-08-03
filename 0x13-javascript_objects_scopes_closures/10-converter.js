#!/usr/bin/node

exports.converter = function (base) {
  function convertDigit (digit) {
    if (digit < 10) {
      return digit;
    }

    if (digit === 10) {
      return 'a';
    }
    if (digit === 11) {
      return 'b';
    }
    if (digit === 12) {
      return 'c';
    }
    if (digit === 13) {
      return 'd';
    }
    if (digit === 14) {
      return 'e';
    }
    if (digit === 15) {
      return 'f';
    }

    return digit;
  }

  return function conv (num) {
    if (num === 0) {
      return '0';
    }

    this.val = conv(Math.floor(num / base));
    if (this.val === '0') {
      this.val = '';
    }

    return `${this.val}${convertDigit(num % base)}`;
  };
};
