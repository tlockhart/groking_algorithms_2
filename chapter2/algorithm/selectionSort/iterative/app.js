"use strict";
const items = [0, 99, 81, 41, 23, 22, 19, 105];
function selectionSort(items) {
    // Comparisons
    for (let i = 0; i < items.length; i++) {
        let lowestNumberIndex = i;
        for (let j = i + 1; j <= items.length - 1; j++) {
            if (items[j] < items[lowestNumberIndex]) {
                lowestNumberIndex = j;
            }
        } // for
        // Swap
        if (lowestNumberIndex != 1) {
            let temp = items[i];
            items[i] = items[lowestNumberIndex];
            items[lowestNumberIndex] = temp;
        }
    } // for
    return items;
}
;
const sortedArray = selectionSort(items);
console.log("In Place Sorted Array:", sortedArray);
/**************** To Screen**********/
const container = document.getElementById("container");
// ✅ Append HTML to `div` element
sortedArray.forEach((item, index) => {
    container.insertAdjacentHTML('beforeend', `<div className={"number-"${index}} style="background-color: lime">${`${item}`}</div>`);
});
