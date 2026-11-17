---
type: simulink-block
title: 'C2000 Arctangent IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000arctangentiqn'
documentation_source_path: 'ref/c2000arctangentiqn.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 Arctangent IQN

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Function**
:   要计算的反正切类型：

    - `atan2` — 计算四象限反正切，输出以弧度为单位，值从 -pi 到 +pi。
    - `atan2PU` — 计算每单位四象限反正切。如果 `atan2(B,A)` 大于或等于 0，则 `atan2PU(B,A) = atan2(B,A)/2*pi`。否则，`atan2PU(B,A) = atan2(B,A)/2*pi+1`。输出以每单位弧度为单位，值从 0 到 2\*pi 弧度。

**注意**

Arctangent IQN 模块的输入顺序对应 Texas Instruments 约定，参数 'A' 在上方，'B' 在下方。

**Function**
:   要计算的反正切类型：

    - `atan2` — 计算四象限反正切，输出以弧度为单位，值从 -pi 到 +pi。
    - `atan2PU` — 计算每单位四象限反正切。如果 `atan2(B,A)` 大于或等于 0，则 `atan2PU(B,A) = atan2(B,A)/2*pi`。否则，`atan2PU(B,A) = atan2(B,A)/2*pi+1`。输出以每单位弧度为单位，值从 0 到 2\*pi 弧度。

**注意**

Arctangent IQN 模块的输入顺序对应 Texas Instruments 约定，参数 'A' 在上方，'B' 在下方。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

四象限反正切

# C2000 Arctangent IQN

四象限反正切

Arctangent IQN 模块计算 IQ 数值输入的四象限反正切，并生成 IQ 数值输出。

**注意**

此模块的实现不会在代码生成期间调用相应的 Texas Instruments® 库函数。Texas Instruments 函数使用全局 Q 设置，而此模块使用的 MathWorks® 代码会根据模块输入动态调整 Q 格式。有关更多信息，请参阅 Using the IQmath Library。

- C2000 Arctangent IQN 模块
