---
type: simulink-block
title: 'Three-axis Accelerometer'
family: 'aeroblks'
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
```yaml
ports:
- name: Ab
  summary: 实际加速度三元素向量
  direction: input
  data_types: double
- name: ω
  summary: 角速率三元素向量
  direction: input
  data_types: double
- name: dω/dt
  summary: 角加速度三元素向量
  direction: input
  data_types: double
- name: CG
  summary: 重心位置三元素向量
  direction: input
  data_types: double
- name: g
  summary: 重力三元素向量
  direction: input
  data_types: double
- name: Ameas
  summary: 测量加速度三元素向量
  direction: output
  data_types: double
```

### 输入

### **Ab** — 实际加速度三元素向量

在机体坐标系下的实际加速度，指定为三元素向量，单位由 **Units** 参数指定。

**数据类型：** `double`

### **ω** — 角速率三元素向量

在机体坐标系下的角速率，指定为三元素向量，单位为弧度每秒。

**数据类型：** `double`

### **dω/dt** — 角加速度三元素向量

在机体坐标系下的角加速度，指定为三元素向量，单位为弧度每二次方秒。

**数据类型：** `double`

### **CG** — 重心位置三元素向量

重心位置，指定为三元素向量，单位由 **Units** 参数指定。

**数据类型：** `double`

### **g** — 重力三元素向量

机体轴下的重力，指定为三元素向量，单位由 **Units** 参数指定。

**数据类型：** `double`
### 输出

### **Ameas** — 测量加速度三元素向量

加速度计输出的测量加速度，以三元素向量形式返回，单位由 **Units** 参数指定。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 单位 Metric (MKS)（默认）| English
  group: ''
  block_parameter: units
  type: 字符向量
  values: '''Metric (MKS)'' | ''English'''
  default: '''Metric (MKS)'''
- name: Accelerometer location
  summary: 加速度计位置 [0 0 0]（默认）| 三元素向量
  group: ''
  block_parameter: acc
  type: 字符向量
  values: 三元素向量
  default: '''[0 0 0]'''
- name: Subtract gravity
  summary: 减去重力 on（默认）| off
  group: ''
  block_parameter: gtype
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Second order dynamics
  summary: 二阶动态特性 on（默认）| off
  group: ''
  block_parameter: dtype_a
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Natural frequency (rad/sec)
  summary: 自然频率 190（默认）| 标量
  group: ''
  block_parameter: w_a
  type: 字符向量
  values: 双精度标量
  default: '''190'''
- name: Damping ratio
  summary: 阻尼比 0.707（默认）| 标量
  group: ''
  block_parameter: z_a
  type: 字符向量
  values: 双精度标量
  default: '''0.707'''
- name: Scale factors and cross-coupling
  summary: 比例因子和交叉耦合 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵
  group: ''
  block_parameter: a_sf_cc
  type: 字符向量
  values: 3×3 矩阵
  default: '''[1 0 0; 0 1 0; 0 0 1]'''
- name: Measurement bias
  summary: 测量偏置 [0 0 0]（默认）| 三元素向量
  group: ''
  block_parameter: a_bias
  type: 字符向量
  values: 3×3 矩阵
  default: '''[0 0 0]'''
- name: Update rate (sec)
  summary: 更新率 0（默认）| 标量
  group: ''
  block_parameter: a_Ts
  type: 字符向量
  values: 双精度标量
  default: '''0'''
- name: Noise on
  summary: 白噪声 on（默认）| off
  group: ''
  block_parameter: a_rand
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Noise seeds
  summary: 噪声种子 [23093 23094 23095]（默认）| 三元素向量
  group: ''
  block_parameter: a_seeds
  type: 字符向量
  values: 三元素向量
  default: '''[23093 23094 23095]'''
- name: Noise power
  summary: 噪声功率 [0.001 0.001 0.001]（默认）| 三元素向量
  group: ''
  block_parameter: a_pow
  type: 字符向量
  values: 三元素向量
  default: '''[0.001 0.001 0.001]'''
- name: Lower and upper output limits
  summary: 加速度的最小值和最大值 [-inf -inf -inf inf inf inf]（默认）| 六元素向量
  group: ''
  block_parameter: a_sat
  type: 字符向量
  values: 六元素向量
  default: '''[-inf -inf -inf inf inf inf]'''
