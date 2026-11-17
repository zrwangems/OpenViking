---
type: simulink-block
title: 'Op-Amp'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'opamp'
documentation_source_path: 'ref/opamp.html'
language: zh-CN
chinese_source: worker-translation
---

# Op-Amp

## 端口
```yaml
ports:
- name: +
  summary: 正端子电气端口
  direction: conserving
- name: '-'
  summary: 负端子电气端口
  direction: conserving
- name: out
  summary: 输出端子电气端口
  direction: conserving
```

### 守恒端口

### **+** — 正端子电气端口

与运放正端子关联的电气守恒端口。

### **-** — 负端子电气端口

与运放负端子关联的电气守恒端口。

### **out** — 输出端子电气端口

与运放输出节点关联的电气守恒端口。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中看到此名称。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

理想运算放大器

Op-Amp 模块对理想运算放大器（运放）进行建模。图中显示了实现原理图。

Op-Amp 模块的实现原理图

模块实现基于以下假设：

- 假设理想运放增益 *A* 为无穷大
- 因此，对于有限输出，必须有 *V1* = 0
- 理想运放还意味着从 p 到 n 的电流为零（*i1* = 0）

这些假设得出模块的以下方程：

```
equations
    v1 == p.v - n.v;
    v1 == 0;
    i1 == 0;
end
```

有关更多信息，请点击模块对话框的**描述**选项卡中的**源代码**链接。

该模块没有参数。但是，您可以在仿真前初始化 **Current into output node** 变量。有关更多信息，请参阅 Block-Level Variable Initialization。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的**标称值**部分。有关更多信息，请参阅 Modify Nominal Values for a Block Variable。
