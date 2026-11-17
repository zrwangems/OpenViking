---
type: simulink-block
title: 'Signal From Workspace'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'signalfromworkspace'
documentation_source_path: 'ref/signalfromworkspace.html'
language: zh-CN
chinese_source: worker-translation
---

# Signal From Workspace

## 端口
```yaml
ports:
- name: Port_1
  summary: 从工作区导入的信号 标量 | 向量 | 矩阵 | 三维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输出

### **Port\_1** — 从工作区导入的信号 标量 | 向量 | 矩阵 | 三维数组

从工作区导入的信号，形式为标量、向量、矩阵或三维数组。

当 **Signal** 参数指定一个 *M*×*N* 矩阵（*M*≠1）时，*N* 列中的每一列都被视为一个独立的通道。您在 **Samples per frame** 参数中指定帧大小 *M*o。输出是一个 *M*o×*N* 矩阵，包含来自每个信号通道的 *M*o 个连续采样。您在 **Sample time** 参数中指定输出采样周期 *T*s，输出帧周期为 *M*o*T*s。为方便起见，导入的行向量（*M*=1）被视为单个通道，因此输出维度为 *M*o×1。

当 **Signal** 参数指定一个 *M*×*N*×*P* 数组时，*P* 个页（每个为一个 *M*×*N* 矩阵）按周期 *T*s 依次输出。**Samples per frame** 参数必须设置为 `1`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Signal
  summary: 要导入的信号 1:10（默认）| MATLAB 工作区变量 | MATLAB 表达式
  group: ''
- name: Sample time
  summary: 输出采样周期 1（默认）| 标量
  group: ''
- name: Samples per frame
  summary: 每帧采样数 1（默认）| 正整数
  group: ''
- name: Form output after final data value by
  summary: 最终导入信号值之后要输出的值 Setting to zero（默认）| Holding final value | Cyclic repetition
  group: ''
- name: Warn when frame size does not evenly divide input length
  summary: 当输入长度不是帧大小的整数倍时发出警告 off（默认）| on
  group: ''
```

### **Signal** — 要导入的信号 `1:10`（默认）| MATLAB 工作区变量 | MATLAB 表达式

要从中导入信号的 MATLAB 工作区变量名称，或指定信号的有效 MATLAB 表达式。

### **Sample time** — 输出采样周期 `1`（默认）| 标量

输出的采样周期 *T*s，指定为标量。输出帧周期为 *M*o*T*s。

### **Samples per frame** — 每帧采样数 `1`（默认）| 正整数

要缓冲到每个输出帧中的采样数 *M*o，指定为正整数标量。当您在 **Signal** 参数中指定三维数组时，此值必须为 `1`。

### **Form output after final data value by** — 最终导入信号值之后要输出的值 `Setting to zero`（默认）| `Holding final value` | `Cyclic repetition`

指定在生成所有指定的信号采样之后的输出。

- 当您指定 `Setting To Zero` 时，模块在生成信号的最后一帧之后，在仿真持续时间内生成零值输出。
- 当您指定 `Holding Final Value` 时，模块在生成信号的最后一帧之后，在仿真持续时间内重复最终采样。
- 当您指定 `Cyclic Repetition` 时，模块在到达信号中的最后一个采样后从头开始重复信号。如果您在 **Samples per frame** 参数中指定的帧大小不能整除输入长度，则会在 Signal From Workspace 子系统中插入一个缓冲模块，模型将变为多速率。如果您不希望模型变为多速率，请确保帧大小能整除输入信号长度。

模块不会将导入的信号外推到最后一个采样之后。

### **Warn when frame size does not evenly divide input length** — 当输入长度不是帧大小的整数倍时发出警告 `off`（默认）| `on`

选择 **Warn when frame size does not evenly divide input length** 参数，以便在输入长度不是帧大小的整数倍时收到提醒。当输入长度不是帧大小的整数倍时，模型将变为多速率。使用 Model Explorer 在模型范围内打开或关闭这些警告：

1. 在 **Modeling** 选项卡中，点击 **Model Explorer**。
2. 在 Model Explorer 的 **Search** 栏中，按 `by Property Name` 搜索 `ignoreOrWarnInputAndFrameLengths` 属性。每个带有 **Warn when frame size does not evenly divide input length** 复选框的模块都会出现在 **Contents** 窗格的列表中。
3. 选择您想要切换警告参数的每个模块，然后在 `ignoreOrWarnInputAndFrameLengths` 列中选择或清除该复选框。

#### 依赖关系

要启用此参数，请将 **Form output after final data value by** 设置为 `Cyclic Repetition`。
## 所属库

DSP System Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

从 MATLAB 工作区导入信号

Signal From Workspace 模块将信号从 MATLAB® 工作区导入到 Simulink® 模型中。**Signal** 参数指定包含要导入信号的 MATLAB 工作区变量名称，或定义矩阵或三维数组的任何有效 MATLAB 表达式。

与 Simulink 的 From Workspace (Simulink) 模块不同，Signal From Workspace 模块在连续输出帧之间保持输出值恒定（即不进行线性插值）。此外，初始信号值始终在 *t*=0 时立即产生。
