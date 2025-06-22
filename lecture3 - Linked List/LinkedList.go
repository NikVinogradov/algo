import struct

type Node struct {
	Value int
	Next *Node
}

type MyLinkedList struct {
	Head *Node
	Size int
}

func Constructor() MyLinkedList {
	return MyLinkedList{}
}

func (this *MyLinkedList) Get(index int) int {
	if(index < 0 || index >= this.Size) {
		return -1
	}

	current := this.Head
	for i := 1; i < index; i++ {
		current = current.Next
	}

	return current.Value
}

func (this *MyLinkedList) AddAtHead(val int) {
	this.AddAtIndex(0, val)
}

func (this *MyLinkedList) AddAtTail(val int) {
	this.AddAtIndex(this.Size, val)
}

func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index < 0 || index > this.Size {
		return
	}

	this.Size += 1

	if index == 0 {
		new_node := &Node{
			Value: val,
			Next:this.Head
		}
		this.Head = new_node
		return
	}

	current := this.Head
	for i := 1; i < index-1; i++ {
		current = current.Next
	}
	old_next := current.Next
	current.Next = &Node{
		Value: val,
		Next:old_next
	}
}

func (this *MyLinkedList) DeleteAtIndex(val int) {

	if index < 0 || index >= this.Size {
		return
	}

	this.Size -= 1

	if index == 0 {
		this.Head = this.Head.Next
		return
	}

	current := this.Head
	for i := 1; i < index-1; i++ {
		current = current.Next
	}
	current.Next = current.Next.Next
}