#!/usr/bin/python3
""Module rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The
            width of new Rectangle.
            height (int): Height of the new Rectangle.
            x (int): The x coordinate of new Rectangle.
            y (int): The y coordinate of new Rectangle.
            id (int): Identity of the new Rectangle.
        Raises:
            TypeError: If Either_of width or height is not an int.
            ValueError: If Either_of width or height <= 0.
            TypeError: If Either_of x or y is not an int.
            ValueError: If Either_of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width MUST be an integer")
        if value <= 0:
            raise ValueError("width MUST be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height MUST be an integer")
        if value <= 0:
            raise ValueError("height MUST be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x MUST be an integer")
        if value < 0:
            raise ValueError("x MUST be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y MUST be an integer")
        if value < 0:
            raise ValueError("y MUST be >= 0")
        self.__y = value

    def area(self):
        """Return THE area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print Rectangle by using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Updates the Rectangle.

        Args:
            *args (ints):The New attribute values.
                - 1st argument defines id attribute
                - 2nd argument defines width attribute
                - 3rd argument defines height attribute
                - 4th argument defines x attribute
                - 5th argument defines y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return dictionary represents of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return print() and str() represente of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
