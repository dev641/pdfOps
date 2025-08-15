class Modal:
    def __init__(self):
        pass

    def __iter__(self):
        # Iterate over the dictionary returned by to_dict()
        for key, value in self.to_dict().items():
            yield key, value

    def __len__(self):
        return len(self.to_dict())

    @staticmethod
    def get_all_fields(self):
        keys = self.to_dict(self).keys()
        return list(keys)

    def to_dict(self):
        raise NotImplementedError("Subclasses must implement to_dict()")
