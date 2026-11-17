---
type: simulink-block
title: 'Estimate Geometric Transformation'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Geometric Transformations'
documentation_page: 'estimategeometrictransformation'
documentation_source_path: 'ref/estimategeometrictransformation.html'
language: en
---

# Estimate Geometric Transformation

## Ports
```yaml
ports:
- name: Pts1
  summary: Point coordinates *M*-by-2 matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Pts2
  summary: Point coordinates *M*-by-2 matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Num
  summary: Number of valid points scalar
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: TForm
  summary: Transformation 3-by-2 matrix | 3-by-3 matrix
  direction: output
  data_types: single | double
- name: Inlier
  summary: Points used *M*-by-1 vector
  direction: output
  data_types: Boolean
```

### Input

### **Pts1** — Point coordinates *M*-by-2 matrix

Point coordinates, specified as an *M*-by-2 matrix of one-based
[*x*
*y*] point coordinates, where *M* represents the
number of points.

The block outputs the same data type for the transformation matrix as the
**Pts1** and **Pts2** image points.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Pts2** — Point coordinates *M*-by-2 matrix

Point coordinates, specified as an *M*-by-2 matrix of one-based
[*x*
*y*] point coordinates, where *M* represents the
number of points.

The block outputs the same data type for the transformation matrix as the
**Pts1** and **Pts2** image points.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Num** — Number of valid points scalar

Number of valid points to find in **Pts1** and
**Pts2**, specified as a scalar. This port appears when you enable
the **Allow variable-size signal input** parameter.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **TForm** — Transformation 3-by-2 matrix | 3-by-3 matrix

Transformation, returned as either a 3-by-2 or a 3-by-3 matrix. The block outputs
the same data type for the transformation matrix as the **Pts1** and
**Pts2** image points.

#### Dependencies

- When **Pts1** and **Pts2** are single or
  double, the output transformation matrix will also have single or double data
  type.
- When **Pts1** and **Pts2** images are
  built-in integers, the option is available to set the transformation matrix data
  type to either `Single` or `Double`.

**Data Types:** `single` | `double`

### **Inlier** — Points used *M*-by-1 vector

Points used to calculate `TForm`, returned as an
*M*-by-1 vector.

#### Dependencies

- The **Inlier** port appears when you enable the
  **Output Boolean signal indicating which point pairs are
  inliers** parameter.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Transformation type
  summary: Transformation type Affine (default) | Nonreflective similarity | Projective
  group: ''
- name: Find and exclude outliers
  summary: Find and exclude outliers on (default) | off
  group: ''
- name: Method
  summary: Method to find outliers RANdom SAmple Consensus (RANSAC) (default) | Least Median of Squares
  group: ''
- name: Algebraic distance threshold for determining inliers
  summary: Algebraic distance threshold for determining inliers 1.5 (default) | scalar
  group: ''
- name: Distance threshold for determining inliers (in pixels)
  summary: Distance threshold for determining inliers (in pixels) 1.5 (default) | scalar
  group: ''
- name: Determine number of random samplings using
  summary: Determine number of random samplings using Specified value (default) | Desired confidence
  group: ''
- name: Number of random samplings
  summary: Number of random samplings 500 (default) | scalar
  group: ''
- name: Desired confidence (in %)
  summary: Desired confidence (in %) 99 (default) | scalar
  group: ''
- name: Maximum number of random samplings
  summary: Maximum number of random samplings 1000 (default) | integer
  group: ''
- name: Stop sampling earlier when a specified percentage of point pairs are determined to be inlier
  summary: Stop sampling off (default) | on
  group: ''
- name: Perform additional iterative refinement of the transformation matrix
  summary: Perform additional iterative refinement off (default) | on
  group: ''
- name: Output Boolean signal indicating which point pairs are inliers
  summary: Output Boolean signal off (default) | on
  group: ''
- name: When Pts1 and Pts2 are built-in integers, set transformation matrix date type to
  summary: Set transformation matrix date type Single (default) | Double
  group: ''
- name: Allow variable-sized signal input
  summary: Allow variable-sized signal input on (default) | off
  group: ''
