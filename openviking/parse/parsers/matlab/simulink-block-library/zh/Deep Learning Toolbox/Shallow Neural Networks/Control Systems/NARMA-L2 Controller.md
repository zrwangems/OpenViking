---
type: simulink-block
title: 'Design NARMA-L2 Neural Controller in Simulink'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Control Systems'
documentation_page: 'design-narma-l2-neural-controller-in-simulink'
documentation_source_path: 'ug/design-narma-l2-neural-controller-in-simulink.html'
language: zh-CN
chinese_source: worker-translation
---

# Design NARMA-L2 Neural Controller in Simulink

本节描述的神经控制器有两个不同的名称：反馈线性化控制和 NARMA-L2 控制。当被控对象模型具有特定形式（伴随形式）时，称为反馈线性化。当被控对象模型可以用相同形式近似时，称为 NARMA-L2 控制。这类控制的核心思想是通过抵消非线性项，将非线性系统动态转换为线性动态。本节首先介绍伴随形式系统模型，并展示如何使用神经网络来辨识该模型。然后描述如何使用辨识出的神经网络模型来开发控制器。接下来是一个如何使用 NARMA-L2 Control 模块的示例，该模块包含在 Deep Learning Toolbox™ 模块集中。

本节描述的神经控制器有两个不同的名称：反馈线性化控制和 NARMA-L2 控制。当被控对象模型具有特定形式（伴随形式）时，称为反馈线性化。当被控对象模型可以用相同形式近似时，称为 NARMA-L2 控制。这类控制的核心思想是通过抵消非线性项，将非线性系统动态转换为线性动态。本节首先介绍伴随形式系统模型，并展示如何使用神经网络来辨识该模型。然后描述如何使用辨识出的神经网络模型来开发控制器。接下来是一个如何使用 NARMA-L2 Control 模块的示例，该模块包含在 Deep Learning Toolbox™ 模块集中。

### NARMA-L2 模型的辨识

与模型预测控制一样，使用反馈线性化（或 NARMA-L2）控制的第一步是辨识待控制的系统。您需要训练一个神经网络来表示系统的前向动态。第一步是选择要使用的模型结构。用于表示一般离散时间非线性系统的一种标准模型是非线性自回归滑动平均（NARMA）模型：

y(k+d)=N[y(k),y(k−1),…,y(k−n+1),u(k),u(k−1),…,u(k−n+1)]

其中 *u*(*k*) 是系统输入，*y*(*k*) 是系统输出。在辨识阶段，您可以训练一个神经网络来近似非线性函数 *N*。这是用于 NN Predictive Controller 的辨识过程。

如果您希望系统输出跟随某个参考轨迹 *y*(*k* + *d*) = *yr*(*k* + *d*)，下一步是开发如下形式的非线性控制器：

u(k)=G[y(k),y(k−1),…,y(k−n+1),yr(k+d),u(k−1),…,u(k−m+1)]

使用此控制器的问题在于，如果您想训练一个神经网络来创建函数 *G* 以最小化均方误差，您需要使用动态反向传播（[NaPa91] 或 [HaJe99]）。这可能相当慢。Narendra 和 Mukhopadhyay [NaMu97] 提出的一种解决方案是使用近似模型来表示系统。本节使用的控制器基于 NARMA-L2 近似模型：

y^(k+d)=f[y(k),y(k−1),…,y(k−n+1),u(k−1),…,u(k−m+1)]+g​[y(k),y(k−1),…,y(k−n+1),u(k−1),…,u(k−m+1)]⋅u(k)

该模型为伴随形式，其中下一个控制器输入 *u*(*k*) 不包含在非线性项中。这种形式的优点是，您可以求解使系统输出跟随参考 *y*(*k* + *d*) = *yr*(*k* + *d*) 的控制输入。由此得到的控制器形式为

