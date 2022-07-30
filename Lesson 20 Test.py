import unittest
import Lesson_20

class MathTestCase(unittest.TestCase):

    def test_Mathemat(self):
        squarelist = [7, 11, 5, 4]
        square = Lesson_20.Mathematician.square_nums(self, squarelist)
        self.assertEqual(square, [49, 121, 25, 16])

    def test_remove_positive(self):
        removelist = [-11, -8, 13, -90]
        remove = Lesson_20.Mathematician.remove_positives(self, removelist)
        self.assertEqual(remove, [-11, -8, -90])

    def test_filter_lips(self):
        leaplist = [2001, 1884,1995, 2003, 2020]
        filt = Lesson_20.Mathematician.filter_leaps(self, leaplist)
        self.assertEqual(filt, [1884, 2020])

    def test_validation_email(self):
        validemail = 'uklk@mail.com'
        res = Lesson_20.Email.name1(self, validemail)
        self.assertEqual(res, None)


    def test_add_fish_to_aquarium_success(self):
        actual = Lesson_20.add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        self.assertEqual(actual, expected)


unittest.main()


