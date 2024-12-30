class Node {
    constructor(value) {
        this._value = value;
        this._next = null;
    }
    get value() {
        return this._value;
    }
    get next() {
        return this._next;
    }
    set next(value) {
        this._next = value;
    }
}
export default Node;
