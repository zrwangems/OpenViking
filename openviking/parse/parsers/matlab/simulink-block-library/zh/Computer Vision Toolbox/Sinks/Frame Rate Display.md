---
type: simulink-block
title: 'Frame Rate Display'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'frameratedisplay'
documentation_source_path: 'ref/frameratedisplay.html'
language: zh-CN
chinese_source: worker-translation
---

# Frame Rate Display

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入数据矩阵 | 数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### 输入

### **Port\_1** — 输入数据矩阵 | 数组

输入数据，指定为 *M*×*N* 矩阵、*M*×*N*×*T* 数组或 *M*×*N*×*C*×*T* 数组。*T* 是视频或图像序列中的帧数，*C* 是颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Update rate
  summary: 更新频率 10（默认）| 正标量
  group: ''
```

### **Update rate** — 更新频率 `10`（默认）| 正标量

指定此参数以控制模块更新显示的频率。模块显示指定视频帧数内的平均更新率。例如，如果此参数设置为 `10`，Frame Rate Display 模块计算将 `10` 个视频帧传递到模块所经过的时间，将经过的时间除以 `10`，并显示平均视频帧率。

**注意**

如果 Frame Rate Display 模块的输入端口未连接到信号，模块将显示 Simulink® 模型的基础（最快）速率。
## 所属库

Computer Vision Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算并显示视频帧率

Frame Rate Display 模块计算并显示输入信号的平均更新率。对于输入视频信号，此模块显示仿真的视频帧率。计算出的速率与挂钟时间相关。例如，如果模型每秒更新输入信号 30 次，此模块将在模块掩码上显示 `30`。

此模块支持图像和视频帧作为输入。输入可以包含强度值或颜色值。
