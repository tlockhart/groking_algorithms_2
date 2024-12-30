"use strict";
function isPalindrome(totalChars, lastIdx, str) {
    console.log(`lastIdx: ${lastIdx}; char: ${str[lastIdx]}`);
    // const curIdx = lastIdx;
    let highIdx = lastIdx;
    const lowIdx = totalChars - 1 - highIdx;
    // Base Case: 
    /*If we have gotten to the middle letter, or if there is 1 element, or no elements, or indexes crossed then we know the word is a palindrome*/
    if (lowIdx >= highIdx)
        return true;
    //if the letters do not match then return false and end the recursive call
    if (str[lowIdx] !== str[highIdx])
        return false;
    // Recursive Case:
    return isPalindrome(totalChars, highIdx - 1, str);
}
console.log("a is Palindrome: " + isPalindrome("a".length, "a".length - 1, "a"));
console.log("motor is Palindrome: " + isPalindrome("motor".length, "motor".length - 1, "motor"));
console.log("rotor is Palindrome: " + isPalindrome("rotor".length, "rotor".length - 1, "rotor"));
/********* To Screen:  ************/
const container = document.getElementById("container");
// ✅ Append HTML to `div` element
container.insertAdjacentHTML('afterend', `<div style="background-color: lime">a is Palindrome: ${isPalindrome("a".length, "a".length - 1, "a")}</div>`);
// ✅ Append HTML to `div` element
container.insertAdjacentHTML('afterend', `<div style="background-color: lime">motor is Palindrome: ${isPalindrome("motor".length, "motor".length - 1, "motor")}</div>`);
// ✅ Append HTML to `div` element
container.insertAdjacentHTML('afterend', `<div style="background-color: lime">rotor is Palindrome: ${isPalindrome("rotor".length, "rotor".length - 1, "rotor")}</div>`);
