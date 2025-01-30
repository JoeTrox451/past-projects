# File: LinkedList.py
# custom data structure of a linked list
# adapted from data structures class, originally in java

class Link:
    def __init__(self, key = 0, text = ""):
        self.int_key = key
        self.str_text = text
        self.next = None

    def showContents(self):
        print("Key:", self.int_key, "| Text:", self.str_text)


class LinkedList:
    def __init__(self):
        self.firstLink = None

    def isEmpty(self):
        return self.firstLink == None

    def create(self, key, text):
        success = False
        if self.isEmpty():
            self.firstLink = Link(key, text)
            self.firstLink.next = None
            success = True
        else:
            print("Head link already exists")
        return success

    def append(self, key, text):
        success = False
        if self.isEmpty():
            success = self.create(key, text)
        else:
            currentLink = self.firstLink
            while currentLink.next != None:
                currentLink = currentLink.next
            if currentLink.next == None:
                newLink = Link(key, text)
                newLink.next = None
                currentLink.next = newLink
                success = True
        return success

    def delete(self, key):
        success = False
        if self.isEmpty(): return success
        currentLink = self.firstLink
        prevLink = self.firstLink
        if currentLink.int_key == key: return success
        while currentLink.int_key != key:
            prevLink = currentLink
            currentLink = currentLink.next
            if currentLink == None: return success
        print("Key found, non head node, deleting")
        prevLink.next = currentLink.next
        success = True
        return success

    def deleteHead(self):
        success = False
        while success == False:
            try:
                if int(input("Head node removal, are you sure? Enter 1 to confirm yes: ")) == 1:
                    self.firstLink = None
                    success = True
                    return success
                else:
                    return success
            except:
                print("Invalid entry")

    def find(self, key):
        if self.isEmpty(): return None
        currentLink = self.firstLink
        while currentLink.int_key != key and currentLink != None:
            currentLink = currentLink.next
        return currentLink

    def insert(self, find_key, new_key, new_text):
        currentLink = self.find(find_key)
        newLink = Link(new_key, new_text)
        newLink.next = currentLink.next
        currentLink.next = newLink
        return True

    def modify(self, find_key, new_key, new_text):
        currentLink = self.find(find_key)
        currentLink.int_key = new_key
        currentLink.str_text = new_text
        return True

    def getLength(self):
        if self.isEmpty(): return 0
        currentLink = self.firstLink
        i = 1
        while currentLink.next != None:
            i += 1
            currentLink = currentLink.next
        return i

    def showContents(self):
        if self.isEmpty():
            print("The list is empty, insert one link minimum to list contents")
            return
        currentLink = self.firstLink
        print("---")
        currentLink.showContents()
        while currentLink.next != None:
            print("|\nV")
            currentLink = currentLink.next
            currentLink.showContents()
        print("---")


def test():
    LLT = LinkedList()
    LLT.create(1,"Joe")
    LLT.append(2,"Dan")
    LLT.append(4,"Noah")
    LLT.showContents()
    input()
    LLT.insert(2,3,"Rob")
    LLT.modify(2,2,"Brennan")
    LLT.showContents()
    input()
    LLT.delete(4)
    LLT.showContents()
    input()
    LLT.append(4,"Dan")
    LLT.append(5,"Noah")
    LLT.showContents()
    input()


if __name__ == "__main__": test()
