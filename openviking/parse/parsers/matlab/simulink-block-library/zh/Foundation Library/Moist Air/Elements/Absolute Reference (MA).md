---
type: simulink-block
title: 'Absolute Reference (MA)'
family: 'simscape'
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
```yaml
ports:
- name: A
  summary: 压力、温度、比湿度和微量气体质量分数均为零的湿空气
  direction: unspecified
```

### 守恒

### **A** — 压力、温度、比湿度和微量气体质量分数均为零的湿空气

湿空气守恒端口，其中压力和温度等于绝对零度，比湿度和微量气体质量分数等于零。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2023a: Absolute Reference (MA) 模块不再推荐使用

Pressure & Temperature Sensor (MA) 模块现在包含一个隐式参考节点，这意味着您只需要一个端口即可进行压力或温度的绝对测量。仅当您需要测量模型中两个节点之间的压力或温度差时，才需要暴露第二个端口。

在之前的版本中，要测量端口 **A** 处的绝对压力和绝对温度，您需要将端口 **B** 连接到 Absolute Reference (MA) 模块。这不再必要，因为您现在可以通过将 Pressure & Temperature Sensor (MA) 模块的 **Measurement reference** 参数设置为 `Absolute` 来进行绝对测量。

此更改没有兼容性影响。现有模型中如果已将 Absolute Reference (MA) 模块连接到 Pressure & Temperature Sensor (MA) 模块，将继续像以前一样工作。

## 描述

（不推荐）绝对零温度和压力下的参考点

Absolute Reference (MA) 模块表示湿空气网络中压力和温度的绝对参考。在端口 **A** 处，压力和温度等于绝对零度。比湿度和微量气体质量分数也等于零。

与其他域不同——在其他域中，域内每个拓扑上不同的回路必须至少包含一个参考模块——湿空气网络没有此要求。有关详细信息，请参阅 Reference Node and Grounding Rules。

Absolute Reference (MA) 模块的目的是为 Pressure & Temperature Sensor (MA) 提供参考。例如，要测量某个节点的绝对压力和绝对温度，请将该节点连接到 Pressure & Temperature Sensor (MA) 模块的 **A** 端口。将 Pressure & Temperature Sensor (MA) 模块的 **B** 端口连接到 Absolute Reference (MA) 模块。

如果您在湿空气网络的其他位置使用 Absolute Reference (MA) 模块，则会触发仿真断言，因为空气混合物压力和温度不可能处于绝对零度。
