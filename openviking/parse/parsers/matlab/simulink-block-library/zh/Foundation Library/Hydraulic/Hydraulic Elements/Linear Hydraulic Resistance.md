---
type: simulink-block
title: 'Linear Hydraulic Resistance'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'linearhydraulicresistance'
documentation_source_path: 'ref/linearhydraulicresistance.html'
language: zh-CN
chinese_source: worker-translation
---

# Linear Hydraulic Resistance

## 端口
```yaml
ports: []
```

该模块具有以下端口：

`A`
:   与阻力入口关联的液压守恒端口。

`B`
:   与阻力出口关联的液压守恒端口。
## 参数
```yaml
parameters: []
```

**Resistance**
:   线性阻力系数。默认值为 `10e9`
    Pa/(m^3/s)。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2023a: 将被移除

Hydraulic 库将在未来版本中移除。请改用 Isothermal Liquid 库。
Isothermal Liquid 库中的模块提供更高的精度、可用性和
数值性能。

有关更新模型的详细信息，请参阅 Upgrading Hydraulic Models to Use Isothermal Liquid Blocks。

## 描述

（将被移除）具有线性阻力损失的液压管道

Linear Hydraulic Resistance 模块表示一种液压阻力，其中
压力损失与流量成正比。该模块在开发的初步
阶段可能很有用，或者作为一种加速仿真的强大手段，特别是在流量
相对于工作点变化不大的情况下。

连接 A 和 B 是分别与模块入口和
出口关联的守恒液压端口。

模块正方向为从端口 A 到端口 B。这意味着如果流体从 A 流向 B，则流量为
正值，压力损失确定为 p=pA−pB。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用
模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。
使用基于标称值的系统缩放可提高仿真鲁棒性。标称
值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal
Values** 部分。有关更多
信息，请参阅 Modify Nominal Values for a Block Variable。
