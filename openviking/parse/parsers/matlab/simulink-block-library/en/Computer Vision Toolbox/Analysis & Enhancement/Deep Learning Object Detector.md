---
type: simulink-block
title: 'Deep Learning Object Detector'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'deeplearningobjectdetector'
documentation_source_path: 'ref/deeplearningobjectdetector.html'
language: en
---

# Deep Learning Object Detector

## Ports

### Input

### **Image** — Image data array

An *H*-by-*W*-by-*C* numeric
array, where *H*, *W*, and *C* are
the height, width, and number of channels of the image, respectively. Only one image
per time step is allowed as input.
### Output

### **Bboxes** — Locations of objects detected matrix

Locations of the objects detected within the input image, returned as an
*M*-by-4 or an *M*-by-5 matrix.
*M* is the number of bounding boxes detected in the image. You can
put an upper bound to the size *M* by specifying the
**Maximum Number of Detections** parameter.

The table describes the format of bounding boxes.

| **Bounding Box** | ***Description*** |
| --- | --- |
| **Axis-aligned rectangle** | Defined in spatial coordinates as an *M*-by-4 numeric matrix with rows of the form [*x* *y* *w* *h*], where:  - *M* is the number of axis-aligned rectangles. - *x* and `y` specify the upper-left corner of the   rectangle. - *w* specifies the width of the rectangle, which is its length   along the *x*-axis. - *h* specifies the height of the rectangle, which is its length   along the *y*-axis. |
| **Rotated rectangle** | Defined in spatial coordinates as an *M*-by-5 numeric matrix with rows of the form [*xctr* *yctr* *w* *h* *yaw*], where:  - *M* is the number of rotated rectangles. - *xctr* and *yctr* specify the center of the   rectangle. - *w* specifies the width of the rectangle, which is its length   along the *x*-axis before rotation. - *h* specifies the height of the rectangle, which is its length   along the *y*-axis before rotation. - *yaw* specifies the rotation angle in degrees. The rotation is   clockwise-positive around the center of the bounding box.  Square rectangle rotated by -30 degrees. |

For more information, see Datastores for Deep Learning (Deep Learning Toolbox).

### **Labels** — Labels for bounding boxes vector

Labels for the bounding boxes, returned as an *M*-by-1 enumerated
vector. *M* is the number of bounding boxes detected in the
image.

### **Scores** — Detection scores vector

Detection confidence scores for each label, returned as an
*M*-by-1 vector. *M* is the number of bounding boxes
detected in the image. A higher score indicates higher confidence in the
detection.

## Parameters

### **Detector** — Source for trained detector object `Detector from MAT file` (default) | `Detector from MATLAB function`

Select the source for the detector object from these options:

- `Detector from MAT file` — Import a detector
  object from a MAT file. For example, select a MAT file containing a
  `yolov2ObjectDetector` object.
- `Detector from MATLAB function` — Import a
  detector object from a MATLAB function. For example, specify the function
  `vehicleDetectorYOLOv2`, which returns a trained
  `yolov2ObjectDetector` object.

The imported detector must be one of these supported objects:

- `rcnnObjectDetector`
- `fastRCNNObjectDetector`
- `fasterRCNNObjectDetector`
- `rtmdetObjectDetector`
- `ssdObjectDetector`
- `yolov2ObjectDetector`
- `yolov3ObjectDetector`
- `yolov4ObjectDetector`
- `yoloxObjectDetector`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Detector` |
| **Type:** character vector, string |
| **Values:** `Detector from MAT file'` | `'Detector from MATLAB function'` |
| **Default:** `Detector from MAT file'` |

### **File path** — MAT file containing detector object `untitled.mat` (default) | MAT file name

This parameter specifies the name of the MAT file that contains the detector object
to load. If the file is not on the MATLAB path, use the **Browse** button to locate the
file.

#### Dependencies

To enable this parameter, set the **Detector** parameter to
`Detector from MAT file`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DetectorFilePath` |
| **Type:** character vector, string |
| **Values:** MAT file path or name |
| **Default:**  `'untitled.mat'` |

### **MATLAB function** — MATLAB function name `untitled` (default) | MATLAB function name

This parameter specifies the name of the MATLAB function that returns a trained object detector. For example, specify the
function `vehicleDetectorYOLOv2`, which returns a trained
`yolov2ObjectDetector` object, or specify a custom function.

#### Dependencies

To enable this parameter, set the **Detector** parameter to
`Detector from MATLAB function`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DetectorFunction` |
| **Type:** character vector, string |
| **Values:** MATLAB function name |
| **Default:** `'untitled'` |

### **Region of interest** — Search region of interest vector of the form [*x* *y* *width* *height*]

Specify the search region of interest as vector of the form [*x y width height*]. The vector specifies the upper-left corner and size of
a region in pixels.

#### Dependencies

