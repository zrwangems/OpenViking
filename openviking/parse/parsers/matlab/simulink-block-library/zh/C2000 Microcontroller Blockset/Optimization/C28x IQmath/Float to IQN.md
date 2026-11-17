---
type: simulink-block
title: 'C2000 Float to IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000floattoiqn'
documentation_source_path: 'ref/c2000floattoiqn.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 Float to IQN

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Q value**
:   Q value，范围为 1 到 30，用于指定输出的精度

**Q value**
:   Q value，范围为 1 到 30，用于指定输出的精度
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

将浮点数转换为 IQ 数

# C2000 Float to IQN

将浮点数转换为 IQ 数

该模块将浮点数转换为 IQ 数。输出的 Q value 在对话框中指定。

**注意**

该模块的实现不会在代码生成期间调用相应的 Texas Instruments® 库函数。TI 函数使用全局 Q 设置，而该模块使用的 MathWorks® 代码会根据模块输入动态调整 Q 格式。有关更多信息，请参阅 Using the IQmath Library。

- C2000 Float to IQN 模块
