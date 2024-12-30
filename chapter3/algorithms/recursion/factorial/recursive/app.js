function factorial(n) {
    // base case: 
    if (n === 0) {
        return 1;
    }
    // recursive case:
    var subFact = n * factorial(n - 1);
    console.log("SubFact:" + subFact);
    return subFact;
}
;
console.log("The value of 0! is " + factorial(0) + ".", "; Answer: 1");
console.log("The value of 5! is " + factorial(5) + ".", "; Answer: 120");
