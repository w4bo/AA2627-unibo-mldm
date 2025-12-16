# Data Mining

# Multi classifier

![](img/multi/7-Multi%20Classifier_0.png)

__Matteo Golfarelli__

# Basics



* Construct multiple base classifiers and predict the class to which a record belongs by aggregating the classifications obtained
  * The result of the compound classifier is defined by means of a function that, for example, assigns the record to the class that was "voted" by the largest number of classifiers


# Bayes Theorem: an example



* Suppose we have 25 simple classifiers.
  * Each classifier has an error-rate of  = 0.35
  * Assume that the classifiers are independent
* There is no correlation between the error-rates of the classifiers
* The probability that the compound classifier gives an incorrect result is:
* Necessary conditions for the compound classifier to give better results than the simple classifiers are:
  * That the classifiers are independent
  * That the error-rate of the single classifier is less than 0.5 Let us suppose


# How to build a composite classifier



* __Changing the training set: building more training sets from the given data set__
  * Bagging and Boosting


# How to build a composite classifier (cont.)



* __Changing the training set: building more training sets from the given data set__
  * Bagging and Boosting
* __By changing the attributes used: individual classifiers are based on a subset of the attributes__
  * Useful when attributes are highly redundant  Random Forest


# How to build a composite classifier (cont.)



* __Changing the training set: building more training sets from the given data set__
  * Bagging and Boosting
* __By changing the attributes used: individual classifiers are based on a subset of the attributes__
  * Useful when attributes are highly redundant  Random Forest
* __Changing the classes considered: __
  * Partition the classes into two groups A0 and A1 and transforms the given problem into a binary problem. The classes that belong to A0 are classified as 0 the remaining ones as 1.
  * The different classifiers are constructed by resubdividing the classes into different subsets
  * The classification of the composite classifier is obtained by increasing the score of the classes that belong to the chosen subset by 1.
  * The record is finally assigned to the class that obtains the highest score
  * Error-Correcting Output Coding: translates a multi-class classification problem into a binary classification one


# How to build a composite classifier (cont.)



* __Changing the training set: building more training sets from the given data set__
  * Bagging and Boosting
* __By changing the attributes used: individual classifiers are based on a subset of the attributes__
  * Useful when attributes are highly redundant  Random Forest
* __Changing the classes considered: __
  * One partitions the classes into two groups A0 and A1 and transforms the given problem into a binary problem. The classes that belong to A0 are classified as 0 the remaining ones as 1.
  * The different classifiers are constructed by resubdividing the classes into different subsets
  * The classification of the composite classifier is obtained by increasing the score of the classes that belong to the chosen subset by 1.
  * The record is finally assigned to the class that obtains the highest score
  * Error-Correcting Output Coding: translates a multi-class classification problem into a binary classification one
* __Changing the parameters of the learning algorithm:__
  * Topology and weights of a neural network
  * Decision trees with random choice policies of the attributes to be used


# Error Decomposition: Bias, Variance & Noise



* A formal model for analyzing the error made by a classifier
  * Probability of a classifier making a mistake in its prediction
* The error committed by a classifier depends on:
  * __BIAS__ : ability of the chosen classifier in modeling events and extending the prediction to events not in the training set
    * Different types of classifiers have different capabilities in defining decision boundary between classes
    * For example, different decision trees may have different capabilities
  * __VARIANCE__ : capability of the training set in representing the actual data set
    * Different training sets may result in different decision boundary
  * __NOISE__ : non-determinism of the classes to be determined
    * Set instances with the same attribute values may result in different classes


![](img/multi/7-Multi%20Classifier_1.png)

![](img/multi/7-Multi%20Classifier_2.png)

# Error Decomposition: Bias, Variance & Noise (cont.)



* Different types of classifiers have inherently different capabilities in modeling the edges of regions
  * 100 training sets each containing 100 examples obtained from a predefined region partition (dashed line)
  * The black line represents the average true line of separation obtained from the 100 classifiers
* The difference between the true separation line and the average separation line represents the classifier bias
  * The bias of the 1-NN is lower
  * However, k-NNs are more sensitive to the composition of the training set and therefore will exhibit greater variance


![](img/multi/7-Multi%20Classifier_3.png)

# Multi classifier



* Different classifiers (e.g., Decision trees + k-nearest neighbor) are used to reduce error bias
  * Classifiers must be independent: no (or little) correlation between errors made between two classifiers
  * Different classifiers can operate on distinct subsets of  _attributes _ on which they have ideal performance
* Class membership is decided by a voting mechanism
  * Class voted on by the largest number of classifiers
  * Voting can be weighted according to the confidence of the classifier in case the classifier provides it
  * Ex. C1 classifier votes for class X. In training C1 made 25 out of 100 errors for class X. Classifier C2 votes for class Y. In training phase C2 committed 10 out of 100 errors for class Y.
  * __The record is assigned to class Y__


# Bagging



* Allows the construction of compound classifiers that associate an event with the highest rated class from the base classifiers
* Each classifier is constructed by  __bootstrapping__  the same training set
* //  _k _ = number of boostrap cycles  _N_  = training set cardinality
* // ()=1 if the argument is TRUE, 0 otherwise
* __	for __  _i_ =1 to  _k _  __do__
* Create a training set  _D_  _i_  such that | _D_  _i_ |= _N_
* Train a classifier  _C_  _i_  using  _D_  _i_
* __	end for__
* Bagging improves generalization error by reducing the  __variance__  component
  * Thus, bagging will be particularly useful for those types of classifiers that are sensitive to changes in the training set


