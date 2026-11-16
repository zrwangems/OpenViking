---
type: simulink-block
title: 'Parameter Node'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Describe System Behaviors / Describe Activity Diagrams'
documentation_page: 'parameternode'
documentation_source_path: 'ref/parameternode.html'
language: zh-CN
chinese_source: official
---

# Parameter Node

## 端口

R2025b 官方文档未提供。

## 参数

### 参数节点

在执行嵌套活动时，参数节点充当对象令牌的缓冲区。参数节点本身会影响相应的引脚。

### **名称** — 参数节点名称 字符串

输入或输出参数节点的名称。默认情况下，该参数被称为 `InputPin` 或 `OutputPin`，具体取决于其配置。当为动作节点添加更多输入或输出引脚时，`InputPin` 或 `OutputPin` 的数字后缀会分别增加。

### **令牌重数** — 开始执行所需的令牌数量 `1` (默认) | 正整数

输入参数节点开始执行相应动作节点所需的令牌数。如果输入参数节点的多重性大于 1，则它可以容纳多个令牌。执行时，动作节点接收的对象令牌数量与多重性参数指定的数量完全一致。

### **正在流式传输** — 启用或禁用流式传输的选项 `off` (默认) | `on`

启用或禁用输入或输出参数节点的数据流。该流控制的值会自动应用于动作节点的相应输入或输出活动引脚。

### **构造型** — 导入的配置文件中的构造型列表 可用构造型的名称

该列表包含导入的配置文件中的构造型。要为参数节点指定构造型，请从列表中选择构造型。

您还可以使用 `<new/edit>` 选项，使用配置文件编辑器管理配置文件。

### 对象类型

输入或输出引脚可以处理特定类型的对象令牌。在属性检查器中，引脚的**对象类型**部分允许您指定对象令牌的类型和其他属性。

### **名称** — 参数节点保存的对象类型 `<owned>` (默认) | `<inherit>` | `custom type`

参数节点持有的对象类型。

- `<owned>` - 从属性检查器中为对象令牌选择属性，如类型、维度、复杂度和单位。
- `<inherit>` - 继承前一个引脚的对象类型。
- `custom type` - 从使用类型编辑器创建的自定义类型列表中选择。

### **方向** — 令牌流经参数节点的方向 `Input` | `Output`

根据创建的是输入引脚还是输出引脚，该参数会自动设置为 `Input` 或 `Output`。

### **类型** — 令牌数据类型 `double` (默认) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `MATLAB Class`

令牌的数据类型。有关使用 MATLAB 类类型的更多信息，请参阅使用 MATLAB 类令牌在活动图中建模复杂对象。

#### 依赖项

要启用该参数，请将**名称**设置为 **<owned>**。

### **维度** — 令牌维度 `1` (默认) | 正整数

令牌的维度。

#### 依赖项

要启用该参数，请将**名称**设置为 **<owned>**。

### **单位** — 令牌单位 字符串

您为令牌指定的自定义单位。

#### 依赖项

要启用该参数，请将**名称**设置为 **<owned>**。

### **复杂度** — 令牌复杂度 `real` (默认) | `complex` | `auto`

令牌的复杂度。

#### 依赖项

要启用该参数，请将**名称**设置为 **<owned>**。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2024a 中推出**

## 描述

通过嵌套活动图处理令牌

参数节点充当对象令牌的缓冲器，引导令牌进入或离开嵌套活动。参数节点的方向性代表输入或输出。您可以通过对象流连接参数节点。

对于具有活动行为类型的动作节点，在创建引脚时，软件会在嵌套活动内创建相应的参数节点。

这就是输入和输出参数节点的两种类型：

- 流式参数节点

  Streaming input parameter node
- 非流式参数节点

  Non-streaming input parameter node
