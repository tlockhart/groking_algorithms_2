var items = [0, 35, 36, 41, 46, 59, 91, 100];
var item = 91;
function getMid(low, high) {
    var mean = Math.floor((low + high) / 2);
    // protect against overflow
    //   const mean = low +((low + high) / 2);
    return mean;
}
var binarySearch = function (items, item) {
    // defaults:
    var index = 0;
    var lowIndex = index;
    var highIndex = items.length - 1;
    // Loop
    while (lowIndex <= highIndex) {
        var mid = getMid(lowIndex, highIndex);
        if (items[mid] === item) {
            return mid;
        }
        else if (items[mid] > item) {
            highIndex = mid - 1;
        }
        else if (items[mid] < item) {
            lowIndex = mid + 1;
        }
        //  console.log(`LowIndex: ${lowIndex}; HighIndex: ${highIndex}`);
        alert("LowIndex: ".concat(lowIndex, "; HighIndex: ").concat(highIndex, "; MID: ").concat(mid));
    }
    return null;
};
console.log("What is the index of the item?", binarySearch(items, item));
