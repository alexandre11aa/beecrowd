var input = require("fs").readFileSync("/dev/stdin", "utf8");

var A = (3.14159 * parseFloat(input)**2).toFixed(4);

console.log('A=' + A)