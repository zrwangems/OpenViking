---
type: simulink-block
title: 'Three-axis Gyroscope'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control (GNC) / Navigation'
documentation_page: 'threeaxisgyroscope'
documentation_source_path: 'threeaxisgyroscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Three-axis Gyroscope

## 端口

### 输入

### **ω** — 角速率三元素向量

机体固定轴中的角速率，指定为三元素向量，单位为 radians per second。

**数据类型：** `double`

### **G's** — 加速度三元素向量

机体固定轴中的加速度，指定为三元素向量，单位为 Gs。

**数据类型：** `double`
### 输出

### **ωmeas** — 测量角速率三元素向量

来自陀螺仪的测量角速率，返回为三元素向量，单位为 radians per second。

**数据类型：** `double`

## 参数

### **二阶动态特性** — 二阶动态特性 `on` (默认) | `off`

要对陀螺仪读数应用二阶动态特性，请选中此复选框。

#### 程序化用法

|  |
| --- |
| **模块参数**：`dtype_g` |
| **类型**：character vector |
| **取值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **固有频率 (rad/sec)** — 固有频率 `190` (默认) | 标量

陀螺仪的固有频率，指定为 double scalar，单位为 radians per second。

#### 程序化用法

|  |
| --- |
| **模块参数**：`w_g` |
| **类型**：character vector |
| **取值**：double scalar |
| **默认值**：`'190'` |

### **阻尼比** — 阻尼比 `0.707` (默认) | 标量

陀螺仪的阻尼比，指定为 double scalar。

#### 程序化用法

|  |
| --- |
| **模块参数**：`z_g` |
| **类型**：character vector |
| **取值**：double scalar |
| **默认值**：`'0.707'` |

### **比例因子和交叉耦合** — 比例因子和交叉耦合 `[1 0 0; 0 1 0; 0 0 1]` (默认) | 3-by-3 矩阵

比例因子和交叉耦合，指定为 3-by-3 matrix，用于使陀螺仪偏离机体轴，并沿机体轴缩放加速度。

#### 程序化用法

|  |
| --- |
| **模块参数**：`g_sf_cc` |
| **类型**：character vector |
| **取值**：3-by-3 matrix |
| **默认值**：`'[1 0 0; 0 1 0; 0 0 1]'` |

### **测量偏置** — 测量偏置 `[0 0 0]` (默认) | 三元素向量

沿陀螺仪各轴的长期偏置，指定为三元素向量，单位为 radians per second。

#### 程序化用法

|  |
| --- |
| **模块参数**：`g_bias` |
| **类型**：character vector |
| **取值**：3-by-3 matrix |
| **默认值**：`'[0 0 0]'` |

### **G 敏感偏置** — 速率最大变化 `[0 0 0]` (默认) | 三元素向量

由于线性加速度导致的速率最大变化，指定为三元素向量，单位为 radians per second per g-unit。

#### 程序化用法

|  |
| --- |
| **模块参数**：`g_sen` |
| **类型**：character vector |
| **取值**：three-element vector |
| **默认值**：`'[0 0 0]'` |

### **更新率 (sec)** — 更新率 `0` (默认) | 标量

陀螺仪的更新率，指定为 double scalar，单位为 seconds。更新率为 0 会创建连续陀螺仪。如果选中了 **噪声开启** 复选框且更新率为 0，则模块以 0.1 的速率更新噪声。

**提示**

如果您：

- 将此参数值更新为 0（连续）
- 为模型配置固定步长求解器

还必须选中 **求解器** 窗格中的 **自动处理数据传输的速率转换** 复选框。此复选框使软件能够正确处理速率转换。

#### 程序化用法

|  |
| --- |
| **模块参数**：`g_Ts` |
| **类型**：character vector |
| **取值**：double scalar |
| **默认值**：`'0'` |

### **噪声开启** — 白噪声 `on` (默认) | `off`

要对陀螺仪读数应用白噪声，请选中此复选框。

#### 程序化用法

|  |
| --- |
| **模块参数**：`g_rand` |
| **类型**：character vector |
| **取值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **噪声种子** — 噪声种子 `[23093 23094 23095]` (默认) | 三元素向量

陀螺仪每个轴的高斯噪声生成器的标量种子，指定为三元素向量。

#### 依赖关系

要启用此参数，请选中 **噪声开启**。

#### 程序化用法

|  |
| --- |
| **模块参数**：`g_seeds` |
| **类型**：character vector |
| **取值**：three-element vector |
| **默认值**：`'[23093 23094 23095]'` |

### **噪声功率** — 噪声功率 `[0.0001 0.0001 0.0001]` (默认) | 三元素向量

陀螺仪每个轴的白噪声功率谱密度 (PSD) 高度，指定为三元素向量，单位为 (rad/s)2/Hz。

#### 依赖关系

要启用此参数，请选中 **噪声开启**。

#### 程序化用法

|  |
| --- |
| **模块参数**：`g_pow` |
| **类型**：character vector |
| **取值**：three-element vector |
| **默认值**：`'[0.0001 0.0001 0.0001]'` |

### **输出下限和上限** — 角速率最小值和最大值 `[-inf -inf -inf inf inf inf]` (默认) | 六元素向量

陀螺仪各轴角速率的三个最小值和三个最大值，指定为六元素向量，单位为 radians per second。

#### 程序化用法

|  |
| --- |
| **模块参数**：`g_sat` |
| **类型**：character vector |
| **取值**：six-element vector |
| **默认值**：`'[-inf -inf -inf inf inf inf]'` |

## 所属库

Aerospace Blockset / GNC / Navigation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现三轴陀螺仪

Three-Axis Gyroscope 模块在三轴中的每个轴上实现一个陀螺仪。有关测量得到的机体角速率的详细信息，请参阅算法。

可选地，若要对模块输入和动态特性应用离散化，同时对测量得到的机体角速率进行非线性化，请使用 Saturation 模块。
