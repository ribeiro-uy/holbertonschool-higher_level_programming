#!/usr/bin/python3
"""module of tests for square"""


import unittest
from models.square import Square


class Test_Square(unittest.TestCase):
    """Tests for square"""
    def no_doc(item):
        """A decorator to add the no-doc docstring
        objects that don't need any other documentation"""
        t = "class" if inspect.isclass(item) else "function"
        item.__doc__ = "This {} intentionally has no documentation".format(t)
        
    def test_area(self):
        """Test area of rectangle"""
        test_inst = Square(2, 2)
        self.assertEqual(test_inst.area(), 4)
        
    def test_square(self):
        """Test Square without parameters"""
        square = Square(1, 2, 3)
        square2 = Square(2)
        square3 = Square(2, 3)
        square4 = Square(2, 3, 4, 5)
        
    def test_wrong_parameter(self):
        """Test for non int arguments in square"""
        with self.assertRaises(TypeError):
            square = Square([1, 2, 3, 4], "5")
            square = Square(1, None)
            square = Square()
            square = Square(None)
            square = Square([1, 2, 3])
            square = Square("str", 2)
            square = Square({"id": 1, "od": 2})
            
    def test_size(self):
        """Test for size values"""
        square = Square(1, 2, 3)
        with self.assertRaises(ValueError):
            square.size = -1
            square.size = 1e10000000
            square.size = 0
            
    def test_none_size(self):
        """Test for non int values in size"""
        square = Square(1, 2, 3)
        with self.assertRaises(TypeError):
            square.size = None
            square.size = True
            square.size = "Atenea"
            square.size = [1, 2, 3]
            square.size = {"id": 1, "od": 2}
            square.size = 2.34
            square.size = (1, 2, 3)
            square.size = float(NaN)
            
    def test_negative_square(self):
        """Test for size negative value"""
        with self.assertRaises(ValueError):
            square = Square(-2)
            
    def test_0_square(self):
        """Test for 0 value in size"""
        with self.assertRaises(ValueError):
            square = Square(0, 2, 3)
            
    def test_x_value(self):
        """Test negative value in x"""
        square = Square(1)
        with self.assertRaises(ValueError):
            square.x = -2
            
    def test_y_value(self):
        """Test negative value in y"""
        square = Square(1)
        with self.assertRaises(ValueError):
            square.y = -5
            
    def test_x_type(self):
        """Test non int values in x"""
        square = Square(2)
        with self.assertRaises(TypeError):
            square.x = [1, 2, 3]
            square.x = {1, 2}
            square.x = "2"
            square.x = 3.14
            square.x = None
            square.x = True
            square.x = {"id": 1, "od": 2}
            square.x = (1, 2, 3)
            square.x = float(NaN)
            
    def test_y_type(self):
        """Test non int values in y"""
        square = Square(2)
        with self.assertRaises(TypeError):
            square.y = [1, 2, 3]
            square.y = {1, 2}
            square.y = "2"
            square.y = 3.14
            square.y = None
            square.y = True
            square.y = {"id": 1, "od": 2}
            square.y = (1, 2, 3)
            square.y = float(NaN)
            
    def test_more_parameters(self):
        """Test more than 4 arguments"""
        with self.assertRaises(TypeError):
            square = Square(2, 4, 5, 7, 8, 9)
            
    def test_str(self):
        """Test str for square"""
        square = Square(5, 0, 0, 4)
        self.assertEqual(square.__str__(), '[Square] (4) 0/0 - 5')
        
    def test_update(self):
        """Test update with correct values"""
        square = Square(5)
        square.update()
        square.update(1, 2, y=3)
        square.update(1, 12, id=4)
        square.update(size=2, y=5)
        
    def test_update_wrong(self):
        """Test update with value errors"""
        square = Square(5)
        with self.assertRaises(ValueError):
            square.update(0)
            square.update(-1, 2, 3)
            square.update(size=-1, x=2, y=3)
            square.update(size=1e1000000)
            
    def test_update_type(self):
        """Test update with Type error"""
        square = Square(4)
        with self.assertRaises(TypeError):
            square.update("ate", 2, 3)
            square.update(1, 2, 3, 4, 5, 7)
            square.update([1, 2, 3])
            square.update({"id": 1, "od": 2})
            square.update(2.3, 2, 3)
            square.update((1, 2, 3))
            square.update(None, 3, 4)
            square.update(True, 3, 4)
            square.update(float(NaN))
            square.update(size=[1, 2, 3])
            square.update(2, x="ate", y=3)
            
    def test_display(self):
        """test the display function"""
        import io
        import contextlib
        
        inst = Square(3, 0, 0, 1)
        with io.StringIO() as fd:
            with contextlib.redirect_stdout(fd):
                inst.display()
                rec = fd.getvalue()
        self.assertEqual(rec, '###\n###\n###\n')
                
if __name__ == '__main__':
    unittest.main()
