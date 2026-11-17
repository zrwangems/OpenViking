---
type: simulink-block
title: 'Three-axis Accelerometer'
family: 'gnc'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'GNC / Navigation'
documentation_page: 'threeaxisaccelerometer'
documentation_source_path: 'threeaxisaccelerometer.html'
language: zh-CN
chinese_source: worker-translation
---

# Three-axis Accelerometer

## 端口

### 输入

### **Ab** — 实际加速度 three-element vector

机体固定轴中的实际加速度，指定为 three-element vector，单位由 **Units** 参数指定。

**数据类型：** `double`

### **ω** — 角速率 three-element vector

机体固定轴中的角速率，指定为 three-element vector，单位为 radians per second。

**数据类型：** `double`

### **dω/dt** — 角加速度 three-element vector

机体固定轴中的角加速度，指定为 three-element vector，单位为 radians per second squared。

**数据类型：** `double`

### **CG** — 重心位置 three-element vector

重心位置，指定为 three-element vector，单位由 **Units** 参数指定。

**数据类型：** `double`

### **g** — 重力 three-element vector

机体轴中的重力，指定为 three-element vector，单位由 **Units** 参数指定。

**数据类型：** `double`

### 输出

### **Ameas** — 测量加速度 three-element vector

来自加速度计的测量加速度，返回为 three-element vector，单位由 **Units** 参数指定。

**数据类型：** `double`

## 参数

### **Units** — 单位 `Metric (MKS)` (默认) | `English`

输入和输出单位，指定为：

| 单位 | 加速度 | 长度 |
| --- | --- | --- |
| `Metric (MKS)` | Meters per second squared | Meters |
| `English` (British Imperial) | Feet per second squared | Feet |

#### 程序化使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English'` |
| **默认值**: `'Metric (MKS)'` |

### **Accelerometer location** — 加速度计位置 `[0 0 0]` (默认) | three-element vector

加速度计组的位置，指定为 three-element vector，从零基准（通常为机头）向后、垂直中心线向右、水平中心线向上测量。该测量参考与重心输入相同。单位是由 **Units** 参数指定的单位。

#### 程序化使用

|  |
| --- |
| **模块参数**: `acc` |
| **类型**: character vector |
| **值**: three-element vector |
| **默认值**: `'[0 0 0]'` |

### **Subtract gravity** — 减去重力 `on` (默认) | `off`

要从加速度读数中减去重力，请选中此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**: `gtype` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **Second order dynamics** — 二阶动态 `on` (默认) | `off`

要对加速度读数应用二阶动态，请选中此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**: `dtype_a` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **Natural frequency (rad/sec)** — 固有频率 `190` (默认) | scalar

加速度计的固有频率，指定为 double scalar，单位为 radians per second。

#### 程序化使用

|  |
| --- |
| **模块参数**: `w_a` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'190'` |

### **Damping ratio** — 阻尼比 `0.707` (默认) | scalar

加速度计的阻尼比，指定为 double scalar，无维度。

#### 程序化使用

|  |
| --- |
| **模块参数**: `z_a` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'0.707'` |

### **Scale factors and cross-coupling** — 比例因子和交叉耦合 `[1 0 0; 0 1 0; 0 0 1]` (默认) | 3-by-3 matrix

比例因子和交叉耦合，指定为 3-by-3 matrix，用于使加速度计相对机体轴偏斜，并沿机体轴缩放加速度。

#### 程序化使用

|  |
| --- |
| **模块参数**: `a_sf_cc` |
| **类型**: character vector |
| **值**: 3-by-3 matrix |
| **默认值**: `'[1 0 0; 0 1 0; 0 0 1]'` |

### **Measurement bias** — 测量偏置 `[0 0 0]` (默认) | three-element vector

沿加速度计各轴的长期偏置，指定为 three-element vector，单位由 **Units** 参数指定。

#### 程序化使用

|  |
| --- |
| **模块参数**: `a_bias` |
| **类型**: character vector |
| **值**: 3-by-3 matrix |
| **默认值**: `'[0 0 0]'` |

### **Update rate (sec)** — 更新率 `0` (默认) | scalar

加速度计的更新率，指定为 double scalar，单位为 seconds。更新率为 0 会创建连续加速度计。如果选中 **Noise on** 复选框且更新率为 0，则模块以 0.1 的速率更新噪声。

**提示**

如果你：

- 将此参数值更新为 0（连续）
- 为模型配置固定步长求解器

则还必须选中 **Solver** 窗格中的 **Automatically handle rate transition for data transfer** 复选框。此复选框使软件能够正确处理速率转换。

#### 程序化使用

|  |
| --- |
| **模块参数**: `a_Ts` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'0'` |

### **Noise on** — 白噪声 `on` (默认) | `off`

要对加速度读数应用白噪声，请选中此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**: `a_rand` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **Noise seeds** — 噪声种子 `[23093 23094 23095]` (默认) | three-element vector

加速度计各轴高斯噪声生成器的标量种子，指定为 three-element vector。

#### 依赖项

要启用此参数，请选中 **Noise on**。

#### 程序化使用

|  |
| --- |
| **模块参数**: `a_seeds` |
| **类型**: character vector |
| **值**: three-element vector |
| **默认值**: `'[23093 23094 23095]'` |

### **Noise power** — 噪声功率 `[0.001 0.001 0.001]` (默认) | three-element vector

加速度计各轴白噪声的功率谱密度 (PSD) 高度，指定为 three-element vector，单位如下：

- 当 **Units** 设置为 `Metric (MKS)` 时，为 (m/s2)/Hz
- 当 **Units** 设置为 `English` 时，为 (ft/s2)/Hz

#### 依赖项

要启用此参数，请选中 **Noise on**。

#### 程序化使用

|  |
| --- |
| **模块参数**: `a_pow` |
| **类型**: character vector |
| **值**: three-element vector |
| **默认值**: `'[0.001 0.001 0.001]'` |

### **Lower and upper output limits** — 加速度的最小值和最大值 `[-inf -inf -inf inf inf inf]` (默认) | six-element vector

加速度计各轴加速度的三个最小值和三个最大值，指定为 six-element vector，单位由 **Units** 参数指定。

#### 程序化使用

|  |
| --- |
| **模块参数**: `a_sat` |
| **类型**: character vector |
| **值**: six-element vector |
| **默认值**: `'[-inf -inf -inf inf inf inf]'` |

## 所属库

Aerospace Blockset / GNC / Navigation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

实现三轴加速度计

Three-Axis Accelerometer 模块在三个轴的每个轴上实现一个加速度计。有关理想测量加速度的详细信息，请参阅 Algorithms。

可选地，要对 Three-Axis Accelerometer 模块的输入和动态应用离散化以及测量加速度的非线性化，请使用 Saturation 模块。

Three-axis Accelerometer 模块图标显示从 **Units** 参数选择的输入和输出单位。
