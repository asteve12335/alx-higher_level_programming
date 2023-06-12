#!/usr/bin/node
// prints the addition of 2 integers

const args = process.argv.slice(2);
const x = parseInt(args[0]);
const y = parseInt(args[1]);

function add (a, b) {
  console.log(a + b);
}

add(x, y);
