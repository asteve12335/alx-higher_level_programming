#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    const char_Array = [];

    for (let i = 0; i < this.width; i++) {
      char_Array.push(c.repeat(this.width));
    }

    console.log(char_Array.join('\n'));
  }
};
