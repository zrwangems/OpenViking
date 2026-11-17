---
type: simulink-block
title: 'Absolute Reference (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'absolutereferenceg'
documentation_source_path: 'ref/absolutereferenceg.html'
language: zh-CN
chinese_source: worker-translation
---

# Absolute Reference (G)

## 端口

### 守恒

### **A** — 压力和温度为零的气体

气体守恒端口，其压力和温度均等于零。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2023a: Absolute Reference (G) 模块不再推荐使用

Pressure & Temperature Sensor (G) 模块现在包含一个隐式参考节点，这意味着你只需要一个端口即可进行压力或温度的绝对测量。仅当你需要测量模型中两个节点之间的压力或温度差时，才需要暴露第二个端口。

在以前的版本中，要测量端口 **A** 处的绝对压力和绝对温度，你需要将端口 **B** 连接到 Absolute Reference (G) 模块。这不再必要，因为你现在可以通过将 Pressure & Temperature Sensor (G) 模块的 **Measurement reference** 参数设置为 `Absolute` 来进行绝对测量。

此更改没有兼容性影响。现有模型中若已将 Absolute Reference (G) 模块连接到 Pressure & Temperature Sensor (G) 模块，将继续像以前一样工作。

## 描述

（不推荐）绝对温度为零和压力为零的参考点

Absolute Reference (G) 模块表示气体网络中压力和温度的绝对参考。在端口 **A** 处，压力和温度均等于零。

与其他域不同——在其他域中，域内每个拓扑上不同的回路必须至少包含一个参考模块——气体网络没有此要求。有关详细信息，请参阅 Reference Node and Grounding Rules。

Absolute Reference (G) 模块的目的是为 Pressure & Temperature Sensor (G) 提供参考。要测量某个节点的绝对压力和绝对温度，请将该节点连接到 Pressure & Temperature Sensor (G) 模块的 **A** 端口。将 Pressure & Temperature Sensor (G) 模块的 **B** 端口连接到 Absolute Reference (G) 模块。

如果你在气体网络的其他位置使用 Absolute Reference (G) 模块，它会触发仿真断言，因为气体压力和温度不可能处于绝对零度。