```

### **Units** — 单位 `Metric (MKS)`（默认）| `English`

输入和输出单位，指定为：

| 单位 | 加速度 | 长度 |
| --- | --- | --- |
| `Metric (MKS)` | 米每二次方秒 | 米 |
| `English`（英制） | 英尺每二次方秒 | 英尺 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认值**：`'Metric (MKS)'` |

### **Accelerometer location** — 加速度计位置 `[0 0 0]`（默认）| 三元素向量

加速度计组的位置，指定为三元素向量，从零基准点（通常为机头）测量至后方、垂直中心线右侧以及水平中心线上方。该测量参考与重心输入相同。单位由 **Units** 参数指定。

#### 编程使用

|  |
| --- |
| **模块参数**：`acc` |
| **类型**：字符向量 |
| **值**：三元素向量 |
| **默认值**：`'[0 0 0]'` |

### **Subtract gravity** — 减去重力 `on`（默认）| `off`

要从加速度读数中减去重力，请选中此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`gtype` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Second order dynamics** — 二阶动态特性 `on`（默认）| `off`

要对加速度读数应用二阶动态特性，请选中此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`dtype_a` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Natural frequency (rad/sec)** — 自然频率 `190`（默认）| 标量

加速度计的自然频率，指定为双精度标量，单位为弧度每秒。

#### 编程使用

|  |
| --- |
| **模块参数**：`w_a` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'190'` |

### **Damping ratio** — 阻尼比 `0.707`（默认）| 标量

加速度计的阻尼比，指定为双精度标量，无量纲。

#### 编程使用

|  |
| --- |
| **模块参数**：`z_a` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'0.707'` |

### **Scale factors and cross-coupling** — 比例因子和交叉耦合 `[1 0 0; 0 1 0; 0 0 1]`（默认）| 3×3 矩阵

比例因子和交叉耦合，指定为 3×3 矩阵，用于将加速度计从机体轴倾斜以及沿机体轴缩放加速度。

#### 编程使用

|  |
| --- |
| **模块参数**：`a_sf_cc` |
| **类型**：字符向量 |
| **值**：3×3 矩阵 |
| **默认值**：`'[1 0 0; 0 1 0; 0 0 1]'` |

### **Measurement bias** — 测量偏置 `[0 0 0]`（默认）| 三元素向量

沿加速度计各轴的长期偏置，指定为三元素向量，单位由 **Units** 参数指定。

#### 编程使用

|  |
| --- |
| **模块参数**：`a_bias` |
| **类型**：字符向量 |
| **值**：3×3 矩阵 |
| **默认值**：`'[0 0 0]'` |

### **Update rate (sec)** — 更新率 `0`（默认）| 标量

加速度计的更新率，指定为双精度标量，单位为秒。更新率为 0 时创建连续加速度计。如果选中 **Noise on** 复选框且更新率为 0，则模块以 0.1 的速率更新噪声。

**提示**

如果您：

- 将此参数值更新为 0（连续）
- 为模型配置定步长求解器

则还必须在 **Solver** 窗格中选中 **Automatically handle rate transition for data transfer** 复选框。此复选框使软件能够正确处理速率转换。

#### 编程使用

|  |
| --- |
| **模块参数**：`a_Ts` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'0'` |

### **Noise on** — 白噪声 `on`（默认）| `off`

要对加速度读数应用白噪声，请选中此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`a_rand` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Noise seeds** — 噪声种子 `[23093 23094 23095]`（默认）| 三元素向量

加速度计各轴高斯噪声生成器的标量种子，指定为三元素向量。

#### 依赖关系

要启用此参数，请选中 **Noise on**。

#### 编程使用

|  |
| --- |
| **模块参数**：`a_seeds` |
| **类型**：字符向量 |
| **值**：三元素向量 |
| **默认值**：`'[23093 23094 23095]'` |

### **Noise power** — 噪声功率 `[0.001 0.001 0.001]`（默认）| 三元素向量

加速度计各轴白噪声的功率谱密度（PSD）高度，指定为三元素向量，单位为：

- (m/s2)/Hz，当 **Units** 设置为 `Metric (MKS)` 时
- (ft/s2)/Hz，当 **Units** 设置为 `English` 时

#### 依赖关系

要启用此参数，请选中 **Noise on**。

#### 编程使用

|  |
| --- |
| **模块参数**：`a_pow` |
| **类型**：字符向量 |
| **值**：三元素向量 |
| **默认值**：`'[0.001 0.001 0.001]'` |

### **Lower and upper output limits** — 加速度的最小值和最大值 `[-inf -inf -inf inf inf inf]`（默认）| 六元素向量

加速度计各轴的三个最小值和三个最大值，指定为六元素向量，单位由 **Units** 参数指定。

#### 编程使用

|  |
| --- |
| **模块参数**：`a_sat` |
| **类型**：字符向量 |
| **值**：六元素向量 |
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

实现三轴加速度计

Three-Axis Accelerometer 模块在三个轴的每一个上实现一个加速度计。有关理想测量加速度的更多信息，请参阅 Algorithms。

可选地，要对 Three-Axis Accelerometer 模块的输入和动态特性应用离散化以及测量加速度的非线性化，请使用 Saturation 模块。

Three-axis Accelerometer 模块图标显示从 **Units** 参数选择的输入和输出单位。
