function sum(numbers: number[]):number {

// Base Case: 
if(numbers.length === 1) {
    return numbers[0];
}
if(numbers.length === 0 ) {
    return 0;
}


// Recursive Case:
const firstElement = numbers.shift()!;
return firstElement + sum(numbers);
}

const numbers = [1,2,3,4];

console.log("sum: " + sum(numbers));


/********* To Screen:  ************/
// const container: HTMLElement | null = document.getElementById("container")!

// // ✅ Append HTML to `div` element
// container.insertAdjacentHTML(
//     'afterend',
//     `<div style="background-color: lime">a is Palindrome: ${ isPalindrome("a".length, "a".length-1, "a")}</div>`,
// )

// // ✅ Append HTML to `div` element
// container.insertAdjacentHTML(
//     'afterend',
//     `<div style="background-color: lime">motor is Palindrome: ${isPalindrome("motor".length, "motor".length-1,"motor")}</div>`,
// )

// // ✅ Append HTML to `div` element
// container.insertAdjacentHTML(
//     'afterend',
//     `<div style="background-color: lime">rotor is Palindrome: ${isPalindrome("rotor".length, "rotor".length-1,"rotor")}</div>`,
// )