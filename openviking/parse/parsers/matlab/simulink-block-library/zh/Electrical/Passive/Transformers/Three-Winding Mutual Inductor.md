---
type: simulink-block
title: 'Three-Winding Mutual Inductor'
family: 'passive'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'threewindingmutualinductor'
documentation_source_path: 'ref/threewindingmutualinductor.html'
language: zh-CN
chinese_source: worker-translation
---

# Three-Winding Mutual Inductor

## 端口

### 守恒

### **1+** — 第一个电感器正电压电气

与第一个互感电感器的正电压相关联的电气守恒端口。

### **1-** — 第一个电感器负电压电气

与第一个互感电感器的负电压相关联的电气守恒端口。

### **2+** — 第二个电感器正电压电气

与第二个互感电感器的正电压相关联的电气守恒端口。

### **2-** — 第二个电感器负电压电气

与第二个互感电感器的负电压相关联的电气守恒端口。

### **3+** — 第三个电感器正电压电气

与第三个互感电感器的正电压相关联的电气守恒端口。

### **3-** — 第三个电感器负电压电气

与第三个互感电感器的负电压相关联的电气守恒端口。

## 参数

### **Inductance L1** — 第一个绕组自感 `0.001` `H`（默认）| 正标量

第一个绕组的自感。

### **Inductance L2** — 第二个绕组自感 `0.001` `H`（默认）| 正标量

第二个绕组的自感。

### **Inductance L3** — 第三个绕组自感 `0.001` `H`（默认）| 正标量

第三个绕组的自感。

### **Perfect coupling - no leakage** — 启用完美耦合的选项 `Off`（默认）| `On`

*自 R2025a 起*

启用无漏感和无快速极点的完美耦合的选项。如果选择此参数，模块会将耦合系数设为 1，同时保留正确的低频行为并阻断 DC。

### **Coefficient of coupling, K12** — 第一个和第二个绕组之间的耦合系数 `0.9`（默认）| 范围 [-1,1] 内的标量

定义第一个和第二个绕组之间互感的耦合系数。负值会产生反相输出。不要使用非常接近 1 的幅值（例如 0.9999），因为这些值可能引入快速仿真动态。要启用完美耦合，请改为选择 **Perfect coupling - no leakage** 参数。

#### 依赖关系

要启用此参数，请清除 **Perfect coupling - no leakage** 参数。

### **Coefficient of coupling, K13** — 第一个和第三个绕组之间的耦合系数 `0.9`（默认）| 范围 [-1,1] 内的标量

定义第一个和第三个绕组之间互感的耦合系数。负值会产生反相输出。不要使用非常接近 1 的幅值（例如 0.9999），因为这些值可能引入快速仿真动态。要启用完美耦合，请改为选择 **Perfect coupling - no leakage** 参数。

#### 依赖关系

要启用此参数，请清除 **Perfect coupling - no leakage** 参数。

### **Coefficient of coupling, K23** — 第二个和第三个绕组之间的耦合系数 `0.9`（默认）| 范围 [-1,1] 内的标量

定义第二个和第三个绕组之间互感的耦合系数。负值会产生反相输出。不要使用非常接近 1 的幅值（例如 0.9999），因为这些值可能引入快速仿真动态。要启用完美耦合，请改为选择 **Perfect coupling - no leakage** 参数。

#### 依赖关系

要启用此参数，请清除 **Perfect coupling - no leakage** 参数。

## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2025a：对无快速极点的理想三绕组互感电感器建模

现在，您可以对无漏感和无快速极点的理想三绕组互感电感器建模。要将耦合系数设为 1，同时保留正确的低频行为并阻断 DC，请选择 **Perfect coupling - no leakage** 参数。

## 描述

三个耦合电感器

Three-Winding Mutual Inductor 模块表示一组三个耦合电感或绕组。三个绕组两端的电压为

V1=L1dI1dt+M12dI2dt+M13dI3dtV2=M12dI1dt+L2dI2dt+M23dI3dtV3=M13dI1dt+M23dI2dt+L3dI3dt

其中：

- *Vi* 是第 *i* 个绕组两端的电压。
- *Ii* 是流过第 *i* 个绕组的电流。
- *Li* 是第 *i* 个绕组的自感。
- *Mij* 是第 *i* 个和第 *j* 个绕组之间的互感，Mij=KijLiLj。

在这些方程中，当电流流入各自电感器端子的正节点时，电流为正。

要将耦合系数设为 1，同时保留正确的低频行为并阻断 DC，请选择 **Perfect coupling - no leakage** 参数 *（自 R2025a 起）*。

Simscape™ 和 Simscape Electrical™ 库包含若干可对同一类型变压器设备建模的模块。但是，这些模块作出不同的建模假设。要为您的应用选择正确的模块，您必须理解这些假设如何影响模块作为频率的函数的行为。有关详细信息，请参阅选择用于变压器建模的模块。

当您运行包含此模块的仿真时，软件会检查指定的参数值，以确保所得设备是无源的。如果不是，软件会发出错误。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅按标称值进行系统缩放。
