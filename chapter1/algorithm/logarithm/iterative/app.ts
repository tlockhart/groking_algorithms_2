// time complexity: O(n) 
const logarithm = (base, items) => {
    let quotient = 0;
    let divisions = 0;

    while (quotient !== 1) {
        quotient = items/base;
        console.log("Quotient = ", quotient);
        items = quotient;
        divisions++;
    }
    return divisions;
}

const items = 8;
console.log("How many divisions are possible?", logarithm(2, items));