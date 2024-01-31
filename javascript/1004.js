var input = require("fs").readFileSync("/dev/stdin", "utf8");

var variaveis = input.split('\n');
    
var A = parseInt(variaveis.shift());
var B = parseInt(variaveis.shift());
   
console.log("PROD = " + (A * B));