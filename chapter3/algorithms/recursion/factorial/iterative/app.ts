function factorial(n: number) {
  var result = 1;
  if(n === 0) {return 1;}
  
  for (var i = result; i <= n; i++) {
      result *= i;
  }

  return result;
};

console.log("The value of 5! should be " + 5*4*3*2*1, "; Answer: 120");
console.log("The value of 5! is " + factorial(5), "; Answer: 120");
console.log("The value of 0! should be 1", "; Answer: 1");
console.log("The value of 0! is " + factorial(0), "; Answer: 1");