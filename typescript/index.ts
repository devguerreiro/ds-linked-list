import assert from "assert";

namespace NSLinkedList {
    export class Node {
        value: number;
        next: Node | null = null;

        constructor(value: number) {
            this.value = value;
        }
    }

    export class LinkedList {
        private initial: Node | null = null;
        private size: number = 0;

        private getNode(index: number) {
            const _index = index < 0 ? this.size + index : index;
            let node = this.initial;
            for (let i = 0; i < _index; i++) {
                if (node !== null) {
                    node = node.next;
                } else {
                    break;
                }
            }
            if (node !== null && !(_index < 0)) {
                return node;
            }
            throw new RangeError();
        }

        add(value: number): void {
            const newNode = new Node(value);
            if (this.size === 0) {
                this.initial = newNode;
            } else {
                let lastNode = this.initial as Node;
                while (lastNode.next !== null) {
                    lastNode = lastNode.next;
                }
                lastNode.next = newNode;
            }
            this.size++;
        }

        get(index: number) {
            const node = this.getNode(index);
            return node.value;
        }

        set(index: number, value: number) {
            const node = this.getNode(index);
            node.value = value;
        }

        indexOf(value: number) {
            let node = this.initial;
            let index = 0;
            while (node !== null) {
                if (node.value === value) {
                    return index;
                }
                node = node.next;
                index++;
            }
            return -1;
        }

        insert(index: number, value: number) {
            const newNode = new Node(value);
            if (index === 0) {
                newNode.next = this.initial;
                this.initial = newNode;
            } else {
                const previousNode = this.getNode(index - 1);
                newNode.next = previousNode.next;
                previousNode.next = newNode;
            }
            this.size++;
        }

        remove(value: number) {
            if (this.size === 0) {
                throw new Error();
            }
            if (this.initial !== null) {
                if (this.initial.value === value) {
                    let aux = this.initial.next;
                    this.initial.next = null;
                    this.initial = aux;
                    this.size--;
                    return true;
                } else {
                    let previousNode = this.initial;
                    let currentNode = previousNode.next;
                    while (currentNode !== null) {
                        if (currentNode.value === value) {
                            previousNode.next = currentNode.next;
                            currentNode.next = null;
                            this.size--;
                            return true;
                        }
                        previousNode = currentNode;
                        currentNode = currentNode.next;
                    }
                    return false;
                }
            }
        }

        get length(): number {
            return this.size;
        }
    }
}

// TODO: convert into unit testing

const linkedList = new NSLinkedList.LinkedList();

const BIG_INDEX = 2 ** 100;

linkedList.add(10);
linkedList.add(11);
linkedList.add(12);

// check length
assert.equal(linkedList.length, 3);

// check get by index
assert.equal(linkedList.get(0), 10);
assert.equal(linkedList.get(1), 11);
assert.equal(linkedList.get(2), 12);

// check inverted get by index
assert.equal(linkedList.get(-1), 12);
assert.equal(linkedList.get(-2), 11);
assert.equal(linkedList.get(-3), 10);

// check index of
assert.equal(linkedList.indexOf(10), 0);
assert.equal(linkedList.indexOf(11), 1);
assert.equal(linkedList.indexOf(12), 2);

// check index of inexistent
assert.equal(linkedList.indexOf(BIG_INDEX), -1);

// check get by index of an index bigger than length
assert.throws(() => linkedList.get(BIG_INDEX), RangeError);

// check get by index of an index smaller than negative length
assert.throws(() => linkedList.get(-BIG_INDEX), RangeError);

// check change index value
linkedList.set(0, 20);
linkedList.set(1, 21);
linkedList.set(2, 22);

assert.equal(linkedList.get(0), 20);
assert.equal(linkedList.get(1), 21);
assert.equal(linkedList.get(2), 22);

// check change inverted index value
linkedList.set(-1, 32);
linkedList.set(-2, 31);
linkedList.set(-3, 30);

assert.equal(linkedList.get(2), 32);
assert.equal(linkedList.get(1), 31);
assert.equal(linkedList.get(0), 30);

// check change index value of an index bigger than length
assert.throws(() => linkedList.set(BIG_INDEX, 1), RangeError);

// check change index value of an index smaller than negative length
assert.throws(() => linkedList.set(-BIG_INDEX, 1), RangeError);

// check insert before initial
let aux = linkedList.get(0);
linkedList.insert(0, 150);
assert.equal(linkedList.get(0), 150);
assert.equal(linkedList.get(1), aux);
assert.equal(linkedList.length, 4);

// check insert in the middle
aux = linkedList.get(2);
linkedList.insert(2, 232);
assert.equal(linkedList.get(2), 232);
assert.equal(linkedList.get(3), aux);
assert.equal(linkedList.length, 5);

// check insert after last
aux = linkedList.get(linkedList.length - 1);
linkedList.insert(linkedList.length, 345);
assert.equal(linkedList.get(linkedList.length - 1), 345);
assert.equal(linkedList.get(linkedList.length - 2), aux);
assert.equal(linkedList.length, 6);

const linkedList2 = new NSLinkedList.LinkedList();

linkedList2.add(10);
linkedList2.add(20);
linkedList2.add(30);
linkedList2.add(40);
linkedList2.add(50);

// remove the first item
aux = linkedList2.get(1);
assert.equal(linkedList2.remove(10), true);
assert.equal(linkedList2.get(0), aux);
assert.equal(linkedList2.length, 4);

// remove the middle item
aux = linkedList2.get(2);
assert.equal(linkedList2.remove(30), true);
assert.equal(linkedList2.get(1), aux);
assert.equal(linkedList2.length, 3);

// remove the last item
aux = linkedList2.get(linkedList2.length - 2);
assert.equal(linkedList2.remove(50), true);
assert.equal(linkedList2.get(linkedList2.length - 1), aux);
assert.equal(linkedList2.length, 2);

// remove inexistent item
assert.equal(linkedList2.remove(50), false);
