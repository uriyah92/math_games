import typing
import ex7_helper

# multiply x by y


def mult(x: ex7_helper.N, y: int) -> ex7_helper.N:
    if y == 0:
        return 0
    return ex7_helper.add(x, mult(x, ex7_helper.subtract_1(y)))

# check if n is even


def is_even(n: int) -> bool:
    if n == 0:
        return True
    return is_even(ex7_helper.subtract_1(n)) == False

# multiply x by y


def log_mult(x: ex7_helper.N, y: int) -> ex7_helper.N:
    if y == 0:
        return 0
    if ex7_helper.is_odd(y):
        y_sub = ex7_helper.subtract_1(y)
        m = ex7_helper.add(x, log_mult(x, ex7_helper.divide_by_2(y_sub)))
        n = log_mult(x, ex7_helper.divide_by_2(y_sub))
    else:
        m = log_mult(x, ex7_helper.divide_by_2(y))
        n = log_mult(x, ex7_helper.divide_by_2(y))
    return ex7_helper.add(m, n)

# check if b could be base for a power that equals x


def is_power(b: int, x: int) -> bool:
    a = b
    n = 1
    return calculate(a, b, x, n) >= 0

# helper func for is_power


def calculate(a: int, b: int, x: int, n: int) -> int:
    if b == x:
        return n
    if x == 1:
        return 0
    if b > x:
        return ex7_helper.subtract_1(0)
    return calculate(a, log_mult(a, b), x, ex7_helper.add(n, 1))

# return the reversed version of a givven string


def reverse(s: str) -> str:
    if len(s) == 1:
        return s
    c = s[0]
    string = s[1:]
    return ex7_helper.append_to_end(reverse(string), c)

# solve the hanoi pazzle


def play_hanoi(hanoi: typing.Any, n: int, src: typing.Any,
               dest: typing.Any, temp: typing.Any) -> None:
    if n <= 0:
        return
    if n == 1:
        hanoi.move(src, dest)
    if n == 2:
        hanoi.move(src, temp)
        hanoi.move(src, dest)
        hanoi.move(temp, dest)
    if n > 2:
        play_hanoi(hanoi, n-1, src, temp, dest)
        play_hanoi(hanoi, 1, src, dest, temp)
        play_hanoi(hanoi, n-1, temp, dest, src)

# return how many 1s in n


def number_of_ones(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n < 10:
        return number_of_ones(n-1)

    if n >= 1000:
        a = n//1000
        b = n//100-a*10
        c = n//10-a*100-b*10
        d = n % 10
        return number_of_ones(n-1)+(a == 1)+(b == 1)+(c == 1)+(d == 1)

    if n >= 100:
        b = n//100
        c = n//10-b*10
        d = n % 10
        return number_of_ones(n-1)+(b == 1)+(c == 1)+(d == 1)

    if n >= 10:
        c = n//10
        d = n % 10
        return number_of_ones(n-1)+(c == 1)+(d == 1)

    return 0


''' check if 1d lists l1 and l2 are identical
 (helper func for compare_2d_lists)'''


def compare_1d_lists(l1: typing.List[int], l2: typing.List[int]) -> bool:
    if len(l1) != len(l2):
        return False
    if len(l1) == 0:
        return True
    if l1[0] == l2[0]:
        return compare_1d_lists(l1[1:], l2[1:])
    else:
        return False


# check if 2d lists l1 and l2 are identical
def compare_2d_lists(l1: typing.List[typing.List[int]],
                     l2: typing.List[typing.List[int]]) -> bool:
    if len(l1) != len(l2):
        return False
    if len(l1) == 0:
        return True
    if compare_1d_lists(l1[0], l2[0]):

        return compare_2d_lists(l1[1:], l2[1:])
    else:
        return False

# deep copy list (helper func for magic_list)


def copy(lst: typing.List[int], lst2: typing.List[int]) -> None:
    if len(lst) == 0:
        return
    copy(lst[1:], lst2+[lst[0]])

# helper func for magic_list


def creator(lst: typing.List[typing.Any], n: int) -> list[typing.Any]:
    if n == 0:
        return []
    old: typing.List[typing.Any] = []
    copy(lst, old)
    new = creator(old, n-1)
    old.append(new)
    return new+old

# return the magic list of n


def magic_list(n: int) -> list[typing.Any]:
    return creator([], n)


print(magic_list(3))
