---
type: simulink-block
title: 'Magnetic Rotor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical'
documentation_page: 'magneticrotor'
documentation_source_path: 'ref/magneticrotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Magnetic Rotor

## 端口

### 守恒

### **N** — 磁性定子连接 magnetic | array

与定子关联的磁性守恒端口。

该端口的值是一个磁性端口数组，其长度等于 **Number of stator teeth** 参数的值。

### **S** — 磁性转子连接 magnetic | array

与转子关联的磁性守恒端口。

该端口的值是一个磁性端口数组，其长度等于 **Number of stator teeth** 参数的值。

### **C** — 电机外壳 mechanical

与电机外壳关联的机械旋转守恒端口。

### **R** — 电机转子 mechanical

与电机转子关联的机械旋转守恒端口。

## 参数

### 主要

### **Number of rotor pole pairs** — 转子极对数 `5`（默认）| 正标量

转子的极对数。该参数必须大于或等于 `1`，且小于 **Number of stator teeth** 参数的值。

### **Number of stator teeth** — 定子齿数 `9`（默认）| 正标量

定子的齿数。该参数必须大于或等于 `2`。

### **Peak magnet flux density** — 磁转子峰值磁通密度 `0.4` `T`（默认）| 正标量

与永磁转子关联的峰值磁通密度。磁通密度随转子角度呈正弦变化。

### **Permanent magnet length (in direction of flux)** — 沿电机径向的磁体长度 `5` `mm`（默认）| 正标量

磁体沿电机径向的长度，或者等效地，沿磁通方向的长度。该参数必须小于 **Rotor radius** 参数的值。

### **Permanent magnet relative permeability** — 永磁体相对磁导率 `1.05`（默认）| 标量

永磁体的相对磁导率。通常，您将该参数设置为略大于 `1` 的值，以反映永磁体中磁偶极子已经对齐。

### **Air gap** — 径向气隙 `1` `mm`（默认）| 正标量

径向气隙的长度。

### **Rotor radius** — 转子半径 `65` `mm`（默认）| 正标量

转子的半径。

### **Tooth depth (in direction of shaft)** — 定子齿深度 `50` `mm`（默认）| 正标量

定子齿沿旋转轴方向的长度。

### 故障

### **Rotor poles fault** — 用于使转子极发生故障的选项 `Add fault`（默认）

用于向转子极添加故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Flux multipliers for faulted rotor poles** — 用于降低转子极磁通的乘数 `ones(1,10)`（默认）| 向量

当转子极发生故障时，用于降低转子极磁密度的乘数。该参数的值必须是一个向量，其长度等于 **Number of rotor pole pairs** 参数值的两倍。向量的每个元素对应一个转子极。

默认值 `ones(1,10)` 产生的行为与无故障场景相同。

#### 依赖关系

要启用该参数，请通过点击 **Rotor poles fault** 参数中的 **Add fault** 超链接，向 Magnetic Rotor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开带有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Duration of transition to faulted** — 模块完全进入故障状态的持续时间 `100` `s`（默认）| 正标量

模块在该持续时间之后对每个转子极的峰值磁体磁通密度施加故障乘数的完整影响。当模块进入故障状态时，软件使用故障乘数逐渐修改每个转子极的峰值磁通密度。

#### 依赖关系

要启用该参数，请通过点击 **Rotor poles fault** 参数中的 **Add fault** 超链接，向 Magnetic Rotor 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开带有故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用该参数，请将 **Trigger Type** 设置为 `Timed`。

## 所属库

Simscape / Electrical / Electromechanical

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

定子齿与旋转永磁转子之间的气隙

Magnetic Rotor 模块表示永磁同步电机（PMSM）中转子组件的磁特性和机械特性。具体而言，该模块将定子齿与旋转永磁转子之间的气隙建模为 Rotating Air Gap 模块数组。

**Number of stator teeth** 参数指定组成 Magnetic Rotor 模块的 Rotating Air Gap 模块数量。下图显示了当您将 **Number of stator teeth** 参数设置为 `9` 时该模块的等效电路：

如果转子角度为零，则其中一个转子磁体与第一个定子齿的中部完全对齐。该永磁体的方向与从端口 **N** 到端口 **S** 的磁通流动方向相反。

磁性端口 **N** 是一个磁性端口数组，其长度等于 **Number of stator teeth** 参数的值。要连接与每个定子齿对应的各个磁性端口，您需要一个 Magnetic Demux 模块。您可以使用 Simscape 代码编写自己的 Magnetic Demux 模块，或使用 Faulted PMSM 示例模型中的模块。

下图显示了 Magnetic Rotor 模块的参数与其在永磁电机内部物理值之间的关系。

- *r* 是 **Rotor radius** 参数的值。
- *g* 是 **Air gap** 参数的值。
- *lm* 是 **Permanent magnet length (in direction of flux)** 参数的值。
- *l* 是 **Tooth depth (in direction of shaft)** 参数的值。

转子周长等于 2πr。那么，转子上一个永磁体的宽度等于 2πr2N，其中 *N* 是 **Number of rotor pole pairs**。

### 故障

要对 Magnetic Rotor 模块中的故障建模，请在 **Faults** 部分中，点击您要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

Magnetic Rotor 模块支持使转子极发生故障。该故障行为对应于转子中一个或多个磁体（极）具有减弱的磁场。您可以通过指定 **Flux multipliers for faulted rotor poles** 参数，对任意转子极的磁通密度施加降低因子。

向故障值的过渡会在 **Duration of transition to faulted** 参数中指定的时间段内线性插值。使用该参数来模拟过热永磁体如何随时间逐渐失去其磁化强度。
