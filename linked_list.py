class LinkedList:
    def __init__(self, value):
        self.head = {"value": value, "next": None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_item = {"value": value, "next": None}
        self.tail["next"] = new_item # assigning new_item's address to head's next
        self.tail = new_item # assigning new_item's address to tail itself
        self.length += 1

    def prepend(self, value):
        pre_item = {"value": value, "next": None}
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
            for idx in range(index - 1):
                curr_item = curr_item["next"]

            next_item = curr_item["next"]
            add_item = {"value": value, "next": next_item}
            curr_item["next"] = add_item

            self.length += 1

    def remove(self, index):
        if index >= self.length:
            index = self.length - 1

        rem_item = self.head
        if index > 0:
            for idx in range(index - 1):
                rem_item = rem_item["next"]
            shift_item = rem_item["next"]
            rem_item["next"] = shift_item["next"]
        else:
            self.head = self.head["next"]

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
