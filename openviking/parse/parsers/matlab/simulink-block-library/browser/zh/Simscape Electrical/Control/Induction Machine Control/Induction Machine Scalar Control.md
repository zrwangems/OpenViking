---
type: simulink-block
title: 'Induction Machine Scalar Control'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinescalarcontrol'
documentation_source_path: 'ref/inductionmachinescalarcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Machine Scalar Control

## 端口

### 输入

### **fRef** — 频率标量

参考电频率。

**示例：** 示例

**数据类型：** `single` | `double`
### 输出

### **Vabc** — 电压矢量

参考相电压。

**示例：** 示例

**数据类型：** `single` | `double`

## 参数

### **额定电频率 (Hz)** — 频率 `60` (默认) | 正标量

标称频率。

### **额定电压 (V)** — 电压 `550` (默认) | 正数且大于 **最小电压 (V)** 参数的值

标称电压。

### **最小电压 (V)** — 电压 `10` (默认) | 零或正数

电压的下界。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1` (默认) | 正标量

连续模块执行之间的时间，以 s 为单位。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅“什么是采样时间？”和“指定采样时间”。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

## 所属库

Simscape / Electrical / Control / Induction Machine Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

感应电机 V/f 控制

Induction Machine Scalar Control 模块实现感应电机标量（即 V/f 或 V/Hz）控制结构。该图显示了该模块实现的开环 V/f 控制结构。

### 方程

Induction Machine Scalar Control 模块基于参考频率 fs\* 按如下公式计算定子电压的幅值：

Vs\*=(Vn−Vminfn−fmin)fs\*,

其中：

- *Vn* 为额定电压。
- *Vmin* 为最小电压。
- *fn* 为额定电频率。
- *fmin* 为最小频率。

静止参考坐标系中的电压分量为：

Vα=Vs\*cos(2πfs\*t)

以及

Vβ=Vs\*sin(2πfs\*t).

该模块通过逆 Clarke 变换从 *Vα* 和 *Vβ* 获得 *Vabc*。
