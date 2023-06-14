#!/usr/bin/node

const argInt = parseInt(process.argv[2]);
function fact (n) {
  if (n > 0) {
    return (n * fact(n - 1));
  } else if (n === 0) {
    return 1;
  }
}
if (isNaN(argInt)) {
  console.log(1);
} else {
  console.log(fact(argInt));
}
