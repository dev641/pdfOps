class FileList:
    """A list wrapper that only allows appending and removing but prevents replacement."""

    def __init__(self):
        self._data = []

    def append(self, item):
        """Only allow adding new file paths."""
        if not isinstance(item, str):
            raise TypeError("Only strings (file paths) can be added")
        self._data.append(item)

    def remove(self, item):
        """Allow removal of existing file paths."""
        self._data.remove(item)

    def __iter__(self):
        """Allow iteration over file paths."""
        return iter(self._data)

    def __getitem__(self, index):
        """Allow indexing."""
        return self._data[index]

    def __len__(self):
        """Return length of file paths."""
        return len(self._data)

    def __repr__(self):
        """String representation."""
        return repr(self._data)
