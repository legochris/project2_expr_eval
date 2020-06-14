"""Expression Evaluation Functions for Project 2
Course: CPE202
Quarter: Spring 2020
Author: Chris Linthacum
"""


import stack_array as sa


def infix_to_postfix(infix):
    """Function to convert an infix expression to postfix
    Args:
        infix(str): The infix expression
    Returns:
        str: the postfix string of the converted expression
    """

    rpn_expr = ""
    operators = {'+', '-', '*', '/', '^'}
    output_stack = sa.StackArray()
    current_token = ""
    operator_stack = sa.StackArray()

    op_precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '(': 0
    }

    association = {
        '+': 'left',
        '-': 'left',
        '*': 'left',
        '/': 'left',
        '^': 'right'
    }

    infix += ' '

    for char in infix:

        # Code to process characters to find individual tokens
        if char != ' ':
            current_token += char
        else:

            # If current token is number, push it to the output stack
            try:
                float(current_token)
                output_stack.push(current_token)
            except ValueError:

                if current_token in operators and \
                        (operator_stack.is_empty() or operator_stack.peek() == '('):
                    operator_stack.push(current_token)
                    current_token = ''
                if current_token == '(':
                    operator_stack.push(current_token)
                    current_token = ''
                if current_token == ')':
                    while operator_stack.peek() != '(':
                        output_stack.push(operator_stack.pop())
                    operator_stack.pop()
                    current_token = ''
                if current_token != '' and \
                        (op_precedence[current_token] > op_precedence[operator_stack.peek()]):
                    operator_stack.push(current_token)
                    current_token = ''
                if current_token != '' and \
                        (op_precedence[current_token] == op_precedence[operator_stack.peek()]):
                    if association[current_token] == 'left':
                        output_stack.push(operator_stack.pop())
                        operator_stack.push(current_token)
                    if association[current_token] == 'right':
                        operator_stack.push(current_token)
                if current_token != '' and \
                        (op_precedence[current_token] < op_precedence[operator_stack.peek()]):
                    while not operator_stack.is_empty() and \
                            (op_precedence[current_token] <= op_precedence[operator_stack.peek()]):
                        output_stack.push(operator_stack.pop())
                    operator_stack.push(current_token)

            current_token = ""

    while not operator_stack.is_empty():
        output_stack.push(operator_stack.pop())

    while output_stack.size() > 1:
        rpn_expr = output_stack.pop() + rpn_expr
        rpn_expr = ' ' + rpn_expr
    rpn_expr = output_stack.pop() + rpn_expr

    return rpn_expr


def prefix_to_postfix(prefix):
    """Function to convert a prefix expression to postfix
    Args:
        prefix(str): The prefix expression
    Returns:
        str: the converted postfix string
    """

    operators = {'+', '-', '*', '/', '^'}
    current_token = ""
    operand_stack = sa.StackArray()

    prefix = ' ' + prefix

    for char in prefix[::-1]:
        if char != ' ':
            current_token += char

        if char == ' ':

            try:
                float(current_token)
                current_token = current_token[::-1]
                operand_stack.push(current_token)
            except ValueError:
                if current_token in operators:
                    op1 = operand_stack.pop()
                    op2 = operand_stack.pop()
                    out_str = str(op1) + ' ' + str(op2) + ' ' + str(current_token)
                    operand_stack.push(out_str)
                else:
                    raise ValueError("Invalid token:" + current_token)

            current_token = ""

    rpn_expr = operand_stack.pop()
    return rpn_expr


def postfix_eval(postfix):
    """Function to evaluate a postfix expression
    Args:
        postfix(str): The postfix expression
    Returns:
        float: The value of the evaluated expression
    """

    current_token = ''
    operators = {'+', '-', '*', '/', '^'}
    rpn_stack = sa.StackArray()

    postfix += ' '

    for char in postfix:

        if char != ' ':
            current_token += str(char)

        if char == ' ':

            try:
                float(current_token)
                rpn_stack.push(float(current_token))
            except ValueError:
                if current_token in operators:
                    val1 = rpn_stack.pop()
                    val2 = rpn_stack.pop()
                    if current_token == '^':
                        out_val = val2 ** val1

                    elif current_token == '+':
                        out_val = val1 + val2

                    elif current_token == '-':
                        out_val = val2 - val1

                    elif current_token == '*':
                        out_val = val2 * val1

                    else:
                        try:
                            out_val = val2 / val1
                        except ZeroDivisionError:
                            raise ValueError('Dividing by Zero')

                    rpn_stack.push(out_val)
                else:
                    raise ValueError("Invalid Token")

            current_token = ''

    return rpn_stack.pop()
