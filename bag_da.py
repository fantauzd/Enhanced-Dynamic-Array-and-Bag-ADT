# Name: Dominic Fantauzzo
# OSU Email: fantauzd@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2 - Dynamic Array Implementation
# Due Date: 2/6/2024
# Description: Implementation of a bag class, using a static array and dynamic array module.
#              The bag class is an ADT that behaves like a bag in real life, with limited functionality.


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds a new element to the bag in O(1) amortized time complexity.

        :param value: value to be added to bag

        :return: None
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes any one element from the bag that matches the provided value
        object. It returns True if some object was actually removed from the bag.
        Otherwise, it returns False.

        :param value: value to be removed from bag

        :return: Boolean True if removed, otherwise False
        """
        # Iterate over the list and look for the value, if found remove it and return True
        for num in range(self._da.length()):
            if self._da.get_at_index(num) == value:
                self._da.remove_at_index(num)
                return True
        # If the object was not found, return False
        return False

    def count(self, value: object) -> int:
        """
        returns the number of elements in the bag that match the provided value object.

        :param value: the object we are counting in the bag

        :return: an integer representing the count
        """
        # iterate through the dynamic array and increment count when the value is found
        count = 0
        for num in range(self._da.length()):
            if self._da.get_at_index(num) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Clears the contents of the bag.

        :return: None
        """
        # Creates a new empty dynamic array to overwrite attribute
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        Compares the contents of a bag with the contents of a second bag provided as
        a parameter. The method returns True if the bags are equal (contain the same number of
        elements, and also contain the same elements without regard to the order of elements).
        Otherwise, it returns False.

        :param second_bag: a bag object

        :return: a boolean value
        """
        # Ensures the bags have the same number of elements
        if second_bag._da.length() == self._da.length():
            # iterates over each value of the first bag and ensures that the second bag
            # has the same number of each element
            for num in range(self._da.length()):
                if self.count(self._da.get_at_index(num)) != second_bag.count(self._da.get_at_index(num)):
                    # If the second bag has a different number of any element, they are not equal
                    return False
        # If the bags don't have the same number of elements, they are not equal
        else:
            return False
        # If the bags have all the same elements, they are equal
        return True

    def __iter__(self):
        """
        Enables the Bag to iterate across itself.
        """
        self._index = 0

        return self

    def __next__(self):
        """
        Returns the next item in the Bag, based on the current location of the iterator.
        """
        try:
            value = self._da.get_at_index(self._index)
        except DynamicArrayException:
            raise StopIteration

        self._index = self._index + 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