```

### **Transformation type** — Transformation type `Affine` (default) | `Nonreflective similarity` | `Projective`

Specify the transformation type as either `Nonreflective
similarity`, `Affine`, or
`Projective`. See Transformations for a
more detailed discussion.

#### Dependencies

You can set additional parameters depending on the transformation type:

- For `Projective` transformation, you can specify a
  scalar algebraic distance threshold for determining inliers.
- For `Affine` or `Nonreflective
  similarity` transformation, you can specify the distance threshold
  for determining inliers in pixels.

### **Find and exclude outliers** — Find and exclude outliers on (default) | off

Enable to find and exclude outliers from the input points and use only the inlier
points to calculate the transformation matrix. When you turn this parameter off, all
input points are used to calculate the transformation matrix.

### **Method** — Method to find outliers `RANdom SAmple Consensus (RANSAC)` (default) | `Least Median of Squares`

Select the method to find outliers as either `RANdom SAmple Consensus
(RANSAC)` or `Least Median of Squares` See RANSAC and Least Median Squares Algorithms for a more detailed
discussion.

#### Dependencies

This parameter appears when you enable the **Find and exclude
outliers** check box.

### **Algebraic distance threshold for determining inliers** — Algebraic distance threshold for determining inliers 1.5 (default) | scalar

Specify a scalar threshold value for determining inliers. The threshold controls the
upper limit used to find the algebraic distance in the RANSAC algorithm.

#### Dependencies

This parameter appears when you set the **Method** parameter to
`Random Sample Consensus (RANSAC)` and the
**Transformation type** parameter to
`Projective`.

### **Distance threshold for determining inliers (in pixels)** — Distance threshold for determining inliers (in pixels) `1.5` (default) | scalar

Specify the upper limit distance a point can differ from the projection location of
its corresponding point.

#### Dependencies

This parameter appears when you set the **Method** parameter to
`Random Sample Consensus (RANSAC)` and you set the value of
the **Transformation type** parameter to `Nonreflective
similarity` or `Affine`.

### **Determine number of random samplings using** — Determine number of random samplings using `Specified value` (default) | `Desired confidence`

Select `Specified value`  to enter a positive integer value
for the number of random samplings. Select `Desired
confidence` to set the number of random samplings as a percentage and a
maximum number.

#### Dependencies

This parameter appears when you select the **Find and exclude
outliers** check box, and you set the value of the
**Method** parameter to `Random Sample Consensus
(RANSAC)`.

### **Number of random samplings** — Number of random samplings `500` (default) | scalar

Specify the number of random samplings for the algorithm to perform.

#### Dependencies

This parameter appears when you set the value of the **Determine number of
random samplings using**  parameter to `Specified
value`.

### **Desired confidence (in %)** — Desired confidence (in %) `99` (default) | scalar

Specify a percent desired confidence by entering a number between
`0` and `100`. The value represents the probability
of the algorithm to find the largest group of points that can be mapped by a
transformation matrix.

#### Dependencies

This parameter appears when you set the **Determine number of random
samplings using** parameter to `Desired
confidence`.

### **Maximum number of random samplings** — Maximum number of random samplings `1000` (default) | integer

Specify an integer number for the maximum number of random samplings.

#### Dependencies

This parameter appears when you set the **Method** parameter to
`Random Sample Consensus (RANSAC)` and you set the value of
the **Determine number of random samplings using** parameter to
`Desired confidence`.

### **Stop sampling earlier when a specified percentage of point pairs are determined to be inlier** — Stop sampling off (default) | on

Enable this parameter to stop random sampling when a percentage of input points have
been found as inliers.

#### Dependencies

This parameter appears when you set the **Method** parameter to
`Random Sample Consensus (RANSAC)`.

### **Perform additional iterative refinement of the transformation matrix** — Perform additional iterative refinement off (default) | on

Specify whether to perform refinement on the transformation matrix.

#### Dependencies

This parameter appears when you select **Find and exclude outliers** check box.

### **Output Boolean signal indicating which point pairs are inliers** — Output Boolean signal off (default) | on

Enable this parameter to output the inlier point pairs that were used to calculate
the transformation matrix.

#### Dependencies

- This parameter appears when you select the **Find and exclude outliers** check box.
- The block will not use this parameter with signed or double, data type
  points.

### **When Pts1 and Pts2 are built-in integers, set transformation matrix date type to** — Set transformation matrix date type `Single` (default) | `Double`

Specify transformation matrix data type as `Single` or
`Double` when the input points are built-in integers.

#### Dependencies

The block will not use this parameter with signed or double, data type
points.

### **Allow variable-sized signal input** — Allow variable-sized signal input on (default) | off

Enable this parameter to allow variable-sized signal input.

#### Dependencies
## Libraries

Computer Vision Toolbox / Geometric Transformations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integera` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a Generated code will be restricted to MATLAB host computers when you set the FFT implementation parameter to FFTW, or when the transform length is not a power of two. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2008a**

## Description

Estimate geometric transformation from matching point pairs

Use the Estimate Geometric Transformation block to find the transformation matrix which
maps the greatest number of point pairs between two images. A *point
pair* refers to a point in the input image and its related point on the image
created using the transformation matrix. You can select to use the RANdom SAmple Consensus
(RANSAC) or the Least Median Squares algorithm to exclude outliers and to calculate the
transformation matrix. You can also use all input points to calculate the transformation
matrix.
