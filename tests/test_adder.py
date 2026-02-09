import pytest
import sys
import os

# 将 src 目录添加到模块搜索路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from calculator.adder import add

def test_add_integers():
    """测试整数加法"""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_floats():
    """测试浮点数加法"""
    assert add(1.5, 2.5) == 4.0
    assert add(-1.1, 1.1) == 0.0

def test_add_mixed_types():
    """测试混合类型加法"""
    assert add(1, 2.5) == 3.5
    assert add(1.5, 2) == 3.5

def test_invalid_types():
    """测试非法类型输入"""
    with pytest.raises(TypeError, match="Arguments must be numbers"):
        add("1", 2)
    with pytest.raises(TypeError, match="Arguments must be numbers"):
        add(1, None)
    with pytest.raises(TypeError, match="Arguments must be numbers"):
        add([], {})

if __name__ == "__main__":
    # 在 Spyder 中直接运行此文件时，会触发 pytest 执行
    pytest.main([__file__])
