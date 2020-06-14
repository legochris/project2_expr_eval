"""Test Functions for Lab 3 Functions and Classes
Course: CPE202
Quarter: Spring 2020
Author: Chris Linthacum
"""

import unittest as ut
import stack_array as sa
import exp_eval as ee


class StackArrayTests(ut.TestCase):
    """Validation tests for the StackArray class and methods"""

    def test_push(self):
        """Tests the push function"""

        test_stack = sa.StackArray()
        test_stack.push(1)
        test_stack.push(2)
        test_stack.push(3)
        self.assertEqual(1, test_stack.arr[0])
        self.assertEqual(3, test_stack.arr[2])

    def test_pop(self):
        """Tests the pop function"""

        test_stack = sa.StackArray()
        test_stack.push(1)
        test_stack.push(2)
        test_stack.push(3)

        empty_stack = sa.StackArray()

        pop_val = test_stack.pop()
        self.assertEqual(3, pop_val)
        self.assertEqual(2, test_stack.num_items)

        self.assertRaises(IndexError, empty_stack.pop)

    def test_repr(self):
        """Tests the repr function"""

        test_stack = sa.StackArray()
        test_stack.push(1)
        test_stack.push(2)
        test_stack.push(3)

        expected_str = '1 2 3'
        test_str = repr(test_stack)
        self.assertEqual(expected_str, test_str)

    def test_eq(self):
        """Tests the eq function"""

        stack_one = sa.StackArray()
        stack_one.push(1)
        stack_one.push(2)
        stack_one.push(3)

        stack_two = sa.StackArray()
        stack_two.push(1)
        stack_two.push(2)

        self.assertFalse(stack_one == stack_two)
        stack_two.push(3)

        stack_three = sa.StackArray()
        stack_three.push(3)
        stack_three.push(2)
        stack_three.push(1)

        not_stack = 1

        self.assertTrue(stack_one == stack_two)
        self.assertFalse(stack_one == not_stack)
        self.assertFalse(stack_one == stack_three)

    def test_enlarge(self):
        """Tests the enlarge function"""

        test_stack = sa.StackArray()
        test_stack.push(0)
        self.assertEqual(test_stack.capacity, 2)
        test_stack.push(1)
        self.assertEqual(test_stack.capacity, 4)
        test_stack.push(2)
        self.assertEqual(test_stack.capacity, 4)
        test_stack.push(3)
        self.assertEqual(test_stack.capacity, 8)

    def test_shrink(self):
        """Tests the shrink function"""

        test_stack = sa.StackArray()
        test_stack.push(1)
        test_stack.push(2)
        test_stack.push(3)
        test_stack.push(4)
        test_stack.push(1)
        test_stack.push(2)
        test_stack.pop()
        test_stack.pop()
        test_stack.pop()
        test_stack.pop()
        self.assertEqual(4, test_stack.capacity)

    def test_peek(self):
        """Tests the peek function"""

        test_stack = sa.StackArray()
        test_stack.push(1)
        test_stack.push(2)
        test_stack.push(3)
        test_stack.push(4)

        empty_stack = sa.StackArray()

        self.assertEqual(4, test_stack.peek())
        self.assertEqual(4, test_stack.peek())

        self.assertRaises(IndexError, empty_stack.peek)

    def test_is_empty(self):
        """Tests the is_empty function"""

        test_stack = sa.StackArray()
        self.assertTrue(test_stack.is_empty())
        test_stack.push(1)
        test_stack.push(2)
        self.assertFalse(test_stack.is_empty())
        test_stack.pop()
        test_stack.pop()
        self.assertTrue(test_stack.is_empty())

    def test_size(self):
        """Tests the size function"""

        test_stack = sa.StackArray()
        test_stack.push(1)
        test_stack.push(2)
        self.assertEqual(2, test_stack.size())
        test_stack.peek()
        self.assertEqual(2, test_stack.size())
        test_stack.pop()
        self.assertEqual(1, test_stack.size())


class InfixToPostfixTests(ut.TestCase):
    """Test Cases for evaluating the infix to postfix conversion function"""

    def test_expression_given(self):
        """Test a valid infix expression to a known postfix output"""
        test_expr = '3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'
        expected_expr = '3 4 2 * 1 5 - 2 3 ^ ^ / +'
        output_expr = ee.infix_to_postfix(test_expr)

        self.assertEqual(expected_expr, output_expr)

    def test_expr_2(self):
        """Test a valid infix expression to a known postfix output - example 2"""
        test_expr = '6 + 4 + 2 ( 7 / 3 * 1 ) + ( 4 ^ 7 - 2 ) * 8'
        expected_expr = '6 4 + 2 7 3 / 1 * + 4 7 ^ 2 - 8 * +'
        output_expr = ee.infix_to_postfix(test_expr)

        self.assertEqual(expected_expr, output_expr)

    def test_expr_3(self):
        """Test a valid infix expression to a known postfix output - example 3"""
        test_expr = '7 * 6 - 2 ( 6 / 2 ) + ( 4 - 1 )'
        expected_expr = '7 6 * 2 6 2 / - 4 1 - +'
        output_expr = ee.infix_to_postfix(test_expr)

        self.assertEqual(expected_expr, output_expr)

    def test_expr_4(self):
        """Test a valid infix expression to a known postfix output - example 4"""
        test_expr = '2 * 20 / 2 + ( 3 + 4 ) * 3 ^ 2 - 6 + 15'
        expected_expr = '2 20 * 2 / 3 4 + 3 2 ^ * + 6 - 15 +'
        output_expr = ee.infix_to_postfix(test_expr)

        self.assertEqual(expected_expr, output_expr)

    def test_expr_5(self):
        """Test a valid infix expression to a known postfix output - example 5"""
        test_expr = '6 + 9 + 4 ^ 2'
        expected_expr = '6 9 + 4 2 ^ +'
        output_expr = ee.infix_to_postfix(test_expr)

        self.assertEqual(expected_expr, output_expr)

    def test_expr_6(self):
        """Test a valid infix expression to a known postfix output - example 6"""
        test_expr = '( 5.9 - 5.3 ) * 7.2 + 1.4 ^ 2'
        expected_expr = '5.9 5.3 - 7.2 * 1.4 2 ^ +'
        output_expr = ee.infix_to_postfix(test_expr)

        self.assertEqual(expected_expr, output_expr)


