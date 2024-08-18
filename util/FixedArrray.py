class FixedSizeArray:
    def __init__(self, _size: int, Type: type) -> None:
        self.size: int = _size
        self.T: type = Type
        # Initialize the array with None values
        self.array = [Type() for _ in range(_size)]
    
    def mod(self, index: int, newItem) -> FileExistsError:
        """Change the value on position 'index' to 'newItem'."""
        if type(newItem) != self.T:
            raise ValueError("The type of given item is not the Type of this Array. Type of array is '{self.T}' and the given type is '" + type(newItem) + "'!")

        if index >= self.size or index < 0:
            raise IndexError("Index is out of range. The Index given is '" + index + "' and the size is '" + self.size + "'!")
        self.array[index] = newItem
    
    def get(self, index: int):
        """Get item on position 'index'."""
        if index >= self.size or index < 0:
            raise IndexError("Index is out of range. The Index given is '" + index + "' and the size is '" + self.size + "'!")

        return self.array[index]