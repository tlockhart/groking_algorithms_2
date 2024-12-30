const items = [0, 35, 36, 41, 46, 59, 91, 100];
const item = 91;

function getMid(low, high) {
   /*** 
    * If the sum of the indexes is odd, you must round 
    *  down to the floor, since there will be a remainder 
    ***/ 
  const mean = Math.floor((low + high) / 2);
  // protect against overflow
  //   const mean = low +((low + high) / 2);
  return mean;
}

const binarySearch = (items: number[], item: number): number | null => {
  // defaults:
  let index = 0;
  let lowIndex = index;
  let highIndex = items.length - 1;

  // Loop
  while (lowIndex <= highIndex) {
    let mid = getMid(lowIndex, highIndex);

    if (items[mid] === item) {
      return mid;
    }
    else if (items[mid] > item) {
      highIndex = mid - 1;
    } else if (items[mid] < item) {
      lowIndex = mid + 1;
    }
   //  console.log(`LowIndex: ${lowIndex}; HighIndex: ${highIndex}`);
  //  alert(`LowIndex: ${lowIndex}; HighIndex: ${highIndex}; MID: ${mid}`);
  }
  return null;
};

console.log("What is the index of the item?", binarySearch(items, item));