u(k)=yr(k+d)−f[y(k),y(k−1),…,y(k−n+1),u(k−1),…,u(k−n+1)]g[y(k),y(k−1),…,y(k−n+1),u(k−1),…,u(k−n+1)]

直接使用此方程可能会导致实现问题，因为您必须根据同一时刻的输出 *y*(*k*) 来确定控制输入 *u*(*k*)。因此，应改用以下模型

y(k+d)=f[y(k),y(k−1),…,y(k−n+1),u(k),u(k−1),…,u(k−n+1)]+g[y(k),…,y(k−n+1),u(k),…,u(k−n+1)]⋅u(k+1)

其中 *d* ≥ 2。下图展示了神经网络表示的结构。

### NARMA-L2 控制器

使用 NARMA-L2 模型，您可以获得控制器

u(k+1)=yr(k+d)−f[y(k),…,y(k−n+1),u(k),…,u(k−n+1)]g[y(k),…,y(k−n+1),u(k),…,u(k−n+1)]

该控制器在 *d* ≥ 2 时是可实现的。下图是 NARMA-L2 控制器的框图。

该控制器可以使用先前辨识的 NARMA-L2 被控对象模型来实现，如下图所示。

### 使用 NARMA-L2 Controller 模块

本节展示如何训练 NARMA-L2 控制器。第一步是将 NARMA-L2 Controller 模块从 Deep Learning Toolbox 模块库复制到 Simulink® Editor 中。如果您不确定如何操作，请参阅 Simulink 文档。以下示例中省略了此步骤。

Deep Learning Toolbox 软件提供了一个示例模型来展示 NARMA-L2 控制器的使用。在此示例中，目标是控制悬浮在电磁铁上方的磁体的位置，其中磁体被约束为只能沿垂直方向移动，如下图所示。

该系统的运动方程为

d2y(t)dt2=−g+αMi2(t)y(t)−βMdy(t)dt

其中 *y*(*t*) 是磁体距电磁铁的距离，*i*(*t*) 是流过电磁铁的电流，*M* 是磁体的质量，*g* 是重力常数。参数 β 是由磁体运动所在材料决定的粘性摩擦系数，α 是由电磁铁上线圈匝数和磁体强度决定的场强常数。

要运行此示例：

1. 启动 MATLAB®。
2. 在 MATLAB 命令窗口中输入 `narmamaglev`。此命令将打开 Simulink Editor 并显示以下模型。NARMA-L2 Control 模块已在模型中。

   narmamaglev 模型的截图
3. 双击 NARMA-L2 Controller 模块。这将打开以下窗口。此窗口使您能够训练 NARMA-L2 模型。控制器没有单独的窗口，因为与模型预测控制器不同，控制器是直接从模型确定的。

   Plant Identification - NARMA-L2 窗口的截图
4. 此窗口的操作方式与其他 Plant Identification 窗口相同，因此不再重复训练过程。而是直接仿真 NARMA-L2 控制器。
5. 返回 Simulink Editor，通过选择菜单选项 **Simulation** > **Run** 启动仿真。仿真运行时，会显示被控对象输出和参考信号，如下图所示。

   包含蓝色和绿色线条的绘图。该绘图标题为 "X Y Plot"，水平和垂直轴分别标记为 X 和 Y。

## MATLAB 命令

您点击了一个对应于以下 MATLAB 命令的链接：

在 MATLAB 命令窗口中输入该命令来运行它。
Web 浏览器不支持 MATLAB 命令。

关闭

MathWorks
MathWorks

选择网站

选择一个网站以获取可用的翻译内容并查看本地活动和优惠。根据您的位置，我们建议您选择：。

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择一个网站

**如何获得最佳网站性能**

选择中国网站（中文或英文）以获得最佳网站性能。其他 MathWorks 国家/地区网站未针对您所在位置的访问进行优化。

美洲

- América Latina (Español)
- Canada (English)
- United States (English)

欧洲

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

亚太地区

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

联系您当地的办事处
