---
type: simulink-block
title: 'Thermocouple'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sensors and Transducers / Encoders and Transducers'
documentation_page: 'thermocouple'
documentation_source_path: 'ref/thermocouple.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermocouple

## 端口

### 守恒

### **A** — 热端口 thermal

热电偶热端口。

### **+** — 正端口 electrical

与热电偶正端口关联的电气守恒端口。

### **-** — 负端口 electrical

与热电偶负端口关联的电气守恒端口。

## 参数

### 电气

### **Thermocouple type** — 热电偶类型 `Type B, E, J, K (t<=0 degC), N, R, S or T` （默认） | `Type K (t>=0 degC)`

选择其中一个建模选项：

- `Type B, E, J, K (t<=0 degC), N, R, S or T` — 此选项等效于早期版本中的模块功能。
- `Type K (t>=0 degC)` — 当温差大于 0 摄氏度时，此选项会向模块方程添加指数项。

### **Coefficients [c0 c1 ... cn]** — 系数 [c0 c1 ... cn] `[0, 0, 0, 0, 0, 0, 0, 0, 0]` （默认）

描述电压随温度变化的方程中的系数 *c* 向量。该向量的最大长度为 15 个元素。

**注意**

您可以从 NIST 数据库 [1] 下载标准热电偶类型的参数。有关如何执行此操作的信息，请参阅 Simulink®Approximating Nonlinear Relationships: Type S Thermocouple 示例。

### **Coefficients [a0 a1 a2]** — 系数 [a0 a1 a2] `[0, 0, 0]` （默认）

附加系数 *a*0、*a*1 和 *a*2 的向量，仅 Type K 热电偶需要。

#### 依赖关系

仅当您为 **Thermocouple model** 参数选择 `Type K (t>=0 degC)` 时，此参数才可见。

### 热

### **Reference temperature** — 参考温度 `0` `degC` （默认）

模块在计算器件两端电压时从热端口温度中减去的温度。

### **Thermal time constant** — 热时间常数 `1` `s` （默认）

当环境温度发生阶跃变化时，热电偶温度达到最终温度变化的 63% 所需的时间。

### **Dissipation factor** — 耗散系数 `1e-3` `W/K` （默认）

使热电偶温度升高 1 K 所需的热功率。

### **Initial temperature** — 初始温度 `25` `degC` （默认）

仿真开始时热电偶的温度。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

将热势差转换为电势差的传感器

Thermocouple 模块使用 NIST ITS-90 Thermocouple Database [1] 中定义的标准多项式参数化来表示热电偶。

对于 Type B, E, J, K (t<=0 degC), N, R, S 或 T 热电偶，器件两端的电压 *E*（以 mV 为单位）为

E(mV)=c0+c1t+...+cntn

其中：

- *ci* 是 **Coefficients [c0 c1 ... cn]** 参数值的第 *i* 个元素。
- *t* 是热端口 A 处的温度与 **Reference temperature** 参数值之间的摄氏温差。

**注意**

器件两端电压作为温差的函数的方程以 mV 为单位定义。实际器件两端电压的单位为 V。

对于 Type K (t>=0 degC) 热电偶，方程包含一个附加指数项：

E(mV)=c0+c1t+...+cntn+a0ea1(t−a2)2

其中 *a*0、*a*1 和 *a*2 是附加系数，仅 Type K 热电偶需要，由 **Coefficients [a0 a1 a2]** 参数值定义。

以下方程描述模块的热行为：

Q=KdtcdTdt

其中：

- *T* 是端口 A 处的温度。
- *Q* 是流入端口 A 的净热流。
- *K*d 是 **Dissipation factor** 参数值。
- *t*c 是 **Thermal time constant** 参数值。
- *dT/dt* 是温度变化率。

要在自由空间中建模热电偶：

1. 将热电偶连接到 Simscape™ Convective Heat Transfer 模块的 B 端口。
2. 将 Convective Heat Transfer 模块的 A 端口连接到 Simscape Ideal Temperature Source 模块，该模块的温度设置为环境温度。
3. 将 Convective Heat Transfer 模块的 **Area** 参数设置为近似面积 *A*nom。
4. 将 Convective Heat Transfer 模块的 **Heat transfer coefficient** 参数设置为 *K*d/*A*nom。
