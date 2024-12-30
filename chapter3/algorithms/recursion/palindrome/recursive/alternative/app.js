"use strict";
// Returns the first character of the string str
function firstCharacter(str) {
    return str.slice(0, 1);
}
;
// Returns the last character of a string str
function lastCharacter(str) {
    return str.slice(-1);
}
;
// Returns the string that results from removing the first
//  and last characters from str
function middleCharacters(str) {
    var newString = str.slice(1, -1);
    // console.log("NewString: " + newString);
    return newString;
}
;
function isPalindrome(str) {
    // base case #1
    if (str.length === 0 || str.length === 1) {
        return true;
    }
    // base case #2 Check the first and last char
    if (firstCharacter(str) !== lastCharacter(str)) {
        return false;
    }
    // recursive case
    return isPalindrome(middleCharacters(str));
}
;
var checkPalindrome = function (str) {
    console.log("Is this word a palindrome? " + str);
    var value = isPalindrome(str);
    console.log(value);
    return value;
};
console.log("a is Palindrome: " + checkPalindrome("a"));
// Program.assertEqual(isPalindrome("a"), true);
console.log("motor is Palindrome: " + checkPalindrome("motor"));
// Program.assertEqual(isPalindrome("motor"), false);
console.log("rotor is Palindrome: " + checkPalindrome("rotor"));
// Program.assertEqual(isPalindrome("rotor"), true);
/********* To Screen:  ************/
const container = document.getElementById("container");
// ✅ Append HTML to `div` element
container.insertAdjacentHTML('afterend', `<div style="background-color: lime">a is Palindrome: ${checkPalindrome("a")}</div>`);
// ✅ Append HTML to `div` element
container.insertAdjacentHTML('afterend', `<div style="background-color: lime">motor is Palindrome: ${checkPalindrome("motor")}</div>`);
// ✅ Append HTML to `div` element
container.insertAdjacentHTML('afterend', `<div style="background-color: lime">rotor is Palindrome: ${checkPalindrome("rotor")}</div>`);
