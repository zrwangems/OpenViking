---
type: simulink-block
title: 'Piezo Stack'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Mechatronic Actuators\u200b'
documentation_page: 'piezostack'
documentation_source_path: 'ref/piezostack.html'
language: zh-CN
chinese_source: worker-translation
---

# Piezo Stack

## 端口

### 守恒

### **+** — 正极端子（电气）

与压电堆叠正极端子关联的电气守恒端口。

### **-** — 负极端子（电气）

与压电堆叠负极端子关联的电气守恒端口。

### **C** — 壳体（机械）

与壳体关联的机械平移守恒端口。

### **R** — 转子（机械）

与转子关联的机械平移守恒端口。

## 参数

### 静态力

### **Parameterization** — 静态力参数化 `Specify from a datasheet`（默认） | `Specify material properties`

选择以下静态力参数化方法之一：

- `Specify from a datasheet` — 提供数据手册参数，模块将其转换为静态力值。
- `Specify material properties` — 提供材料属性，模块将其转换为静态力值。

### **Stack area** — 堆叠横截面积 `100` `mm^2`（默认） | 正标量

堆叠的横截面积。

### **Stack length** — 堆叠长度 `36` `mm`（默认） | 正标量

无负载且未施加电势时的堆叠长度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet`。

### **No-load displacement at V0 volts** — 空载无约束位移 `0.038` `mm`（默认） | 正标量

施加 V0 volts 电压时堆叠的无约束位移。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet`。

### **Blocking force at V0 volts** — 阻挡力 `3800` `N`（默认） | 正标量

施加 V0 volts 电压且物理上阻止堆叠膨胀时，堆叠产生的力。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet`。

### **Test voltage V0** — 测试电压 `120` `V`（默认） | 正标量

用于确定空载位移和阻挡力的电压。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet`。

### **Capacitance** — 电容 `13` `uF`（默认） | 正标量

电容。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet`。

### **Piezo layer thickness** — 压电层厚度 `0.3` `mm`（默认） | 正标量

压电堆叠中每一层的厚度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify material properties`。

### **Number of layers** — 层数 `50`（默认） | 大于或等于 `1` 的标量

压电堆叠中的层数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify material properties`。

### **Piezoelectric charge constant** — 压电电荷常数 `500e-12` `m/V`（默认） | 正标量

每单位所施加电场产生的机械应变。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify material properties`。

### **Dielectric constant** — 介电常数 `2.1240e-08` `F/m`（默认） | 正标量

在恒定应力下测量的每单位电场的介电常数或介电位移。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify material properties`。

### **Elastic compliance** — 弹性柔量 `19e-12` `m^2/N`（默认） | 正标量

压电材料中每单位所施加应力产生的应变。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify material properties`。

### 动态力

### **Parameterization** — 动态力参数化 `Specify from a datasheet`（默认） | `Specify material properties`

选择以下动态力参数化方法之一：

- `Specify from a datasheet` — 提供数据手册参数，模块将其转换为动态力值。
- `Specify material properties` — 提供材料属性，模块将其转换为动态力值。

### **Resonant frequency at constant field** — 恒定场下的谐振频率 `inf` `kHz`（默认） | 正标量

当电气端口短路时，若受到机械扰动，执行器自然谐振的频率。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet`。

### **Mechanical quality factor** — 机械品质因数 `inf`（默认） | 正标量

影响 **R** 和 **C** 机械端口之间阻尼的因子。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet`。

### **Damping** — 平移阻尼 `0` `N/(m/s)`（默认） | 非负标量

平移阻尼项。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet`。

### **Effective mass** — 有效质量 `0` `g`（默认） | 非负标量

近似设备分布式动力学的质量，当连接到机械 R 端口时，使堆叠以正确频率谐振。该质量通常约为实际堆叠质量的三分之一。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify from a datasheet`。

## 所属库

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008b 中引入**

## 描述

压电堆叠执行器的电气和力特性

Piezo Stack 模块使用以下方程表示压电堆叠执行器的电气和力特性：

S=sE T+d' E

D=d T+εT E

其中

- *S* 是应变张量。
- *T* 是应力张量。
- *E* 是电场矢量。
- *D* 是电位移矢量。
- *sE* 是受恒定电场作用时的弹性柔量矩阵。
- *d* 是压电常数矩阵。
- *εT* 是在恒定应力下测量的介电常数。

**注意**

该模块对一维集总参数行为建模，因此 *S*、*T*、*E* 和 *D* 均为标量值。

您可以使用数据手册参数或材料属性来指定确定静态力的模块参数，具体取决于模块对话框的**静态力**选项卡上 **Parameterization** 参数的值。

模块对话框的**动态力**选项卡允许您包含可选的有效质量和机械阻尼效应。

- 如果您为 **Effective mass** 参数指定非零值，或为 **Resonant frequency at constant field** 参数指定有限值，则模块会将集总质量连接到机械 R 端口。当您指定有限的谐振频率时，模块会计算有效质量以实现正确的谐振频率。
- 如果您为 **Damping** 参数指定非零值，或为 **Mechanical quality factor** 参数指定有限值，则模块会在 **R** 到 **C** 机械端口之间添加阻尼项。当您指定机械品质因数 *Qm* 时，模块根据该参数值按 √(Mk)/Qm 计算阻尼，其中 *k* 是短路设备刚度，或等效为恒定场下的刚度。

在电气 **+** 到 **-** 端口之间施加正电压，会在机械 **C** 到 **R** 端口之间产生正向位移。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅为模块变量设置优先级和初始目标。

标称值提供了一种在模型中指定变量预期幅值的方法。基于标称值进行系统缩放可提高仿真的稳健性。您可以使用不同来源指定标称值，包括模块对话框或属性检查器中的**标称值**部分。有关详细信息，请参阅按标称值进行系统缩放。
