import LinkedList from "./LinkedList.js";
import Node from "./Node.js";
const appendNode1 = new Node("Have ");
const appendNode2 = new Node("a ");
const appendNode3 = new Node("nice ");
const appendNode4 = new Node("day! ");
const prependNode1 = new Node("Thanks ");
const prependNode1B = new Node("Thanks ");
const prependNode2 = new Node("for ");
const prependNode3 = new Node("stopping ");
const prependNode4 = new Node("by! ");
const deleteNode1 = new Node("Thanks ");
const findNode1 = new Node("day! ");
const findNode2NoMatch = new Node("anyone match?");
const insertAfterNode1 = new Node("End Message!");
const linkedList = new LinkedList("Tony");
linkedList.append(appendNode1);
linkedList.append(appendNode2);
linkedList.append(appendNode3);
linkedList.append(appendNode4);
//This will create an infinite loop, 
// Because this will create circular liked list
// You must use a completely new node
// linkedList.append(prependNode1)
linkedList.append(prependNode1B);
// Prepend nodes must be in reverse order
linkedList.prepend(prependNode4);
linkedList.prepend(prependNode3);
linkedList.prepend(prependNode2);
linkedList.prepend(prependNode1);
// Delete nodes with matching values
linkedList.delete(deleteNode1);
// Find First Occurence
console.log("FOUND FIRST OCCURENCE:", linkedList.findFirst(findNode1));
console.log("OCCURENCE NOT FOUND:", linkedList.findFirst(findNode2NoMatch));
// InsertAfter
linkedList.insertMiddle(insertAfterNode1, appendNode4);
const greeting = `Hello `;
/********* To Console: ************/
console.log(`${greeting} ${linkedList.name}!`, linkedList.toConsole());
/********* To Screen:  ************/
const container = document.getElementById("container");
// ✅ Append text to `div` element
container.insertAdjacentText("beforeend", greeting);
// ✅ Append HTML to `div` element
container.insertAdjacentHTML('beforeend', `<span style="background-color: lime">${linkedList.name}</span>`);
// ✅ Append HTML to `div` element
container.insertAdjacentHTML('afterend', `<span style="background-color: lime">${linkedList.toScreen().join("")}</span>`);
