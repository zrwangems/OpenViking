---
type: simulink-block
title: 'Neural Network Architectures'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Control Systems'
documentation_page: 'neural-network-architectures'
documentation_source_path: 'ug/neural-network-architectures.html'
language: zh-CN
chinese_source: worker-translation
---

# Neural Network Architectures

前面展示的两个或多个神经元可以组合在一个层中，而一个特定的网络可以包含一个或多个这样的层。首先考虑单层神经元。

前面展示的两个或多个神经元可以组合在一个层中，而一个特定的网络可以包含一个或多个这样的层。首先考虑单层神经元。

### One Layer of Neurons

一个具有 *R* 个输入元素和 *S* 个神经元的单层网络如下所示。

神经元层。该层接收输入向量 p 并计算列向量输出 a。

在该网络中，输入向量 **p** 的每个元素通过权重矩阵 **W** 连接到每个神经元输入。第 *i* 个神经元有一个求和器，它收集其加权输入和偏置以形成自己的标量输出 *n*(*i*)。各个 *n*(*i*) 组合在一起形成 *S* 元素净输入向量 **n**。最后，神经元层的输出形成列向量 **a**。**a** 的表达式显示在图底部。

请注意，层的输入数量通常不同于神经元数量（即 *R* 不一定等于 *S*）。层不受其输入数量等于其神经元数量的约束。

你可以通过将前面展示的两个网络并联，简单地创建一个具有不同传递函数的单个（复合）神经元层。两个网络将具有相同的输入，并且每个网络将创建部分输出。

输入向量元素通过权重矩阵 **W** 进入网络。

W=[w1,1w1,2…w1,Rw2,1w2,2…w2,RwS,1wS,2…wS,R]

请注意，矩阵 **W** 元素上的行索引表示权重的目标神经元，列索引表示该权重的输入来源。因此，*w*1,2 中的索引表示信号 *从* 第二个输入元素 *到* 第一个（也是唯一的）神经元的强度为 *w*1,2。

该 *S* 个神经元、*R* 个输入的单层网络也可以用简写形式绘制。

神经元层

这里 **p** 是 *R* 长度输入向量，**W** 是 *S* × *R* 矩阵，**a** 和 **b** 是 *S* 长度向量。如前所定义，神经元层包括权重矩阵、乘法运算、偏置向量 **b**、求和器以及传递函数模块。

#### Inputs and Layers

为了描述具有多个层的网络，必须扩展该表示法。具体来说，需要区分连接到输入的权重矩阵和连接在层之间的权重矩阵。还需要标识权重矩阵的源和目标。

我们将连接到输入的权重矩阵称为 *输入权重；* 我们将连接到层输出的权重矩阵称为 *层权重。* 此外，上标用于标识网络中各种权重和其他元素的源（第二个索引）和目标（第一个索引）。为了说明，前面展示的单层多输入网络在此以简写形式重新绘制。

神经元层

连接到输入向量 **p** 的权重矩阵被标记为输入权重矩阵（**IW**1,1），其源为 1（第二个索引），目标为 1（第一个索引）。第 1 层的元素，例如其偏置、净输入和输出，具有上标 1，表示它们与第一层相关联。

Multiple Layers of Neurons 使用层权重（**LW**）矩阵以及输入权重（**IW**）矩阵。

### Multiple Layers of Neurons

一个网络可以有多个层。每一层都有一个权重矩阵 **W**、一个偏置向量 **b** 和一个输出向量 **a**。为了区分图中这些层各自的权重矩阵、输出向量等，将层的编号作为上标附加到相关变量上。你可以在接下来展示的三层网络以及图底部的方程中看到这种层表示法的使用。

三层神经元

上面展示的网络具有 *R*1 个输入、第一层中的 *S*1 个神经元、第二层中的 *S*2 个神经元等。不同层通常具有不同数量的神经元。常量输入 1 被馈送到每个神经元的偏置。

请注意，每个中间层的输出是下一层的输入。因此，第 2 层可以作为一个具有 *S*1 个输入、*S*2 个神经元和 *S*2 × *S*1 权重矩阵 **W**2 的单层网络来分析。第 2 层的输入是 **a**1；输出是 **a**2。既然第 2 层的所有向量和矩阵都已标识，它就可以单独作为一个单层网络来处理。这种方法可以用于网络中的任何层。

多层网络的各层扮演不同的角色。产生网络输出的层称为 *输出层*。所有其他层称为 *隐藏层*。前面展示的三层网络有一个输出层（第 3 层）和两个隐藏层（第 1 层和第 2 层）。一些作者将输入称为第四层。此工具箱不使用该 designation。

具有单个输入向量的多层网络架构可以用表示法 *R* − *S*1 − *S*2 −...− *SM* 来指定，其中指定了输入向量的元素数量以及每一层中的神经元数量。

同一个三层网络也可以使用简写表示法绘制。

三层神经元

多层网络非常强大。例如，一个两层网络，其中第一层是 sigmoid 层，第二层是线性层，可以被训练以任意好地逼近任何函数（具有有限数量的不连续点）。这种两层网络在 Multilayer Shallow Neural Networks and Backpropagation Training 中被广泛使用。

这里假设第三层的输出 **a**3 是感兴趣的网络输出，并且该输出被标记为 **y**。此表示法用于指定多层网络的输出。

### 输入和输出处理函数

网络输入可能具有关联的处理函数。处理函数将用户输入数据转换为对网络更容易或更高效的形式。

例如，`mapminmax` 转换输入数据，使所有值落入区间 [−1, 1]。这可以加速许多网络的学习。`removeconstantrows` 删除输入向量中对应于始终具有相同值的输入元素的行，因为这些输入元素没有向网络提供任何有用信息。第三个常见的处理函数是 `fixunknowns`，它将未知数据（在用户数据中用 `NaN` 值表示）重新编码为网络可用的数值形式。`fixunknowns` 保留关于哪些值已知、哪些值未知的信息。

类似地，网络输出也可以具有关联的处理函数。输出处理函数用于转换用户提供的目标向量以供网络使用。然后，使用相同的函数对网络输出进行反向处理，以产生与原始用户提供目标具有相同特征的输出数据。

`mapminmax` 和 `removeconstantrows` 通常都与网络输出相关联。然而，`fixunknowns` 不是。目标中的未知值（由 `NaN` 值表示）不需要为网络使用而更改。

处理函数在 Choose Neural Network Input-Output Processing Functions 中有更详细的描述。

## 另请参阅

### Topics

- Neuron Model
- Workflow for Neural Network Design

## MATLAB 命令

您点击的链接对应于以下 MATLAB 命令：

在 MATLAB 命令窗口中输入该命令以运行它。
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

Select a Web Site

选择一个网站，以便在可提供翻译内容的地方获取翻译内容并查看本地活动和优惠。根据您的位置，我们建议您选择：。

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择一个网站

**How to Get Best Site Performance**

选择中国网站（中文或英文）以获得最佳网站性能。其他 MathWorks 国家/地区网站未针对您所在位置的访问进行优化。

Americas

- América Latina (Español)
- Canada (English)
- United States (English)

Europe

- Belgium (English)
- Denmark (English)
- Deutschland (Deutsch)
- España (Español)
- Finland (English)
- France (Français)
- Ireland (English)
- Italia (Italiano)
- Luxembourg (English)

- Netherlands (English)
- Norway (English)
- Österreich (Deutsch)
- Portugal (English)
- Sweden (English)
- Switzerland
  - Deutsch
  - English
  - Français
- United Kingdom (English)

Asia Pacific

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

Contact your local office
