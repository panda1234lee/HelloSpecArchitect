# Python 加法计算器 (Python Adder) 技术设计文档

## 1. 系统概要 (System Summary)
> 本功能将实现一个轻量级的 Python 工具库，提供核心的加法运算功能。该库将被设计为独立的模块 `adder.py`，以便于被其他 Python 服务或脚本导入调用。

## 2. 决策记录 (Decision Rationale)
- **原方案选择**: 使用 Python 标准库实现，不引入额外的第三方数学库（如 NumPy），以保持轻量和极简的依赖关系。
- **权衡 (Trade-offs)**: 选择了在函数内部进行手动的类型检查 (`isinstance`)。虽然增加了几行代码，但能确保在调用初期拦截非法类型，防止隐式的类型强制转换错误。

## 3. 详细设计 (Detailed Design)
### 3.1 逻辑流程 (Logic Flow)
```mermaid
graph TD
    A[开始: add(a, b)] --> B{校验 a, b 均为数值?}
    B -- 否 --> C[抛出 TypeError]
    B -- 是 --> D[执行 a + b]
    D --> E[返回计算结果]
    C --> F[结束]
    E --> F[结束]
```

### 3.2 目录与模块结构 (Structure)
- `src/calculator/`:
    - `__init__.py`: 包初始化。
    - `adder.py`: 核心加法函数实现。
- `tests/`:
    - `test_adder.py`: 针对加法功能的单元测试。

### 3.3 数据模型 (Data Models)
> 本功能不涉及复杂数据模型，仅处理基本数值类型：
- `a`: `int` | `float`
- `b`: `int` | `float`
- `return`: `int` | `float`

### 3.4 交互接口 (APIs / Props)
- **API 定义**:
    - `add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]`
    - **输入**: 两个加数。
    - **输出**: 计算结果。

## 4. 安全性与异常处理 (Security & Error Handling)
- **防御性编程**: 
  - 使用 `isinstance(x, (int, float))` 严格过滤掉 `str`, `list`, `None` 等非法类型。
  - 错误信息需清晰指明是哪个参数类型错误：`"Arguments must be numbers (int or float)"`。

## 5. 验证方案 (Verification Plan)
- **自动化测试**: 
  - `test_add_integers`: 验证 1+1=2。
  - `test_add_floats`: 验证 1.5+2.5=4.0。
  - `test_invalid_types`: 传入 `"1"` 或 `None` 时，断言系统抛出 `TypeError`。
- **手动验证**:
  - 在终端运行 `python -c "from calculator.adder import add; print(add(10, 20))"`。
