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


class FileSelectorMeta(type):
    """Metaclass to prevent replacing the class-level _filePaths attribute."""

    def __setattr__(cls, name, value):
        """Prevent setting _filePaths directly."""
        if name == "_filePaths":
            raise AttributeError("Cannot modify _filePaths directly.")
        super().__setattr__(name, value)


class FileSelector(metaclass=FileSelectorMeta):
    _filePaths = FileList()  # 🔥 Single source of truth!

    @classmethod
    def filePaths(cls):
        """Return the filePaths list (read-only access)."""
        return cls._filePaths  # ✅ Cannot be replaced, only modified


# ========================
# ✅ Usage Example:
# ========================

fs1 = FileSelector()
fs2 = FileSelector()

# ✅ Append a file
fs1.filePaths().append("file1.pdf")
fs2.filePaths().append("file2.pdf")

# ✅ Remove a file
fs1.filePaths().remove("file1.pdf")

# ❌ Attempt to replace filePaths (will fail)
try:
    FileSelector._filePaths = ["new_list.pdf"]
except AttributeError as e:
    print("🚨 Error:", e)

# ✅ Check final result
print(FileSelector.filePaths())  # ['file2.pdf']