To enable this parameter, select the **Specify region of
interest** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ROI` |
| **Type:** character vector, string |
| **Values:** character vector specified as `'[x y width height]'` |
| **Default:** `'[1 1 100 100]'` |

### **Detection threshold** — Detection threshold scalar in the range [0, 1]

Specify the detection threshold as scalar in the range [0, 1]. Detections that have
scores lower than this threshold value are removed. To reduce false positives, increase
this value.

#### Dependencies

To enable this parameter, you must use a detector that supports the
**Detection threshold** parameter. For example, use a
`yolov2ObjectDetector` object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Threshold` |
| **Type:** character vector, string |
| **Values:** scalar |
| **Default:** `'0.5'` |

### **Number of Strongest Regions** — Maximum number of strongest region proposals `2000` (default) | positive integer

Specify the maximum number of strongest region proposals as an integer. Reduce this
value to speed up processing at the cost of detection accuracy. To use all region
proposals, specify this parameter as `Inf`.

#### Dependencies

To enable this parameter, use a detector that supports the **Number of
Strongest Regions** parameter. For example, use an
`rcnnObjectDetector` object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumStrongestRegions` |
| **Type:** character vector, string |
| **Values:** integer |
| **Default:** `'2000'` |

### **Maximum Region Size** — Maximum region size vector of the form [*height* *width*]

Specify the maximum region size as a vector of the form [*height*
*width*]. Units are in pixels. The maximum region size defines the size
of the largest region containing the object. For example, [`50`
`50`] sets the size of the largest region containing the object to
`50`-by-`50` pixels. To reduce computation time, set
this value to the known maximum region size for the objects that can be detected in the
input test images.

#### Dependencies

To enable this parameter

- Select the **Specify maximum region size**
  parameter.
- Use a detector that supports the **Maximum Region Size**
  parameter. For example, use a `yolov2ObjectDetector`
  object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaxSize` |
| **Type:** character vector, string |
| **Values:** character vector specified as `'[height width]'` |
| **Default:** `'[50 50]'` |

### **Minimum Region Size** — Minimum region size vector of the form [*height* *width*]

Specify the minimum region size as a vector of the form [*height*
*width*]. Units are in pixels. The minimum region size defines the size
of the smallest region containing the object. For example, [`1`
`1`] sets the size of the smallest region containing the object to
`1`-by-`1` pixels.

#### Dependencies

To enable this parameter

- Select the **Specify minimum region size**
  parameter.
- Use a detector that supports the **Minimum Region Size**
  parameter. For example, use a `yolov2ObjectDetector`
  object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MinSize` |
| **Type:** character vector, string |
| **Values:** character vector specified as `'[height width]'` |
| **Default:** `'[1 1]'` |

### **Maximum Number of Detections** — Maximum number of detections `500` (default) | positive integer

Specify the maximum number of detections as a positive integer. This value is the
upper bound for the number of detections and must be greater than or equal to 2.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaxDetections` |
| **Type:** character vector, string |
| **Values:** integer |
| **Default:** `'500'` |

## Libraries

Computer Vision Toolbox / Analysis & Enhancement

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- The **Language** parameter in the **Configuration
  Parameters** > **Code Generation** general category must
  be set to `C++`.
- For a list of networks and layers supported for code generation, see Networks and Layers Supported for Code Generation (MATLAB Coder).
- To generate code for the Math Kernel Library for Deep Neural Networks (MKL-DNN)
  target library with YOLOv3, YOLOv4, or RTMDet as the object detectors, set the
  `MaxStackSize` and `TLCOptions` model parameters
  to a higher value. For example, you can set the `MaxStackSize` and
  `TLCOptions` parameter values to '`inf`' using the
  following
  syntax.

  ```
  >> set_param(modelName,'MaxStackSize','inf')
  >> set_param(modelName,'TLCOptions','-aMaxStackVariableSize=inf')
  ```

### GPU Code Generation Generate CUDA® code for NVIDIA® GPUs using GPU Coder™.

Usage notes and limitations:

- The **Language** parameter in the **Configuration
  Parameters** > **Code Generation** general category must
  be set to `C++`.
- For a list of networks and layers supported for CUDA® code generation, see Supported Networks, Layers, and Classes (GPU Coder).

## Version History

**Introduced in R2021b**

### R2024b: Support to RTMDet object detector

Starting in R2024b, `Deep Learning Object Detector` block supports Real-Time Model for
object Detection (RTMDet). You can import a pretrained RTMDet object detector object,
`rtmdetObjectDetector` to perform object detection.

### R2024b: Support for YOLOX object detector

Starting in R2024b, `Deep Learning Object Detector` block supports You Only Look Once X
(YOLOX) object detection. You can import a pretrained YOLOX object detector object, `yoloxObjectDetector` to perform object detection.

## Description

Detect objects using trained deep learning object detector

The Deep Learning Object Detector block predicts bounding boxes, class
labels, and scores for the input image by using the trained object detector specified through
the block parameter. This block allows loading of a pretrained object detector into the
Simulink® model from a MAT file or from a MATLAB® function. This block provides a graphical interface for using the detector
objects in Simulink. To enable some parameters of the Deep Learning Object Detector
block you must choose an object detector that supports those parameters. For example, using a
`yolov2ObjectDetector` object with this block enables you to select
parameters similar to the name-value arguments of the associated `detect` object
function.
