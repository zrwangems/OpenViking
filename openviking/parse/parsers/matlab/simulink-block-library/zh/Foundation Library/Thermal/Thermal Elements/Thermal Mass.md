---
type: simulink-block
title: 'Thermal Mass'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Elements'
documentation_page: 'thermalmass'
documentation_source_path: 'ref/thermalmass.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermal Mass

## 端口

### 输入

### **Mdot** — 质量控制信号，kg/s 物理信号

输入物理信号，用于指定热质量的变化。使用高优先级 **Mass** 变量指定初始热质量值。

#### 依赖关系

要启用此端口，请将 **Mass type** 参数设置为 `Variable`。

### **Tin** — 进入质量流的温度，K 物理信号

输入物理信号，用于指定进入质量流的温度。当端口 **Mdot** 处的信号小于或等于 0 时，端口 **Tin** 处的信号值无效。

#### 依赖关系

要启用此端口，请将 **Mass type** 参数设置为 `Variable`。
### 守恒

### **M** — 将质量连接到回路热网络的端口

热守恒端口，用于将质量连接到物理网络。

端口名称在模块图标中不可见，但您可以通过点击模块对话框 **Description** 选项卡中的 **Source code** 链接，在底层源文件中查看此名称。

### **N** — 第二个图形化热端口

第二个热守恒端口，允许您将质量与框图的其他元件串联连接。此端口与端口 **M** 具有相同的温度，因此单端口和双端口模块表示之间的区别纯粹是图形上的。

端口名称在模块图标中不可见，但您可以通过点击模块对话框 **Description** 选项卡中的 **Source code** 链接，在底层源文件中查看此名称。

#### 依赖关系

要启用此端口，请将 **Number of graphical ports** 参数设置为 `2`。

## 参数

### **Mass type** — 指定热质量是否可以在仿真期间变化 `Constant`（默认）| `Variable`

选择热质量是否可以在仿真期间变化：

- `Constant` — 热质量在仿真期间保持恒定。
- `Variable` — 热质量可以在仿真期间变化。使用此选项对质量发生变化但几何效应可忽略的系统进行建模，例如洗衣机在每个循环中注入、加热然后排空不同量的液体。

### **Mass** — 恒定质量 `1 kg`（默认）| 正标量

质量值。质量在仿真期间保持恒定。

#### 依赖关系

要启用此参数，请将 **Mass type** 参数设置为 `Constant`。

### **Specific heat** — 材料的比热容 `447 J/(K*kg)`（默认）| 正标量

材料的比热容。

### **Minimum mass** — 最小可接受质量 `1e-6 kg`（默认）| 正标量

最小热质量值。如果热质量在仿真期间低于此值，模块将报错。

#### 依赖关系

要启用此参数，请将 **Mass type** 参数设置为 `Variable`。

### **Number of graphical ports** — 可见端口数量 `1`（默认）| `2`

如何将模块连接到回路的其余部分：

- `1` — 模块有一个守恒端口，将其连接到热回路。当模块只有一个端口时，将其连接到其他两个模块之间的连接线上。
- `2` — 选择此选项会暴露第二个端口，允许您将模块与回路中的其他模块串联连接。由于两个端口具有相同的温度，模块的功能与只有一个端口时相同。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

### R2023a：使用可变热质量

该模块包含 **Mass type** 参数，允许您指定热质量在仿真期间保持恒定还是变化。在之前的版本中，热质量只能是恒定的。

## 描述

热系统中的质量

Thermal Mass 模块表示一个热质量，反映材料或材料组合存储内能的能力。材料的质量及其比热容表征了这一属性。热质量由下式描述

Q=c⋅mdTdt，

其中：

- *Q* 是热流量。
- *c* 是质量材料的比热容。
- *m* 是质量。
- *T* 是温度。
- *t* 是时间。

**Mass type** 参数允许您指定热质量在仿真期间保持恒定还是变化：

- `Constant` — 热质量在仿真期间恒定。
- `Variable` — 热质量可以在仿真期间变化。如果选择此选项，模块对话框中的 **Mass** 参数将被 **Minimum mass** 参数和高优先级 **Mass** 变量替换，并且模块具有两个物理信号输入端口：**Mdot**，指定热质量的变化；**Tin**，指定流入质量流的温度。当热质量恒定或减少时，端口 **Tin** 处的信号值无效。

使用 `Variable` 选项来建模质量发生变化但几何效应可忽略的系统，例如洗衣机在每个循环中注入、加热，然后排空不同量的液体。

默认情况下，模块具有一个热守恒端口。由于模块正方向是从端口指向模块，因此如果热量流入模块，则热流量为正。

在某些应用中，习惯上在框图布局中将质量与其他元件串联显示。为支持此用例，**Number of graphical ports** 参数允许您在模块图标的对侧显示第二个端口。双端口变体纯粹是图形性的：两个端口具有相同的温度，因此无论模块有一个还是两个端口，其功能都相同。模块图标根据 **Mass type** 和 **Number of graphical ports** 参数的值而变化。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。

如果将 **Mass type** 参数设置为 `Variable`，请使用高优先级 **Mass** 变量来指定初始热质量值。
