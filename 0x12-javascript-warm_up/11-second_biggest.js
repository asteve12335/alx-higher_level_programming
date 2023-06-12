#!/usr/bin/node

if (process.argv.length > 3) {
  const lst = process.argv.slice(2).map(Number);

  lst.splice(lst.indexOf(Math.max.apply(null, lst)), 1);
  console.log(Math.max.apply(null, lst));
} else {
  console.log(0);
}
