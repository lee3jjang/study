"""사칙연산 모듈

이 것은 사칙연산 모듈입니다.
더하기 빼다 나누기 곱하기가 됩니다.



"""

def sum(x: float, y: float) -> float:
    """두 수를 받아 더하는 함수

    Args:
        a (float): 숫자 1개
        b (float): 다른 숫자 1개

    Returns:
        float: 합친 수를 반환
 
    Example:
        >>> sum(4, 2)
        2
    """
    return x + y