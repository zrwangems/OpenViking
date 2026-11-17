---
type: simulink-block
title: 'Digital Input'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'digitalinput'
documentation_source_path: '../rtw/freedomboard/ref/digitalinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Input

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**Pin**
:   选择数字引脚。

    确保不要将同一个引脚编号分配给模型中的多个模块。

**Sample time**
:   指定此模块读取数字引脚值的频率，以秒为单位。此参数值默认为 1/10 秒。

**View pin map**
:   点击此按钮可打开开发板快照，其中包含 GPIO 引脚的参考信息。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

读取数字输入引脚的逻辑值

读取所选数字输入引脚的逻辑值。FRDM-KL25Z 开发板上有 14 个引脚可用作数字信号输入，即 D0-D13。该开发板的数字引脚布局与标准 Arduino 数字引脚兼容。

在没有硬件的仿真过程中，此模块输出零值。
