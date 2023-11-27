class SingletonMeta(type):
    """
    In Python, a Singleton can be implemented in different ways. Possible methods
    include using a base class, a decorator, or a metaclass. We will use
    a metaclass, as it is most suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        This implementation does not consider the possible change of the passed
        arguments in `__init__`.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonBase(metaclass=SingletonMeta):
    pass
