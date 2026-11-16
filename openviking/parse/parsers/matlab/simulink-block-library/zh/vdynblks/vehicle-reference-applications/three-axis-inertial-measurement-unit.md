---
type: simulink-block
title: 'Three-axis Inertial Measurement Unit'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'threeaxisinertialmeasurementunit'
documentation_source_path: 'ref/threeaxisinertialmeasurementunit.html'
language: zh-CN
chinese_source: worker-translation
---

# Three-axis Inertial Measurement Unit

## 端口

### 输入

### **A\_b** — 实际加速度三元素向量

体轴坐标系中的实际加速度，指定为三元素向量，单位采用所选单位。

**数据类型：** `double`

### **w** — 角速率三元素向量

体轴坐标系中的角速率，指定为三元素向量，单位为 radians per second。

**数据类型：** `double`

### **w\_dot** — 角加速度三元素向量

体轴坐标系中的角加速度，指定为三元素向量，单位为 radians per second squared。

**数据类型：** `double`

### **CG** — 重心位置三元素向量

重心位置，指定为三元素向量，单位采用所选单位。

**数据类型：** `double`

### **g** — 重力三元素向量

体轴中的重力，指定为三元素向量，单位采用所选单位。

**数据类型：** `double`

### 输出

### **A\_meas** — 测量加速度三元素向量

来自加速度计的测量加速度，指定为三元素向量，单位采用所选单位。

**数据类型：** `double`

### **w\_meas** — 测量角速率三元素向量

来自陀螺仪的测量角速率，指定为三元素向量，单位为 radians per second。

**数据类型：** `double`

## 参数

#### 主要

### **Units** — 单位 `Metric (MKS)` (默认) | `English`

输入和输出单位，指定为：

| 单位 | 加速度 | 长度 |
| --- | --- | --- |
| `Metric (MKS)` | Meters per second squared | Meters |
| `English` (British Imperial) | Feet per second squared | Feet |

#### 程序化使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认**：`'Metric (MKS)'` |

### **IMU location** — IMU 位置 `[0 0 0]` (默认) | three-element vector

IMU 的位置（也是加速度计组位置），相对于车辆重心，沿车辆固定轴。该测量参考与重心输入相同。单位采用所选长度单位。

#### 程序化使用

|  |
| --- |
| **模块参数**：`imu` |
| **类型**：character vector |
| **值**：three-element vector |
| **默认**：`'[0 0 0]'` |

### **Update rate** — 更新率 `0` (默认) | real, double scalar

加速度计和陀螺仪的更新率，指定为 real, double scalar，单位为秒。更新率为 0 会创建连续加速度计和连续陀螺仪。如果选择 **Noise on** 参数且更新率为 0，则模块以 0.1 的速率更新噪声。

**提示**

如果你：

- 将此参数值更新为 0（continuous）
- 为模型配置固定步长求解器

还必须选中 **Solver** 窗格中的 **Automatically handle rate transition for data transfer** 复选框。该复选框使软件能够正确处理速率转换。

#### 程序化使用

|  |
| --- |
| **模块参数**：`a_Ts` |
| **类型**：character vector |
| **值**：real, double scalar |
| **默认**：`'0'` |

#### 加速度计

### **Second order dynamics for accelerometer** — 二阶动态特性 `on` (默认) | `off`

要将二阶动态特性应用于加速度读数，请选中此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**：`dtype_a` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认**：`'on'` |

### **Accelerometer natural frequency (rad/sec)** — 加速度计自然频率 `190` (默认) | real, double scalar

加速度计的自然频率，指定为 real, double scalar，单位为 radians per second。

#### 程序化使用

|  |
| --- |
| **模块参数**：`w_a` |
| **类型**：character vector |
| **值**：real, double scalar |
| **默认**：`'190'` |

#### 依赖关系

要启用此参数，请选择 **Second order dynamics for accelerometer**。

### **Accelerometer damping ratio** — 加速度计阻尼比 `0.707` (默认) | real, double scalar

加速度计的阻尼比，指定为 real, double scalar，无量纲。

#### 程序化使用

|  |
| --- |
| **模块参数**：`z_a` |
| **类型**：character vector |
| **值**：real, double scalar |
| **默认**：`'0.707'` |

#### 依赖关系

要启用此参数，请选择 **Second order dynamics for accelerometer**。

### **Accelerometer scale factor and cross-coupling** — 比例因子和交叉耦合 `[1 0 0; 0 1 0; 0 0 1]` (默认) | 3-by-3 matrix

比例因子和交叉耦合，指定为 3-by-3 matrix，用于使加速度计偏离体轴，并沿体轴缩放加速度。

#### 程序化使用

|  |
| --- |
| **模块参数**：`a_sf_cc` |
| **类型**：character vector |
| **值**：3-by-3 matrix |
| **默认**：`'[1 0 0; 0 1 0; 0 0 1]'` |

### **Accelerometer measurement bias** — 加速度计测量偏置 `[0 0 0]` (默认) | three-element vector

沿加速度计各轴的长期偏置，指定为三元素向量，单位采用所选加速度单位。

#### 程序化使用

|  |
| --- |
| **模块参数**：`a_bias` |
| **类型**：character vector |
| **值**：three-element vector |
| **默认**：`'[0 0 0]'` |

