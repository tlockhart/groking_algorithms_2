class Node {

    private _value: string;
    private _next: Object | null;

    constructor(value: string) {
        this._value = value;
        this._next = null;
    }
    get value(): string {
        return this._value;
    }
    get next(): Object | null {
        return this._next;
    }
    set next(value) {
        this._next = value;
    }
}

export default Node;