---
type: simulink-block
title: 'Controller LCFB1'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Turbine-Governors\u200b'
documentation_page: 'controllerlcfb1'
documentation_source_path: 'ref/controllerlcfb1.html'
language: zh-CN
chinese_source: worker-translation
---

# Controller LCFB1

## 端口

### 输入

### **speed\_pu** — 速度负载标量

速度负载，指定为标量。

**数据类型：** `single` | `double`

### **Pmwset** — 功率设定值标量

功率设定值，指定为标量。

**数据类型：** `single` | `double`

### **Pelec** — 电功率输入标量

电功率输入，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **Pref** — 偏置标量

要应用于涡轮机-调速器速度负载参考值的偏置，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### **速度参考值 (pu)** — 速度参考值 `1`（默认）| 标量

标幺值速度参考值。

### **初始功率参考值, P\_ref0 (pu)** — 初始功率参考值 `0.45`（默认）| 标量

仿真开始时的标幺值功率参考值。

### **控制器死区 (pu)** — 控制器死区 `0`（默认）| 标量

控制器的标幺值死区。

### **最大误差, e\_max (pu)** — 最大误差 `0.1`（默认）| 标量

最大可能误差。

### **频率偏差增益, f\_b (pu)** — 频率偏差的增益 `0`（默认）| 标量

频率偏差的标幺值增益。

### **比例增益, K\_p (pu)** — PI 控制的比例增益 `0`（默认）| 标量

PI 控制的标幺值比例增益。

### **积分增益, K\_i (pu/s)** — PI 控制的积分增益 `0.1`（默认）| 标量

PI 控制的标幺值积分增益。

### **功率变送器时间常数, T\_pelec (s)** — 功率变送器的时间常数 `3.5`（默认）| 标量

功率变送器的时间常数，以秒为单位。功率变送器由图中标记为 "Low-Pass Filter" 的模块表示。

### **最大输出, I\_rmax (pu)** — 输出上限 `0.035`（默认）| 标量

输出的标幺值上限饱和限值。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / Turbine-Governors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2020a 中引入**

## 描述

用于涡轮机-调速器模型的负载控制器

Controller LCFB1 模块对 LCFB1 涡轮负载控制器模型进行建模。您可以将此负载控制器与任何涡轮机-调速器模型配合使用，例如 Governor Type 1 或 Governor Type 3 模块。

您可以使用 **采样时间（-1 表示继承）** 参数在模块的连续实现和离散实现之间切换。要将控制器配置为连续时间，请将 **采样时间（-1 表示继承）** 属性设置为 `0`。要将控制器配置为离散时间，请将 **采样时间（-1 表示继承）** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

下图说明了模块的整体结构：
