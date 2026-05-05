import unittest
from generator import generate_task
from utils import check_answer

class TestMathTrainer(unittest.TestCase):

    def test_generate_task(self):
        q, a = generate_task()
        self.assertIsInstance(q, str)
        self.assertIsInstance(a, (int, float))

    def test_check_answer_correct(self):
        self.assertTrue(check_answer(5, 5))

    def test_check_answer_wrong(self):
        self.assertFalse(check_answer(5, 10))

if __name__ == "__main__":
    unittest.main()