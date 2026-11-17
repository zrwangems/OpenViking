---
type: simulink-block
title: 'Absolute Reference (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'absolutereferencetl'
documentation_source_path: 'ref/absolutereferencetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Absolute Reference (TL)

## 端口

### 守恒端口

### **A** — 压力和温度均为零的热液体

热液体守恒端口，其压力和温度均等于零。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2023a：不再推荐使用 Absolute Reference (TL) 模块

Pressure & Temperature Sensor (TL) 模块现在包含一个隐式参考节点，这意味着您只需要一个端口即可进行压力或温度的绝对测量。仅当您需要测量模型中两个节点之间的压力或温度差时，才需要暴露第二个端口。

在之前的版本中，要测量端口 **A** 处的绝对压力和绝对温度，您需要将端口 **B** 连接到 Absolute Reference (TL) 模块。现在不再需要这样做，因为您可以通过将 Pressure & Temperature Sensor (TL) 模块的 **Measurement reference** 参数设置为 `Absolute` 来进行绝对测量。

此更改没有兼容性影响。现有模型中若将 Absolute Reference (TL) 模块连接到 Pressure & Temperature Sensor (TL) 模块，其工作方式与之前相同。

## 描述

（不推荐）绝对温度为零且压力为零的参考点

Absolute Reference (TL) 模块表示热液体系统中压力和温度的绝对参考。在端口 **A** 处，压力和温度均等于零。
