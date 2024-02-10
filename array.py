import ctypes


class DynamicArray:
    def __init__(self):
        """Create an empty array."""
        self._n = 0  # Count existing elements
        self._capacity = 0
        self._array = self.creat_array(self._capacity)

    def __len__(self):
        """Return the number of elements in the array."""
        return self._n

    def __getitem__(self, index):
        if not 0 <= index < self._n:
            raise IndexError("Index out of range")
        return self._array[index]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(self._capacity * 2)
        self._array[self._n] = obj
        self._n += 1  # increasing existing elements

    def _resize(self, new_capacity):
        """Create a bigger array"""
        new_array = self.creat_array(new_capacity)  # Create a bigger array
        for element in range(self._n):
            new_array[element] = self._array[element]  # Set all elements
        self._array = new_array  # Using bigger array
        self._capacity = new_capacity

    @staticmethod
    def creat_array(capacity):
        return (capacity * ctypes.py_object)()