---
type: simulink-block
title: 'Absolute Reference (G)'
family: 'gas'
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

### **A** — 压力和温度均为零的气体

气体守恒端口，其中压力和温度均等于零。

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

### R2023a: 不再推荐使用 Absolute Reference (G) 模块

Pressure & Temperature Sensor (G) 模块现在包含一个隐式参考节点，这意味着您只需要一个端口即可对压力或温度进行绝对测量。仅当您需要测量模型中两个节点之间的压力或温度差时，才需要暴露第二个端口。

在以前的版本中，要测量端口 **A** 处的绝对压力和绝对温度，您需要将端口 **B** 连接到一个 Absolute Reference (G) 模块。现在不再需要这样做，因为您可以通过将 Pressure & Temperature Sensor (G) 模块的 **测量参考** 参数设置为 `Absolute` 来进行绝对测量。

此更改没有兼容性影响。现有模型中，如果 Absolute Reference (G) 模块连接到 Pressure & Temperature Sensor (G) 模块，则会像以前一样继续工作。

## 描述

（不推荐）绝对温度和压力为零的参考点

Absolute Reference (G) 模块表示气体网络中压力和温度的绝对参考。在端口 **A** 处，压力和温度均等于零。

与其他域不同，在其他域中，每个域内每个拓扑上不同的回路必须至少包含一个参考模块，而气体网络没有此要求。有关详细信息，请参阅参考节点和接地规则。

Absolute Reference (G) 模块的目的是为 Pressure & Temperature Sensor (G) 提供参考。要测量某个节点的绝对压力和绝对温度，请将该节点连接到 Pressure & Temperature Sensor (G) 模块的 **A** 端口。将 Pressure & Temperature Sensor (G) 模块的 **B** 端口连接到 Absolute Reference (G) 模块。

如果您在气体网络中的其他地方使用 Absolute Reference (G) 模块，则会触发仿真断言，因为气体压力和温度不能处于绝对零。
