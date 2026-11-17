---
type: simulink-block
title: 'Design Neural Network Predictive Controller in Simulink'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Control Systems'
documentation_page: 'design-neural-network-predictive-controller-in-simulink'
documentation_source_path: 'ug/design-neural-network-predictive-controller-in-simulink.html'
language: zh-CN
chinese_source: worker-translation
---

# Design Neural Network Predictive Controller in Simulink

在 Deep Learning Toolbox™ 软件中实现的神经网络预测控制器使用非线性被控对象的神经网络模型来预测未来的被控对象性能。然后，控制器计算控制输入，以在指定的未来时间范围内优化被控对象性能。模型预测控制的第一步是确定神经网络被控对象模型（系统辨识）。接下来，控制器使用被控对象模型来预测未来性能。（有关各种模型预测控制策略在线性系统中的应用的完整介绍，请参阅 Model Predictive Control Toolbox™ 文档。）

在 Deep Learning Toolbox™ 软件中实现的神经网络预测控制器使用非线性被控对象的神经网络模型来预测未来的被控对象性能。然后，控制器计算控制输入，以在指定的未来时间范围内优化被控对象性能。模型预测控制的第一步是确定神经网络被控对象模型（系统辨识）。接下来，控制器使用被控对象模型来预测未来性能。（有关各种模型预测控制策略在线性系统中的应用的完整介绍，请参阅 Model Predictive Control Toolbox™ 文档。）

以下部分描述了系统辨识过程。随后描述了优化过程。最后，讨论了如何使用在 Simulink® 环境中实现的模型预测控制器模块。

**注意**

要设计神经网络预测控制器，您还可以使用 System Identification Toolbox™ 和 Model Predictive Control Toolbox。使用 System Identification Toolbox 通过神经网络进行被控对象建模，并使用 Model Predictive Control Toolbox 设计控制器。

推荐使用此工作流，因为它具有以下优势：

- 将被控对象建模和控制设计解耦。
- 通过用于神经网络被控对象和控制器的专用 Simulink 模块，轻松与 Simulink 集成。
- 用于线性和非线性预测控制的多个内置求解器。
- 支持代码生成。

有关展示如何使用这些工具的示例，请参阅 Control House Heating Using Nonlinear MPC with Neural State-Space Prediction Model (Model Predictive Control Toolbox)。

### 系统辨识

模型预测控制的第一阶段是训练神经网络来表示被控对象的前向动态。被控对象输出与神经网络输出之间的预测误差用作神经网络训练信号。该过程由下图表示：

系统辨识图，输入为 u，输出为 y\_p。

神经网络被控对象模型使用先前的输入和先前的被控对象输出来预测被控对象输出的未来值。神经网络被控对象模型的结构如下图所示。

两层神经网络图，输入为 y\_p(t) 和 u(t)，输出为 y\_m(t+1)。

该网络可以使用从被控对象运行中收集的数据，以批处理模式离线训练。您可以使用 Multilayer Shallow Neural Networks and Backpropagation Training 中讨论的任何训练算法进行网络训练。此过程将在以下部分中更详细地讨论。

### 预测控制

模型预测控制方法基于滚动时域技术 [SoHa96]。神经网络模型在指定的时间范围内预测被控对象响应。数值优化程序使用这些预测来确定使指定范围内的以下性能指标最小化的控制信号

J=∑j=N1N2(yr(t+j)−ym(t+j))2+ρ∑j=1Nu(u′(t+j−1)−u′(t+j−2))2

其中 *N*1、*N*2 和 *Nu* 定义了评估跟踪误差和控制增量的范围。*u*′ 变量是试探性控制信号，*yr* 是期望响应，*ym* 是网络模型响应。ρ 值决定了控制增量平方和对性能指标的贡献。

以下框图说明了模型预测控制过程。控制器由神经网络被控对象模型和优化模块组成。优化模块确定使 *J* 最小化的 *u*′ 值，然后将最优 *u* 输入到被控对象。控制器模块在 Simulink 中实现，如下一节所述。

框图，输入为 y\_r，输出为 y\_p

### 使用神经网络预测控制器模块

本节展示如何使用 NN Predictive Controller 模块。第一步是将 NN Predictive Controller 模块从 Deep Learning Toolbox 模块库复制到 Simulink Editor。如果不确定如何操作，请参阅 Simulink 文档。以下示例中跳过此步骤。

Deep Learning Toolbox 软件提供了一个示例模型来展示预测控制器的使用。此示例使用催化连续搅拌釜反应器 (CSTR)。该过程的示意图如下图所示。

过程示意图，包含 w\_1、C\_b1、w\_2 和 C\_b2，以及输出 w\_0 和 C\_b

