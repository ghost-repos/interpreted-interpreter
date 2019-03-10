import pytest, random
from _test_utils import eval_and_print, assert_stripped_output_is

class TestDefine(object):
    @pytest.mark.parametrize("v1, v2", [(x, y) for x in range(10) for y in range(5)])
    def test_binary_addition(self, v1, v2, capsys):
        eval_and_print("(b+ %s %s)" % (v1, v2))
        assert_stripped_output_is(capsys, str(v1 + v2))

    @pytest.mark.parametrize("v", [(x) for x in range(10)])
    def test_define_variables(self, v, capsys):
        eval_and_print("(define x %s)" % v)
        capsys.readouterr()
        eval_and_print("x")
        assert_stripped_output_is(capsys, str(v))

    @pytest.mark.parametrize("v1, v2", [(x, y) for x in range(5) for y in range(5)])
    def test_define_functions(self, v1, v2, capsys):
        eval_and_print("(define (a x) (b+ %s x))" % v1)
        capsys.readouterr()
        eval_and_print("(a %s)" % v2)
        assert_stripped_output_is(capsys, str(v1 + v2))

    def test_define_recursive_nary_function(self, capsys):
        eval_and_print("""
            (define (max x . z)
                (if (null? z) x
                    (apply max
                        (cons
                            (if (b< x (car z)) (car z) x)
                            (cdr z)))))
                       """)
        capsys.readouterr()
        eval_and_print("(max 10 2 3 4 5 15 100 2)")
        assert_stripped_output_is(capsys, "100")
