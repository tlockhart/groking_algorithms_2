class LinkedList {
    constructor(name) {
        this.name = name;
        // First Element
        this.head = null;
        // Last Element
        this.tail = null;
    }
    append(newNode) {
        // EdgeCase: Only update the old tail, if one exists, could be empty list.
        if (this.tail) {
            // previous tail next pointer set to newNode
            this.tail.next = newNode;
        }
        // Tail is now updated to the newNode
        this.tail = newNode;
        // Edge Case: If empty list, the head must be set after adding a new one
        if (!this.head) {
            this.head = newNode;
        }
    }
    //EdgeCase Empty list, requires setting
    // head and tail nodes
    prepend(newNode) {
        if (this.head) {
            newNode.next = this.head;
            this.head = newNode;
        }
        else {
            // set the head to the newNode
            this.head = newNode;
        }
        if (!this.tail) {
            this.tail = newNode;
        }
    }
    delete(node) {
        console.log("DELETE NODE:", node);
        // EdgeCase: List is empty
        if (!this.head) {
            return;
        }
        // EdgeCase: First node's value matches delete value
        while (this.head && this.head.value === node.value) {
            this.head = this.head.next;
        }
        let curNode = this.head;
        while (curNode.next) {
            // check if current and next value has value to delete
            if (curNode.next.value === node.value) {
                curNode.next = curNode.next.next;
            }
            else {
                // no matching value, increment node pointer
                curNode = curNode.next;
            }
        } // while
        // Edge case: If tail node is matching node, then update tail node
        if (this.tail.value === node.value) {
            this.tail = curNode;
        }
    } // delete
    findFirst(node) {
        console.log("LOOKING FOR FIRST OCCURENCE OF NODE:", node);
        if (!this.head) {
            return;
        }
        let curNode = this.head;
        while (curNode) {
            if (curNode.value === node.value) {
                return curNode;
            }
            curNode = curNode.next;
        } // while
        // Didn't find a match
        return null;
    }
    // Find the node with the afterValue
    insertMiddle(insertNode, beforeInsertNode) {
        const selectedNode = this.findFirst(beforeInsertNode);
        if (selectedNode) {
            // Start inserting next should point to the node after selectedNode
            insertNode.next = selectedNode.next;
            // reset selectedNode, so it points to the insertNode
            selectedNode.next = insertNode;
        }
    }
    toConsole() {
        const elements = [];
        let curNode = this.head;
        while (curNode) {
            elements.push(curNode);
            curNode = curNode.next;
        } //while
        return elements;
    } //toArray
    toScreen() {
        const elements = [];
        let curNode = this.head;
        while (curNode) {
            elements.push(curNode.value);
            curNode = curNode.next;
        } //while
        return elements;
    } //toArray
}
export default LinkedList;
