# **Behavioral Cloning**

## Writeup Template

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[model]: ./examples/placeholder.png "Model Visualization"
[image2]: ./examples/placeholder.png "Grayscaling"
[recovery_1]: ./examples/center_2020_12_01_17_20_41_819.jpg "Recovery Image 1"
[recovery_2]: ./examples/center_2020_12_01_17_20_42_521.jpg "Recovery Image 2"
[recovery_3]: ./examples/center_2020_12_01_17_20_43_913.jpg "Recovery Image 3"
[center_image]: ./examples/center_2020_12_01_16_21_11_291.jpg "Normal Image"
[flipped_image]: ./examples/center_flipped.jpg "Flipped Image"
[original_image]: ./examples/center_2020_12_01_17_01_53_958.jpg "Original Image"
[image7]: ./examples/placeholder_small.png "Flipped Image"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network
* writeup_report.md or writeup_report.pdf summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

My model consists of a convolution neural network with 5x5 and 3x3 filter sizes and depths between 25 and 64 (model.py lines //TODO) 

The model includes RELU layers to introduce nonlinearity (code line 20), and the data is normalized in the model using a Keras lambda layer (code line 32).

#### 2. Attempts to reduce overfitting in the model

The model contains dropout layers in order to reduce overfitting (model.py lines 49).

The model was trained and validated on different data sets to ensure that the model was not overfitting (code line //TODO). The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 25).

#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used the given sample data and additionally I generated 2 extra laps of center lane driving, as well as 1 recovery lap and 1 lap driving in the opposite direction.

For details about how I created the training data, see the next section.

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

The overall strategy for deriving a model architecture was to ...

My first step was to use a convolution neural network model similar to the ... I thought this model might be appropriate because ...

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. I found that my first model had a low mean squared error on the training set but a high mean squared error on the validation set. This implied that the model was overfitting. 

To combat the overfitting, I modified the model so that ...

Then I ... 

The final step was to run the simulator to see how well the car was driving around track one. There were a few spots where the vehicle fell off the track... to improve the driving behavior in these cases, I ....

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The final model architecture (model.py lines 18-24) consisted of a convolution neural network with the following layers and layer sizes ...

Here is a visualization of the architecture (note: visualizing the architecture is optional according to the project rubric)

![center image][model]

#### 3. Creation of the Training Set & Training Process

I used the sample data set provided as a base and I added more data by driving the simulation. First, to capture good driving behavior, I recorded two laps on track one using center lane driving. Here is an example image of center lane driving:

![center image][center_image]

Then, I recorded the vehicle recovering from the left side and right sides of the road back to center so that the vehicle would learn to come back to the center in case the vehicle approaches a lane link. These images show what a recovery looks like starting from the vehicle close to the left border and returning to the center:

![alt text][recovery_1]
![alt text][recovery_2]
![alt text][recovery_3]

I repeated this process in multiple places of the lap for a complete circuit.

Additionally I drove the vehicle in the opposite direction of the loop to have more data and to help overcome the overfitting which naturally is generate by driving always to the left, making the car more susceptible to oversteer the vehicle to the left. This was also a center drive.



To augment the data sat, I also flipped images and angles thinking that this would augment the data in a really natural way, also the car tends to oversteer to the left because the loop is in that direction, so by flippint the image and inverting the angle this effect could be improved. For example, here is an image that has then been flipped:

![alt text][original_image]
![alt text][flipped_image]

After the collection process the original 30110 data points became a total of 60220. I then preprocessed this data by cropping relevant the highway section of the image, then applying a lambda function to center the data in 0 and between the values -1 and 1. 


I finally randomly shuffled the data set and put 20% of the data into a validation set.

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was Z as evidenced by ... I used an adam optimizer so that manually training the learning rate wasn't necessary.
