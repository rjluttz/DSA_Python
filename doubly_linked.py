class DoublyLinkedList:
    def __init__(self, value):
        self.head = {"value": value, "prev": None, "next": None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_item = {"value": value, "prev": None, "next": None}
        new_item["prev"] = self.tail
        self.tail["next"] = new_item
        self.tail = new_item    
        self.length += 1

    def prepend(self, value):
        pre_item = {"value": value, "prev": None, "next": None}
        self.head["prev"] = pre_item
        pre_item["next"] = self.head
        self.head = pre_item
        self.length += 1

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index == -1 or index >= self.length:
            self.append(value)
        else:
            curr_item = self.head
            for _ in range(index - 1):
                curr_item = curr_item["next"]

            next_item = curr_item["next"]
            # when adding a new item as the next item of curr item, 
            # curr item becomes prev item of the new item
            add_item = {"value": value, "prev": curr_item, "next": next_item}
            # now the next item's prev becomes the new added item
            next_item["prev"] = add_item
            # for the current item, new added item becomes the next item
            curr_item["next"] = add_item

            self.length += 1

    def remove(self, index):
        if self.length == 0:
            return

        if index >= self.length:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail["prev"]
                self.tail["next"] = None
        elif index == 0:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head["next"]
                self.head["prev"] = None
        else:
            rem_item = self.head
            for _ in range(index - 1):
                rem_item = rem_item["next"]

            # get the item to delete
            shift_item = rem_item["next"]

            # get the previous item for delete item
            prev_item = shift_item["prev"]
            # get the next item for delete item
            next_item = shift_item["next"]

            # now set the next item
            rem_item["next"] = next_item 
            # When tail is shifted to left, it is already None
            # if the next item not None
            if next_item:
                next_item["prev"] = prev_item

        self.length -= 1

    def printlist(self):
        curr_item = self.head
        print("[", end="")
        while True:
            print(curr_item["value"], end=",")
            if not curr_item["next"]:
                break
            curr_item = curr_item["next"]
        print("]")
