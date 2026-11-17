---
type: simulink-block
title: 'Absolute Reference (MA)'
family: 'moist-air'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'absolutereferencema'
documentation_source_path: 'ref/absolutereferencema.html'
language: zh-CN
chinese_source: worker-translation
---

# Absolute Reference (MA)

## 端口

### 守恒

### **A** — 压力、温度、比湿和痕量气体质量分数为零的湿空气

湿空气守恒端口，其中压力和温度等于绝对零，并且比湿和痕量气体质量分数等于零。

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2023a：不再推荐 Absolute Reference (MA) 模块

Pressure & Temperature Sensor (MA) 模块现在包含一个隐式参考节点，这意味着您只需要一个端口即可进行压力或温度的绝对测量。仅当需要测量模型中两个节点之间的压力或温度差时，才暴露第二个端口。

在以前的版本中，要测量端口 **A** 处的绝对压力和绝对温度，您需要将端口 **B** 连接到 Absolute Reference (MA) 模块。现在不再需要这样，因为您现在可以通过将 Pressure & Temperature Sensor (MA) 模块的 **Measurement reference** 参数设置为 `Absolute` 来进行绝对测量。

此更改没有兼容性影响。现有模型中，如果 Absolute Reference (MA) 模块连接到 Pressure & Temperature Sensor (MA) 模块，将继续像以前一样工作。

## 描述

（不推荐）绝对温度和压力为零的参考点

Absolute Reference (MA) 模块表示湿空气网络中的压力和温度的绝对参考。在端口 **A** 处，压力和温度等于绝对零。比湿和痕量气体质量分数也等于零。

与其他域不同，在其他域中，域内每个拓扑上不同的回路必须至少包含一个参考模块，而湿空气网络没有此要求。有关详细信息，请参阅 Reference Node and Grounding Rules。

Absolute Reference (MA) 模块的用途是为 Pressure & Temperature Sensor (MA) 提供参考。例如，要测量某个节点的绝对压力和绝对温度，请将该节点连接到 Pressure & Temperature Sensor (MA) 模块的 **A** 端口。将 Pressure & Temperature Sensor (MA) 模块的 **B** 端口连接到 Absolute Reference (MA) 模块。

如果在湿空气网络中的其他地方使用 Absolute Reference (MA) 模块，则会触发仿真断言，因为空气混合物的压力和温度不能处于绝对零。
