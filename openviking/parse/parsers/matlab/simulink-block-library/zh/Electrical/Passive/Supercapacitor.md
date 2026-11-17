---
type: simulink-block
title: 'Supercapacitor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'supercapacitor'
documentation_source_path: 'ref/supercapacitor.html'
language: zh-CN
chinese_source: worker-translation
---

# Supercapacitor

## 端口

### 守恒

### **+** — 正电气端子 electrical

与正端子关联的电气守恒端口。

### **-** — 负电气端子 electrical

与负端子关联的电气守恒端口。

## 参数

#### 电池特性

### **Fixed resistances, [R1 R2 R3]** — 每个支路的固定电阻值 `[0.2, 90.0, 1000.0]` `Ohm`（默认值）

将超级电容器各个支路中固定电阻器的电阻值指定为一个数组。

### **Fixed capacitances, [C1 C2 C3]** — 每个支路的固定电容值 `[2.5, 1.5, 4.0]` `F`（默认值）

将超级电容器中固定电容器的各个电容值指定为一个数组。

### **Voltage-dependent capacitor gain** — 第一个支路的可变电容系数 `0.95` `F/V`（默认值）

指定超级电容器第一个支路中电压相关电容器的可变电容系数 *Kv*。有关确定可变电容系数的信息，请参阅 [1]。

### **Self-discharge resistance** — 自放电电阻 `inf`（默认值）

指定连接在两个端子之间的超级电容器的自放电电阻。

#### 配置

### **Number of series cells** — 串联的超级电容器电池数 `1`（默认值）

指定超级电容器中串联配置的电池数。

### **Number of parallel cells** — 并联的超级电容器电池数 `1`（默认值）

指定超级电容器中并联配置的电池数。

#### 变量

### **Beginning Value** — 初始目标值 `0`（默认值）

使用 **Variables** 选项卡在仿真前设置模块变量的优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

电化学双层电容器

Supercapacitor 模块表示电化学双层电容器（ELDC），通常称为超级电容器或超电容器。超级电容器的电容值比普通电容器的电容值大几个数量级。超级电容器可以提供能量脉冲，因为它们可以快速充电和放电。

您可以使用单个 Supercapacitor 模块对任意数量的串联或并联超级电容器电池进行建模。为此，请将相关参数，即 **Number of series cells** 或 **Number of parallel cells**，设置为大于 `1` 的值。在内部，该模块仅对单个超级电容器电池的方程进行仿真，但它会计算：

- 根据串联电池数计算输出电压
- 根据并联电池数计算电流

基于单个电池的输出计算多电池超级电容器的输出，比单独仿真每个电池的方程更高效。

该图显示了 Supercapacitor 模块中单个电池的等效电路。该电路是一个电阻器和电容器网络，通常用于对超级电容器行为进行建模。

电容器 *C1*、*C2* 和 *C3* 具有固定电容。电容器 *Cv* 的电容取决于其两端的电压。电阻器 *R1*、*R2* 和 *R3* 具有固定电阻。Supercapacitor 模块中每个单独固定电容器两端的电压计算如下

Vcn=vNseries−inRn,

其中：

- *v* 是模块两端的电压。
- *Nseries* 是串联的电池数。
- *n* 是支路编号。*n* = [1, 2, 3]。
- *in* 是通过第 *n* 个支路的电流。
- *Rn* 是第 *n* 个支路中的电阻。
- *Vcn* 是第 *n* 个支路中电容器两端的电压。

通过超级电容器第一个支路的电流方程取决于该支路中电容器两端的电压。如果电容器承受正电压，即

Vc1>0,

则

i1=(C1+KvVc1)dVc1dt,

否则

i1=C1dVc1dt,

其中：

- *Vc1* 是第一个支路中电容器两端的电压。
- *C1* 是第一个支路中固定电容器的电容。
- *Kv* 是电压相关电容增益。
- *i1* 是通过第一个支路的电流。

对于其余支路，电流定义为

in=CndVcndt,

其中：

- *n* 是支路编号。*n* =[2, 3]。
- *Cn* 是第 *n* 个支路的电容。

通过 Supercapacitor 模块的总电流为

i=Nparallel(i1+i2+i3+vRdischarge),

其中：

- *Nparallel* 是并联的电池数。
- *Rdischarge* 是超级电容器的自放电电阻。
- *i* 是通过超级电容器的电流。