class PrefixToPostfixTests(ut.TestCase):
    """Test cases for evaluating the prefix to postfix conversion function"""

    def test_expression_given(self):
        """Test a valid prefix expression to a known postfix output - given example"""
        test_expr = '* - 3 / 2 1 - / 4 5 6'
        expected_expr = '3 2 1 / - 4 5 / 6 - *'
        output_expr = ee.prefix_to_postfix(test_expr)

        self.assertEqual(expected_expr, output_expr)

    def test_expression_2(self):
        """Test a valid prefix expression to a known postfix output - example 2"""
        test_expr = '* / + 6 4 - 7 5 ^ 3 2'
        expected_expr = '6 4 + 7 5 - / 3 2 ^ *'
        output_expr = ee.prefix_to_postfix(test_expr)

        self.assertEqual(expected_expr, output_expr)

    def test_expression_3(self):
        """Test a valid prefix expression to a known postfix output - example 3"""
        test_expr = '^ + - ^ 3 2 * 2 3 / 8 2 2'
        expected_expr = '3 2 ^ 2 3 * - 8 2 / + 2 ^'
        output_expr = ee.prefix_to_postfix(test_expr)

        self.assertEqual(expected_expr, output_expr)

    def test_expression_4(self):
        """Test a valid prefix expression to a known postfix output - example 4"""
        test_expr = '+ - * 7 3 / 6 2 ^ 4 2'
        expected_expr = '7 3 * 6 2 / - 4 2 ^ +'
        output_expr = ee.prefix_to_postfix(test_expr)

        self.assertEqual(expected_expr, output_expr)

    def test_expression_5(self):
        """Test a valid prefix expression to a known postfix output - example 5"""
        test_expr = '+ 6 + 9 ^ 4 2'
        expected_expr = '6 9 4 2 ^ + +'
        output_expr = ee.prefix_to_postfix(test_expr)

        self.assertEqual(expected_expr, output_expr)

    def test_expression_6(self):
        """Test a valid prefix expression to a known postfix output - example 6"""
        test_expr = '+ * - 5.9 5.3 7.2 ^ 1.4 2'
        expected_expr = '5.9 5.3 - 7.2 * 1.4 2 ^ +'
        output_expr = ee.prefix_to_postfix(test_expr)

        self.assertEqual(expected_expr, output_expr)

    def test_bad_operator(self):
        """Test for correct exception handling when invalid operator included in the expression"""
        test_expr = '** 7 3'

        self.assertRaises(ValueError, ee.prefix_to_postfix, test_expr)


class PostfixEvalTests(ut.TestCase):
    """Test cases for the Postfix Expression Evaluation Function"""

    def test_expression(self):
        """Tests the evaluation of a correctly formatted postfix expression to a known value"""
        test_expr = '5 1 2 + 4 ^ + 3 -'
        expected_val = 83
        output_val = ee.postfix_eval(test_expr)

        self.assertEqual(expected_val, output_val)

    def test_expr_2(self):
        """Tests the evaluation of a correctly formatted postfix expression to a known value
           - example 2"""
        test_expr = '6 4 + 2 7 3 / 1 * + 4 7 ^ 2 - 8 * +'
        expected_val = 131060.333
        output_val = ee.postfix_eval(test_expr)

        self.assertAlmostEqual(expected_val, output_val, 2)

    def test_expr_3(self):
        """Tests the evaluation of a correctly formatted postfix expression to a known value
           - example 3"""
        test_expr = '7 6 * 2 6 2 / - 4 1 - +'
        expected_val = 2
        output_val = ee.postfix_eval(test_expr)

        self.assertAlmostEqual(expected_val, output_val, 6)

    def test_expr_4(self):
        """Tests the evaluation of a correctly formatted postfix expression to a known value
           - example 4"""
        test_expr = '2 20 * 2 / 3 4 + 3 2 ^ * + 6 - 15 +'
        expected_val = 92
        output_val = ee.postfix_eval(test_expr)

        self.assertAlmostEqual(expected_val, output_val, 2)

    def test_expr_5(self):
        """Tests the evaluation of a correctly formatted postfix expression to a known value
           - example 5"""
        test_expr = '6 9 + 4 2 ^ +'
        expected_val = 31
        output_val = ee.postfix_eval(test_expr)

        self.assertAlmostEqual(expected_val, output_val, 5)

    def test_expr_6(self):
        """Tests the evaluation of a correctly formatted postfix expression to a known value
           - example 6"""
        test_expr = '5.9 5.3 - 7.2 * 1.4 2 ^ +'
        expected_val = 6.28
        output_val = ee.postfix_eval(test_expr)

        self.assertAlmostEqual(expected_val, output_val, 5)

    def test_expr_zero_div(self):
        """Tests the correct error raising when attempting to divide by zero"""
        test_expr = '6 0 /'

        self.assertRaises(ValueError, ee.postfix_eval, test_expr)

    def test_bad_operator(self):
        """Tests the correct error handling when a bad operator is included in the expression"""
        test_expr = '6 4 **'

        self.assertRaises(ValueError, ee.postfix_eval, test_expr)


if __name__ == '__main__':
    ut.main()
