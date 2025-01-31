class FileSelectorMeta(type):
    """Metaclass to prevent replacing the class-level _filePaths attribute."""

    def __setattr__(cls, name, value):
        """Prevent setting _filePaths directly."""
        if name == "_filePaths":
            raise AttributeError("Cannot modify _filePaths directly.")
        super().__setattr__(name, value)