# Bagging (cont.)



* Allows the construction of compound classifiers that associate an event with the highest rated class from the base classifiers
* Each classifier is constructed by  __bootstrapping__  the same training set
* //  _k _ = number of boostrap cycles  _N_  = training set cardinality
* // ()=1 if the argument is TRUE, 0 otherwise
* __	for __  _i_ =1 to  _k _  __do__
* Create a training set  _D_  _i_  such that | _D_  _i_ |= _N_
* Train a classifier  _C_  _i_  using  _D_  _i_
* __	end for__
* Bagging improves generalization error by reducing the  __variance__  component
  * Thus, bagging will be particularly useful for those types of classifiers that are sensitive to changes in the training set


In statistics: any test or metric that uses random sampling with replacement

# Bagging: an example



* Basic classifier: one-level binary decision tree
  * Can only make choices of the type x  s  -1    x>s  1 where s is the split point
* The data set
* Accuracy of the basic classifier cannot exceed 70%
  * x  0.3  1     x>0.3  -1
  * x  0.7  -1   x>0.7  1


| _x_ | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| _y_ | 1 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 | 1 |

# Bagging cycles

![](img/multi/7-Multi%20Classifier_4.png)

# Bagging result

Bagging determines the behavior of a two-level decision tree

![](img/multi/7-Multi%20Classifier_5.png)

_Draw_  _ the _  _two_  _-level _  _decision_  _ _  _tree_  _ _  _corresponding_  _ to the result of _  _bagging_

# Random Forest

# Boosting



  * An iterative approach to progressively adjust the composition of the training set in order to focus on incorrectly classified records
  * Initially, all N records have the same weight (1/N)
  * Unlike bagging, the weights can change at the end of the boosting round in order to increase the probability of the record being selected in the training set
    * The probability of records that are difficult to classify i.e., that were classified incorrectly in the previous boosting round are increased
  * The final result is obtained by combining the predictions made by the different classifiers
  * Boosting techniques differ based on how:
  * the weights of the training set records are updated
  * the predictions of the classifiers are combined
  * __AdaBoost __ is one of the most widely used boosting techniques


# AdaBoost



  * Let  _C_ 1,  _C_ 2, ...,  _C_  _T_  _ _ be the basic  _T_  classifiers each used at a boost cycle  _j_   [1, _T_ ]. Let  __  _j_  be the error rate:
  * ( _x_  _i_ ,y _i_ ) i=1..N records of the training set
  * _w_  _i_  is the weight of the i-th element of the training set
  * ()=1 if the argument is TRUE, 0 otherwise
  * The relevance of a classifier is defined as:
  *  _j_  takes positive values when the error rate is close to 0
  *  _j_  takes negative values when the error rate is close to 1


![](img/multi/7-Multi%20Classifier_7.png)

# AdaBoost (cont.)



  * The weight updating rule for record  _i_  at boosting cycle  _j _ is
  * _Z_  _j_  is a normalization factor to ensure that
  * The weight of correctly classified records is reduced,
  * that of weights classified incorrectly increases
  * If a boost cycle produces a classifier with error rate greater than 50%, the weights are reported 1/n
  * The record is assigned to the class that maximizes the weighted sum:


# AdaBoost (cont.)

__w__ ={ _w_  _i_ =1/N  _i_ =1..N}

__for __  _j_ =1 to T _ _  __do__  // boost __ __ cycle number

Build a training set D _j_  by sampling with replacement based on  __w__

Train a classifier C _j_  on D _j_

Apply C _j_  to D

_   _  _j_ =1/N  _i_  _w_  _i_ (C _j_ ( __x__ i) _y_  _i_ )  // compute the weighted error

__	if__   __  _j _ > 0.5  __then __

__w__ ={ _w_  _i_ =1/N| _i_ =1,2,…,N};  // reset!

__	else__

_		_  _j_ =1/2 ln((1- __  _j_ )/ __  _j_ );

Update the weight  __w;__

__	end if;__

__end for;__

__                          __ // sign return 1/-1 if the classification is correct/wrong

# AdaBoost: an example



* Basic classifier: one-level binary decision tree
  * Can only make choices of the type x  s  -1    x>s  1 where s is the split point
* The data set
* Accuracy of the basic classifier cannot exceed 70%
  * x  0.3  1     x>0.3  -1
  * x  0.7  -1   x>0.7  1


| _x_ | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| _y_ | 1 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 | 1 |

# AdaBoost: cycles

![](img/multi/7-Multi%20Classifier_8.png)

# AdaBoost: cycles (cont.)

![](img/multi/7-Multi%20Classifier_9.png)

Split point: 0.75

__ 1 _ _ =0.03

__ 1=1.738

Split point: 0.05

__ 2 _ _ =0.004

__ 2=2.7784

Split point: 0.30

__ 3 _ _ =0.00027

__ 3=4.1195

# AdaBoost: an example



* The dataset
* The result
  * 5.16 = -1.738 + 2.7784 + 4.1195
  * The classifier does not make errors adopting a behvior compatible with a two-level decision tree


| _x_ | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| _y_ | 1 | 1 | 1 | -1 | -1 | -1 | -1 | 1 | 1 | 1 |

![](img/multi/7-Multi%20Classifier_10.png)

__ 1=1.738

__ 2=2.7784

__ 3=4.1195