系统的动态模型为

dh(t)dt=w1(t)+w2(t)−0.2h(t)dCb(t)dt=(Cb1−Cb(t))w1(t)h(t)+(Cb2−Cb(t))w2(t)h(t)−k1Cb(t)(1+k2Cb(t))2

其中 *h*(*t*) 是液位，*Cb*(*t*) 是过程输出处的产物浓度，*w*1(*t*) 是浓缩进料 *Cb*1 的流速，*w*2(*t*) 是稀释进料 *Cb*2 的流速。输入浓度设置为 *Cb*1 = 24.9 和 *Cb*2 = 0.1。与消耗速率相关的常数为 *k*1 = 1 和 *k*2 = 1。

控制器的目标是通过调节流速 *w*1(*t*) 来维持产物浓度。为简化示例，设置 *w*2(*t*) = 0.1。本实验不控制罐的液位 *h*(*t*)。

要运行此示例：

1. 启动 MATLAB®。
2. 在 MATLAB Command Window 中键入 `predcstr`。此命令打开 Simulink Editor 并显示以下模型。

   Simulink 中 predstr 模型的截图。

   Plant 模块包含 Simulink CSTR 被控对象模型。NN Predictive Controller 模块信号的连接方式如下：

   - Control Signal 连接到 Plant 模型的输入。
   - Plant Output 信号连接到 Plant 模块输出。
   - Reference 连接到 Random Reference 信号。
3. 双击 NN Predictive Controller 模块。这将打开以下用于设计模型预测控制器的窗口。此窗口使您能够更改控制器范围 *N*2 和 *Nu*。（*N*1 固定为 1。）前面描述的加权参数 ρ 也在此窗口中定义。参数 α 用于控制优化。它决定了成功优化步骤所需的性能降低量。您可以选择优化算法使用哪种线性最小化例程，并且可以决定每个采样时间执行多少次优化算法迭代。线性最小化例程是 Multilayer Shallow Neural Networks and Backpropagation Training 中讨论的例程的轻微修改。

   Neural Network Predictive Control 对话框的截图
4. 选择 **Plant Identification**。这将打开以下窗口。在使用控制器之前，您必须开发神经网络被控对象模型。被控对象模型预测未来的被控对象输出。优化算法使用这些预测来确定优化未来性能的控制输入。被控对象模型神经网络有一个隐藏层，如前所示。您在此窗口中选择该层的大小、延迟输入和延迟输出的数量以及训练函数。您可以选择 Multilayer Shallow Neural Networks and Backpropagation Training 中描述的任何训练函数来训练神经网络被控对象模型。

   Plant Identification 对话框的截图
5. 点击 **Generate Training Data**。程序通过向 Simulink 被控对象模型施加一系列随机阶跃输入来生成训练数据。然后，潜在训练数据显示在类似于下图的图中。

   Plant Input-Output Data 对话框的截图
6. 点击 **Accept Data**，然后在 Plant Identification 窗口中点击 **Train Network**。被控对象模型训练开始。训练根据您选择的训练算法（本例中为 `trainlm`）进行。这是批处理训练的简单应用，如 Multilayer Shallow Neural Networks and Backpropagation Training 中所述。训练完成后，显示所得被控对象模型的响应，如下图所示。（如果存在验证和测试数据，也有单独的图。）

   Training Data for NN Predictive Control 对话框的截图

   然后，您可以通过再次选择 **Train Network** 使用相同数据集继续训练，可以 **Erase Generated Data** 并生成新数据集，或者可以接受当前被控对象模型并开始仿真闭环系统。对于此示例，开始仿真，如下列步骤所示。
7. 在 Plant Identification 窗口中选择 **OK**。这将训练好的神经网络被控对象模型加载到 NN Predictive Controller 模块中。
8. 在 Neural Network Predictive Control 窗口中选择 **OK**。这将控制器参数加载到 NN Predictive Controller 模块中。
9. 返回 Simulink Editor，通过选择菜单选项 **Simulation** > **Run** 开始仿真。随着仿真的运行，显示被控对象输出和参考信号，如下图所示。

   标题为 "X Y Plot" 的二维线图。水平轴标记为 "X Axis"。垂直轴标记为 "Y Axis"。

## MATLAB 命令

您点击了对应于以下 MATLAB 命令的链接：

在 MATLAB Command Window 中输入该命令来运行它。Web 浏览器不支持 MATLAB 命令。

Close

MathWorks
MathWorks

选择网站

选择网站以获取本地化内容并查看本地活动和优惠。根据您的位置，我们建议您选择：

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择网站

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
