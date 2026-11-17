---
type: simulink-block
title: 'Three-axis Inertial Measurement Unit'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'GNC / Navigation'
documentation_page: 'threeaxisinertialmeasurementunit'
documentation_source_path: 'threeaxisinertialmeasurementunit.html'
language: zh-CN
chinese_source: worker-translation
---

# Three-axis Inertial Measurement Unit

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
- name: ωmeas
  summary: 测量角速率三元素向量
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

机体坐标系下的重力，指定为三元素向量，单位由 **Units** 参数指定。

**数据类型：** `double`
### 输出

### **Ameas** — 测量加速度三元素向量

加速度计输出的测量加速度，返回为三元素向量，单位由 **Units** 参数指定。

**数据类型：** `double`

### **ωmeas** — 测量角速率三元素向量

陀螺仪输出的测量角速率，返回为三元素向量，单位为弧度每秒。

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
- name: IMU location
  summary: IMU 位置 [0 0 0]（默认）| 三元素向量
  group: ''
  block_parameter: imu
  type: 字符向量
  values: 三元素向量
  default: '''[0 0 0]'''
- name: Update rate (sec)
  summary: 更新速率 0（默认）| 标量
  group: ''
  block_parameter: i_Ts
  type: 字符向量
  values: 双精度标量
  default: '''0'''
- name: Second-order dynamics for accelerometer
  summary: 二阶动态特性 on（默认）| off
  group: ''
  block_parameter: dtype_a
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Accelerometer natural frequency (rad/sec)
  summary: 加速度计自然频率 190（默认）| 标量
  group: ''
  block_parameter: w_a
  type: 字符向量
  values: 双精度标量
  default: '''190'''
- name: Accelerometer damping ratio
  summary: 加速度计阻尼比 0.707（默认）| 标量
  group: ''
  block_parameter: z_a
  type: 字符向量
  values: 双精度标量
  default: '''0.707'''
- name: Accelerometer scale factor and cross-coupling
  summary: 比例因子和交叉耦合 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵
  group: ''
  block_parameter: a_sf_cc
  type: 字符向量
  values: 3×3 矩阵
  default: '''[1 0 0; 0 1 0; 0 0 1]'''
- name: Accelerometer measurement bias
  summary: 加速度计测量偏置 [0 0 0]（默认）| 三元素向量
  group: ''
  block_parameter: a_bias
  type: 字符向量
  values: 三元素向量
  default: '''[0 0 0]'''
- name: Accelerometer upper and lower limits
  summary: 加速度的最小值和最大值 [-inf -inf -inf inf inf inf]（默认）| 六元素向量
  group: ''
  block_parameter: a_sat
  type: 字符向量
  values: 六元素向量
  default: '''[-inf -inf -inf inf inf inf]'''
- name: Second-order dynamics for gyro
  summary: 陀螺仪二阶动态特性 on（默认）| off
  group: ''
  block_parameter: dtype_g
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Gyro natural frequency (rad/sec)
  summary: 陀螺仪自然频率 190（默认）| 标量
  group: ''
  block_parameter: w_g
  type: 字符向量
  values: 双精度标量
  default: '''190'''
- name: Gyro damping ratio
  summary: 陀螺仪阻尼比 0.707（默认）| 标量
  group: ''
  block_parameter: z_g
  type: 字符向量
  values: 双精度标量
  default: '''0.707'''
- name: Gyro scale factors and cross-coupling
  summary: 陀螺仪比例因子和交叉耦合 [1 0 0; 0 1 0; 0 0 1]（默认）| 3×3 矩阵
  group: ''
  block_parameter: g_sf_cc
  type: 字符向量
  values: 3×3 矩阵
  default: '''[1 0 0; 0 1 0; 0 0 1]'''
- name: Gyro measurement bias
  summary: 陀螺仪测量偏置 [0 0 0]（默认）| 三元素向量
  group: ''
  block_parameter: g_bias
  type: 字符向量
  values: 三元素向量
  default: '''[0 0 0]'''
- name: G-sensitive bias
  summary: 速率的最大变化量 [0 0 0]（默认）| 三元素向量
  group: ''
  block_parameter: g_sens
  type: 字符向量
  values: 三元素向量
  default: '''[0 0 0]'''
- name: Gyro upper and lower limits
  summary: 角速率的最小值和最大值 [-inf -inf -inf inf inf inf]（默认）| 六元素向量
  group: ''
  block_parameter: g_sat
  type: 字符向量
  values: 六元素向量
  default: '''[-inf -inf -inf inf inf inf]'''
