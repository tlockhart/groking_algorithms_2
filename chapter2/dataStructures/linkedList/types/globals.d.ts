declare global {
    interface Node {
         _value: string;
         readonly _next: Object | null;
    }
}