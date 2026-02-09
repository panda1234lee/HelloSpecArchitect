from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    执行两个数值的加法运算。
    
    Args:
        a: 第一个加数 (int 或 float)
        b: 第二个加数 (int 或 float)
        
    Returns:
        两个加数的和。
        
    Raises:
        TypeError: 如果输入不是数值类型。
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers (int or float)")
    
    return a + b
