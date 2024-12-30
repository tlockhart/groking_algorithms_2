function getMid(low: number, high:number) {
   /*** 
    * If the sum of the indexes is odd, you must round 
    *  down to the floor, since there will be a remainder 
    ***/ 
  const mean = Math.floor((low + high) / 2);
  // protect against overflow
  //   const mean = low +((low + high) / 2);
  return mean;
}

const binarySearch = (items: number[], item: number, low: number, high: number): number | null | undefined => {
  // defaults:
  let lowIndex = low;
  let highIndex = high;

  // Base Condition:
  // highIndex <=0 means length of array can be 0 or 1, -1 woul make it -1 or 0
  if ( highIndex <= 0  || lowIndex >= highIndex) return null;

    let mid = getMid(lowIndex, highIndex);
    console.log("Mid:", mid, ";item:", item, items[mid], item === items[mid]);

    if (items[mid] === item) {
      console.log("Returning mid:", mid);
      return mid;
    }
    else if (items[mid] > item) {
      highIndex = mid - 1;
    } else if (items[mid] < item) {
      lowIndex = mid + 1;
    }

  console.log("lowIndex:", lowIndex, "; highIndex:", highIndex);
  // remember to return the recursive call
  return binarySearch(items,item, lowIndex, highIndex);
};

const items = [0, 35, 36, 41, 46, 59, 91, 100];
const item = 91;
const low = 0;
const high = items.length -1;
console.log("What is the index of the item?", binarySearch(items, item, low, high));
