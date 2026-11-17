---
type: simulink-block
title: 'C2802x/C2803x/C2806x/F28M3x AnalogIO Output'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c2802xc2803xc2806xf28m3xanalogiooutput'
documentation_source_path: 'ref/c2802xc2803xc2806xf28m3xanalogiooutput.html'
language: zh-CN
chinese_source: worker-translation
---

# C2802x/C2803x/C2806x/F28M3x AnalogIO Output

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**参数（输出引脚）**
:   选择模拟输出引脚。如果模块的输入为 True，选择 **Toggle**
    会反转引脚的输出电压电平。

**参数（输出引脚）**
:   选择模拟输出引脚。如果模块的输入为 True，选择 **Toggle**
    会反转引脚的输出电压电平。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

配置 Analog IO 以在特定引脚上输出模拟信号

# C2802x/C2803x/C2806x/F28M3x AnalogIO Output

配置 Analog IO 以在特定引脚上输出模拟信号

使用此模块驱动 Analog IO 引脚的输出电压。

在常规模式下，模块输入的值为 True 会将 Analog IO 引脚拉高，而值为 False 会将引脚接地。

在切换模式下，模块输入的值为 True 会切换 Analog IO 引脚的实际输出电平，而值为 False 不会改变 Analog IO 引脚的输出电平。

- C2802x/C2803x/C2806x/F28M3x AnalogIO Output 模块
