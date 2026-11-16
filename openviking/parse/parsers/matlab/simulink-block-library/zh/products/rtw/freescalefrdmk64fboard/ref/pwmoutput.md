---
type: simulink-block
title: 'PWM Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'pwmoutput'
documentation_source_path: 'freescalefrdmk64fboard/ref/pwmoutput.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Output

## 端口

在 R2025b 中未提供文档。

## 参数

**引脚**
:   选择用于生成脉冲波形的输出引脚。要查看引脚映射，请点击 **查看引脚映射**。

**初始频率 (Hz)**
:   以 Hertz 为单位指定初始频率。默认初始频率为 2000 Hz。

**初始占空比 (0 – 100)**
:   指定介于 0 到 100 之间的初始占空比。默认初始占空比为 0。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

在 R2025b 中未提供文档。

## 版本历史

**在 R2016a 中推出**

## 描述

在指定输出引脚上生成脉冲波形

在指定的输出引脚上生成脉冲波形。可以将 0 到 100 之间的值作为模块输入。所提供的输入值用于控制脉冲波形的占空比。输入为 ‘0’ 时，模块产生的占空比为 ‘0’%；输入为 ‘100’ 时，模块产生的占空比为 100%。
