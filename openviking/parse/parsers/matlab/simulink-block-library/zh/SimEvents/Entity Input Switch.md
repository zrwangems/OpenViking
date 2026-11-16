---
type: simulink-block
title: 'Entity Input Switch'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'entityinputswitch'
documentation_source_path: 'ref/entityinputswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Entity Input Switch

## 端口

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

用于进入模块的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_2** — 输入实体 标量 | 向量 | 矩阵

用于进入模块的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **control** — 传入控制实体 标量

用于传入控制实体的输入控制端口，该控制实体确定到达模块的实体所使用的输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### 输出

### **Port\_1** — 输出实体 标量 | 向量 | 矩阵

用于退出模块的实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## 参数

### **输入端口数量** — 指定输入端口数量 `2`（默认）| 标量

确定模块具有多少实体输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`NumberInputPorts` |
| **类型**：character vector |
| **值**：`'2'` | 标量 |
| **默认**：`'2'` |

### **活动端口选择** — 指定活动输入端口 `All`（默认）| `Switch`

指定活动输入端口，以允许实体到达所有端口或一次到达一个端口。选择 `All` 可合并实体路径并允许实体到达所有端口。选择 `Switch` 可一次仅允许一个实体到达一个端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`ActivePortSelection` |
| **类型**：character vector |
| **值**：`'All'` | `'Switch'` |
| **默认**：`'All'` |

### **切换准则** — 指定输入端口切换准则 `Round robin`（默认）| `From control port` | `Equiprobable`

选择在输入端口之间切换的准则。

- 选择 `Round robin` 以轮询方式选择端口。在 **初始端口选择** 中设置初始端口。
- 选择 `From control port` 以让控制端口确定所选端口。将出现一个控制端口，用于输入携带数据的匿名实体，该数据的值大于 `0` 且小于或等于输入端口数量，以确定活动端口。
- 选择 `Equiprobable` 以让模块以相等概率随机选择任何端口。设置 **种子** 以生成随机数并确定活动输入端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SwitchingCriterion` |
| **类型**：character vector |
| **值**：`'Round robin'` | `'From control port'` | `'Equiprobable'` |
| **默认**：`'Round robin'` |

### **初始端口选择** — 指定用于实体进入的初始输入端口 `1`（默认）| 标量

指定初始允许实体到达的端口。

#### 程序化使用

|  |
| --- |
| **模块参数**：`InitialPortSelection` |
| **类型**：character vector |
| **值**：`'1'` | 标量 |
| **默认**：`'1'` |

### **种子** — 指定用于确定输入端口的随机数生成器种子 `23453`（默认）| 标量

指定用于确定输入端口的随机数生成器种子。

#### 依赖项

当 **切换准则** 设置为 `Equiprobable` 时，此参数可见。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Seed` |
| **类型**：character vector |
| **值**：`'23453'` | 标量 |
| **默认**：`'23453'` |

## 所属库

SimEvents

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

切换输入实体

使用输入开关的典型场景是多个实体源馈入单个队列，其中排序遵循特定规则。例如，分时计算机的终端用户将作业提交到馈入中央处理单元的队列，其中算法调节对队列的访问，以防止任何一个用户不公平地占用。

**注意**

如果要合并消息或实体路径并生成组件接口代码，请使用 Simulink® Message Merge 模块。Message Merge 模块的行为与将 **活动端口选择** 参数设置为 `All` 的 Entity Output Switch 模块相同。

有关示例，请参阅 Generate Entities When Events Occur。

### 合并实体路径

可以使用 **活动端口选择** 参数设置为 `All` 的 Entity Input Switch 模块将多个路径合并为单个路径。合并实体路径不会更改实体本身，就像合并道路车道不会改变在其上行驶的车辆一样。特别地，Entity Input Switch 模块不会创建聚合或批次。

以下是可能合并实体路径的一些场景：

- 附加不同数据 — 多个实体生成器模块创建对特定属性具有不同值的实体。然后这些实体沿合并路径前进，但之后可能会根据它们各自的属性值而被区别对待。
- 合并队列 — 多个队列合并为单个队列。
- 连接反馈路径 — 反馈路径与普通路径进入同一队列。

### 对同时待处理的到达进行排序

Entity Input Switch 模块不会发生任何冲突，即使多个实体尝试同时到达。行为类别如下：

- 如果实体尝试到达时实体输出端口未被阻塞，则到达顺序取决于 Entity Input Switch 模块之前各模块的离开事件顺序。

  即使多个实体的离开时间相同，顺序也可能影响系统行为。例如，如果实体前进到队列，离开顺序将决定它们在队列中的位置。
- 如果当 Entity Input Switch 模块的实体输出端口从阻塞变为未阻塞时，有待处理实体正等待前进到该模块，则会按顺序通知实体输入端口此变化。从阻塞变为未阻塞意味着实体可以前进到 Entity Input Switch 模块。

  如果至少两个实体正在通过不同的实体输入端口等待前进到 Entity Input Switch 模块，则通知顺序很重要，因为第一个收到此变化通知的端口会第一个将实体前进到 Entity Input Switch 模块。

### 选择到达路径

Entity Input Switch 模块允许实体到达其端口。所选实体输入端口可以在仿真期间更改。

还可以选择在输入端口之间切换的准则。

- 选择 `Round robin` 以轮询方式选择端口。
- 选择 `From control port` 以让控制端口确定所选端口。
- 选择 `Equiprobable` 以让模块以相等概率随机选择任何端口。

### 限制

实体输入端口总数必须小于 128。要对超过 128 个端口建模，请并行或串联使用多个 Entity Input Switch 模块。