### **Accelerometer upper and lower limits** — 加速度的最小值和最大值 `[-inf -inf -inf inf inf inf]` (默认) | six-element vector

加速度计各轴上的三个最小加速度值和三个最大加速度值，指定为六元素向量，单位采用所选加速度单位。

#### 程序化使用

|  |
| --- |
| **模块参数**：`a_sat` |
| **类型**：character vector |
| **值**：six-element vector |
| **默认**：`'[-inf -inf -inf inf inf inf]'` |

#### 陀螺仪

### **Second-order dynamics for gyro** — 陀螺仪二阶动态特性 `on` (默认) | `off`

要将二阶动态特性应用于陀螺仪读数，请选中此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**：`dtype_g` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认**：`'on'` |

### **Gyro natural frequency (rad/sec)** — 陀螺仪自然频率 `190` (默认) | real, double scalar

陀螺仪的自然频率，指定为 real, double scalar，单位为 radians per second。

#### 程序化使用

|  |
| --- |
| **模块参数**：`w_g` |
| **类型**：character vector |
| **值**：real, double scalar |
| **默认**：`'190'` |

#### 依赖关系

要启用此参数，请选择 **Second-order dynamics for gyro**。

### **Gyro damping ratio** — 陀螺仪阻尼比 `0.707` (默认) | real, double scalar

陀螺仪的阻尼比，指定为 real, double scalar，无量纲。

#### 程序化使用

|  |
| --- |
| **模块参数**：`z_g` |
| **类型**：character vector |
| **值**：real, double scalar |
| **默认**：`'0.707'` |

#### 依赖关系

要启用此参数，请选择 **Second-order dynamics for gyro**。

### **Gyro scale factors and cross-coupling** — 陀螺仪比例因子和交叉耦合 `[1 0 0; 0 1 0; 0 0 1]` (默认) | 3-by-3 matrix

陀螺仪比例因子和交叉耦合，指定为 3-by-3 matrix，用于使陀螺仪偏离体轴，并沿体轴缩放角速率。

#### 程序化使用

|  |
| --- |
| **模块参数**：`g_sf_cc` |
| **类型**：character vector |
| **值**：3-by-3 matrix |
| **默认**：`'[1 0 0; 0 1 0; 0 0 1]'` |

### **Gyro measurement bias** — 陀螺仪测量偏置 `[0 0 0]` (默认) | three-element vector

沿陀螺仪各轴的长期偏置，指定为三元素向量，单位为 radians per second。

#### 程序化使用

|  |
| --- |
| **模块参数**：`g_bias` |
| **类型**：character vector |
| **值**：three-element vector |
| **默认**：`'[0 0 0]'` |

### **G-sensitive bias** — 速率最大变化 `[0 0 0]` (默认) | three-element vector

由线性加速度引起的速率最大变化，指定为三元素向量，单位为 radians per second per g-unit。

#### 程序化使用

|  |
| --- |
| **模块参数**：`g_sens` |
| **类型**：character vector |
| **值**：three-element vector |
| **默认**：`'[0 0 0]'` |

### **Gyro upper and lower limits** — 角速率的最小值和最大值 `[-inf -inf -inf inf inf inf]` (默认) | six-element vector

陀螺仪各轴上的三个最小角速率值和三个最大角速率值，指定为六元素向量，单位为 radians per second。

#### 程序化使用

|  |
| --- |
| **模块参数**：`g_sat` |
| **类型**：character vector |
| **值**：six-element vector |
| **默认**：`'[-inf -inf -inf inf inf inf]'` |

#### 噪声

### **Noise on** — 白噪声 `on` (默认) | `off`

要将白噪声应用于加速度和陀螺仪读数，请选中此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**：`a_rand` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认**：`'on'` |

### **Noise seeds** — 噪声种子 `[23093 23094 23095 23096 23097 23098]` (默认) | six-element vector

加速度计和陀螺仪各轴高斯噪声生成器的标量种子，指定为六元素向量。

#### 程序化使用

|  |
| --- |
| **模块参数**：`a_seeds` |
| **类型**：character vector |
| **值**：six-element vector |
| **默认**：`'[23093 23094 23095 23096 23097 23098]'` |

#### 依赖关系

要启用此参数，请选择 **Noise on**。

### **Noise power** — 噪声功率 `[0.001 0.001 0.001 0.0001 0.0001 0.0001]` (默认) | six-element vector

加速度计和陀螺仪各轴白噪声的功率谱密度 (PSD) 高度，指定为六元素向量，单位为：

- `Metric (MKS)` 时为 (m/s2)/Hz
- `English` 时为 (ft/s2)/Hz

#### 程序化使用

|  |
| --- |
| **模块参数**：`a_pow` |
| **类型**：character vector |
| **值**：six-element vector |
| **默认**：`'[0.001 0.001 0.001 0.0001 0.0001 0.0001]'` |

#### 依赖关系

要启用此参数，请选择 **Noise on**。

## 所属库

Vehicle Dynamics Blockset / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

实现三轴惯性测量单元 (IMU)

Three-Axis Inertial Measurement Unit 模块实现一个惯性测量单元 (IMU)，其中包含三轴加速度计和三轴陀螺仪。

有关方程和误差应用的说明，请参阅 Three-axis Accelerometer (Aerospace Blockset) 和 Three-axis Gyroscope (Aerospace Blockset)。