- name: Noise on
  summary: 白噪声 on（默认）| off
  group: ''
  block_parameter: i_rand
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Noise seeds
  summary: 噪声种子 [23093 23094 23095 23096 23097 23098]（默认）| 六元素向量
  group: ''
  block_parameter: i_seeds
  type: 字符向量
  values: 六元素向量
  default: '''[23093 23094 23095 23096 23097 23098]'''
- name: Noise power
  summary: 噪声功率 [0.001 0.001 0.001 0.0001 0.0001 0.0001]（默认）| 六元素向量
  group: ''
  block_parameter: i_pow
  type: 字符向量
  values: 六元素向量
  default: '''[0.001 0.001 0.001 0.0001 0.0001 0.0001]'''
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

### **IMU location** — IMU 位置 `[0 0 0]`（默认）| 三元素向量

IMU 的位置（也是加速度计组的位置），从零基准点（通常为机头）向后、沿垂直中心线向右、沿水平中心线向上测量。该测量参考与重心输入相同。单位由 **Units** 参数指定。

#### 编程使用

|  |
| --- |
| **模块参数**：`imu` |
| **类型**：字符向量 |
| **值**：三元素向量 |
| **默认值**：`'[0 0 0]'` |

### **Update rate (sec)** — 更新速率 `0`（默认）| 标量

加速度计和陀螺仪的更新速率，指定为双精度标量，单位为秒。更新速率为 0 时创建连续加速度计和连续陀螺仪。如果选中 **Noise on** 复选框且更新速率为 0，则模块以 0.1 的速率更新噪声。

**提示**

如果您：

- 将此参数值更新为 0（连续）
- 为模型配置定步长求解器

您还必须在 **Solver** 窗格中选中 **Automatically handle rate transition for data transfer** 复选框。此复选框使软件能够正确处理速率转换。

#### 编程使用

|  |
| --- |
| **模块参数**：`i_Ts` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'0'` |

### **Second-order dynamics for accelerometer** — 二阶动态特性 `on`（默认）| `off`

要对加速度读数应用二阶动态特性，请选中此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`dtype_a` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Accelerometer natural frequency (rad/sec)** — 加速度计自然频率 `190`（默认）| 标量

加速度计的自然频率，指定为双精度标量，单位为弧度每秒。

#### 依赖关系

要启用此参数，请选中 **Second order dynamics for accelerometer**。

#### 编程使用

|  |
| --- |
| **模块参数**：`w_a` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'190'` |

### **Accelerometer damping ratio** — 加速度计阻尼比 `0.707`（默认）| 标量

加速度计的阻尼比，指定为双精度标量，无量纲。

#### 依赖关系

要启用此参数，请选中 **Second order dynamics for accelerometer**。

#### 编程使用

|  |
| --- |
| **模块参数**：`z_a` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'0.707'` |

### **Accelerometer scale factor and cross-coupling** — 比例因子和交叉耦合 `[1 0 0; 0 1 0; 0 0 1]`（默认）| 3×3 矩阵

比例因子和交叉耦合，指定为 3×3 矩阵，用于将加速度计从机体轴倾斜以及沿机体轴缩放加速度。

#### 编程使用

|  |
| --- |
| **模块参数**：`a_sf_cc` |
| **类型**：字符向量 |
| **值**：3×3 矩阵 |
| **默认值**：`'[1 0 0; 0 1 0; 0 0 1]'` |

### **Accelerometer measurement bias** — 加速度计测量偏置 `[0 0 0]`（默认）| 三元素向量

沿加速度计各轴的长期偏置，指定为三元素向量，单位由 **Units** 参数指定。

#### 编程使用

|  |
| --- |
| **模块参数**：`a_bias` |
| **类型**：字符向量 |
| **值**：三元素向量 |
| **默认值**：`'[0 0 0]'` |

### **Accelerometer upper and lower limits** — 加速度的最小值和最大值 `[-inf -inf -inf inf inf inf]`（默认）| 六元素向量

加速度计各轴加速度的三个最小值和三个最大值，指定为六元素向量，单位由 **Units** 参数指定。

#### 编程使用

|  |
| --- |
| **模块参数**：`a_sat` |
| **类型**：字符向量 |
| **值**：六元素向量 |
| **默认值**：`'[-inf -inf -inf inf inf inf]'` |

### **Second-order dynamics for gyro** — 陀螺仪二阶动态特性 `on`（默认）| `off`

要对陀螺仪读数应用二阶动态特性，请选中此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`dtype_g` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Gyro natural frequency (rad/sec)** — 陀螺仪自然频率 `190`（默认）| 标量

陀螺仪的自然频率，指定为双精度标量，单位为弧度每秒。

#### 依赖关系

要启用此参数，请选中 **Second-order dynamics for gyro**。

#### 编程使用

|  |
| --- |
| **模块参数**：`w_g` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'190'` |

