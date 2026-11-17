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
language: en
---

# Neural Network Architectures

Two or more of the neurons shown earlier can be combined in a layer, and a particular network could contain one or more such layers. First consider a single layer of neurons.

Two or more of the neurons shown earlier can be combined in a layer, and a particular
network could contain one or more such layers. First consider a single layer of
neurons.

### One Layer of Neurons

A one-layer network with *R* input elements and
*S* neurons follows.

Layer of neurons. The layer receives input vector p and calculates a column vector output a.

In this network, each element of the input vector **p** is
connected to each neuron input through the weight matrix **W**. The *i*th
neuron has a summer that gathers its weighted inputs and bias to form its own scalar output
*n*(*i*). The various
*n*(*i*) taken together form an
*S*-element net input vector **n**. Finally,
the neuron layer outputs form a column vector **a**. The
expression for **a** is shown at the bottom of the
figure.

Note that it is common for the number of inputs to a layer to be different from the
number of neurons (i.e., *R* is not necessarily equal to
*S*). A layer is not constrained to have the number of its inputs equal
to the number of its neurons.

You can create a single (composite) layer of neurons having different transfer functions
simply by putting two of the networks shown earlier in parallel. Both networks would have
the same inputs, and each network would create some of the outputs.

The input vector elements enter the network through the weight matrix **W**.

W=[w1,1w1,2…w1,Rw2,1w2,2…w2,RwS,1wS,2…wS,R]

Note that the row indices on the elements of matrix **W**
indicate the destination neuron of the weight, and the column indices indicate which source
is the input for that weight. Thus, the indices in
*w*1,2 say that the strength of the signal
*from* the second input element *to* the first (and
only) neuron is *w*1,2.

The *S* neuron *R*-input one-layer network also can be
drawn in abbreviated notation.

Layer of neurons

Here **p** is an *R*-length input vector,
**W** is an *S* × *R*
matrix, **a** and **b** are
*S*-length vectors. As defined previously, the neuron layer includes the
weight matrix, the multiplication operations, the bias vector **b**, the summer, and the transfer function blocks.

#### Inputs and Layers

To describe networks having multiple layers, the notation must be extended.
Specifically, it needs to make a distinction between weight matrices that are connected to
inputs and weight matrices that are connected between layers. It also needs to identify
the source and destination for the weight matrices.

We will call weight matrices connected to inputs *input weights;* we will call weight matrices connected to layer
outputs *layer weights.* Further, superscripts are used to identify the
source (second index) and the destination (first index) for the various weights and other
elements of the network. To illustrate, the one-layer multiple input network shown earlier
is redrawn in abbreviated form here.

Layer of neurons

The weight matrix connected to the input vector **p** is
labeled as an input weight matrix (**IW**1,1) having a source 1 (second index) and a
destination 1 (first index). Elements of layer 1, such as its bias, net input, and output
have a superscript 1 to say that they are associated with the first layer.

Multiple Layers of Neurons uses layer weight
(**LW**) matrices as well as input weight (**IW**) matrices.

### Multiple Layers of Neurons

A network can have several layers. Each layer has a weight matrix **W**, a bias vector **b**, and an output vector
**a**. To distinguish between the weight matrices, output
vectors, etc., for each of these layers in the figures, the number of the layer is appended
as a superscript to the variable of interest. You can see the use of this layer notation in the three-layer network shown next, and in the equations at the
bottom of the figure.

Three layers of neurons

The network shown above has *R*1 inputs,
*S*1 neurons in the first layer,
*S*2 neurons in the second layer, etc. It is
common for different layers to have different numbers of neurons. A constant input 1 is fed
to the bias for each neuron.

Note that the outputs of each intermediate layer are the inputs to the following layer.
Thus layer 2 can be analyzed as a one-layer network with
*S*1 inputs,
*S*2 neurons, and an
*S*2 ×
*S*1 weight matrix **W**2. The input to layer 2 is **a**1; the output is **a**2. Now that all the vectors and matrices of layer
2 have been identified, it can be treated as a single-layer network on its own. This
approach can be taken with any layer of the network.

The layers of a multilayer network play different roles. A layer that produces the
network output is called an *output layer*. All other layers are called *hidden layers*. The three-layer network shown earlier has one output
layer (layer 3) and two hidden layers (layer 1 and layer 2). Some authors refer to the
inputs as a fourth layer. This toolbox does not use that designation.

The architecture of a multilayer network with a single input vector can be specified
with the notation *R* − *S*1 −
*S*2 −...−
*SM*, where the number of elements of the
input vector and the number of neurons in each layer are specified.

The same three-layer network can also be drawn using abbreviated notation.

Three layers of neurons

Multiple-layer networks are quite powerful. For instance, a network of two layers, where
the first layer is sigmoid and the second layer is linear, can be trained to approximate any
function (with a finite number of discontinuities) arbitrarily well. This kind of two-layer
network is used extensively in Multilayer Shallow Neural Networks and Backpropagation Training.

Here it is assumed that the output of the third layer, **a**3, is the network output of interest, and this
output is labeled as **y**. This notation is used to specify
the output of multilayer networks.

### Input and Output Processing Functions

Network inputs might have associated processing functions. Processing functions
transform user input data to a form that is easier or more efficient for a network.

For instance, `mapminmax` transforms input data so that all
values fall into the interval [−1, 1]. This can speed up learning for many networks.
`removeconstantrows` removes the rows of the
input vector that correspond to input elements that always have the same value, because
these input elements are not providing any useful information to the network. The third
common processing function is `fixunknowns`, which recodes unknown data
(represented in the user's data with `NaN` values) into a numerical form
for the network. `fixunknowns` preserves information about which
values are known and which are unknown.

Similarly, network outputs can also have associated processing functions. Output
processing functions are used to transform user-provided target vectors for network use.
Then, network outputs are reverse-processed using the same functions to produce output data
with the same characteristics as the original user-provided targets.

Both `mapminmax` and `removeconstantrows` are often associated with network outputs. However,
`fixunknowns` is not. Unknown values in targets
(represented by `NaN` values) do not need to be altered for network
use.

Processing functions are described in more detail in Choose Neural Network Input-Output Processing Functions.

## See Also

### Topics

- Neuron Model
- Workflow for Neural Network Design

## MATLAB Command

You clicked a link that corresponds to this MATLAB command:

Run the command by entering it in the MATLAB Command Window.
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

Select a Web Site

Choose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select: .

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

You can also select a web site from the following list

**How to Get Best Site Performance**

Select the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.

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