### **Gyro damping ratio** — 陀螺仪阻尼比 `0.707`（默认）| 标量

陀螺仪的阻尼比，指定为双精度标量。

#### 依赖关系

要启用此参数，请选中 **Second-order dynamics for gyro**。

#### 编程使用

|  |
| --- |
| **模块参数**：`z_g` |
| **类型**：字符向量 |
| **值**：双精度标量 |
| **默认值**：`'0.707'` |

### **Gyro scale factors and cross-coupling** — 陀螺仪比例因子和交叉耦合 `[1 0 0; 0 1 0; 0 0 1]`（默认）| 3×3 矩阵

陀螺仪比例因子和交叉耦合，指定为 3×3 矩阵，用于将陀螺仪从机体轴倾斜以及沿机体轴缩放角速率。

#### 编程使用

|  |
| --- |
| **模块参数**：`g_sf_cc` |
| **类型**：字符向量 |
| **值**：3×3 矩阵 |
| **默认值**：`'[1 0 0; 0 1 0; 0 0 1]'` |

### **Gyro measurement bias** — 陀螺仪测量偏置 `[0 0 0]`（默认）| 三元素向量

沿陀螺仪各轴的长期偏置，指定为三元素向量，单位为弧度每秒。

#### 编程使用

|  |
| --- |
| **模块参数**：`g_bias` |
| **类型**：字符向量 |
| **值**：三元素向量 |
| **默认值**：`'[0 0 0]'` |

### **G-sensitive bias** — 速率的最大变化量 `[0 0 0]`（默认）| 三元素向量

由线加速度引起的速率最大变化量，指定为三元素向量，单位为弧度每秒每 g 单位。

#### 编程使用

|  |
| --- |
| **模块参数**：`g_sens` |
| **类型**：字符向量 |
| **值**：三元素向量 |
| **默认值**：`'[0 0 0]'` |

### **Gyro upper and lower limits** — 角速率的最小值和最大值 `[-inf -inf -inf inf inf inf]`（默认）| 六元素向量

陀螺仪各轴角速率的三个最小值和三个最大值，指定为六元素向量，单位为弧度每秒。

#### 编程使用

|  |
| --- |
| **模块参数**：`g_sat` |
| **类型**：字符向量 |
| **值**：六元素向量 |
| **默认值**：`'[-inf -inf -inf inf inf inf]'` |

### **Noise on** — 白噪声 `on`（默认）| `off`

要对加速度和陀螺仪读数应用白噪声，请选中此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`i_rand` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Noise seeds** — 噪声种子 `[23093 23094 23095 23096 23097 23098]`（默认）| 六元素向量

加速度计和陀螺仪各轴高斯噪声生成器的标量种子，指定为六元素向量。

#### 依赖关系

要启用此参数，请选中 **Noise on**。

#### 编程使用

|  |
| --- |
| **模块参数**：`i_seeds` |
| **类型**：字符向量 |
| **值**：六元素向量 |
| **默认值**：`'[23093 23094 23095 23096 23097 23098]'` |

### **Noise power** — 噪声功率 `[0.001 0.001 0.001 0.0001 0.0001 0.0001]`（默认）| 六元素向量

加速度计和陀螺仪各轴白噪声的功率谱密度（PSD）高度，指定为六元素向量，单位为：

- (m/s2)/Hz，当 **Units** 设置为 `Metric (MKS)` 时
- (ft/s2)/Hz，当 **Units** 设置为 `English` 时

#### 依赖关系

要启用此参数，请选中 **Noise on**。

#### 编程使用

|  |
| --- |
| **模块参数**：`i_pow` |
| **类型**：字符向量 |
| **值**：六元素向量 |
| **默认值**：`'[0.001 0.001 0.001 0.0001 0.0001 0.0001]'` |
## 所属库

Aerospace Blockset / GNC / Navigation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现三轴惯性测量单元（IMU）

Three-Axis Inertial Measurement Unit 模块实现了一个包含三轴加速度计和三轴陀螺仪的惯性测量单元（IMU）。

有关方程和误差应用的描述，请参阅 Three-axis Accelerometer 和 Three-axis Gyroscope。

Three-axis Inertial Measurement Unit 模块图标显示从 **Units** 参数选择的输入和输出单位。
