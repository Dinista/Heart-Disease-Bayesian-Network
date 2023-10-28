# Heart-Disease-Bayesian-Network
## Introduction


This project employs <a href="https://en.wikipedia.org/wiki/Bayesian_network">Bayesian network</a> modeling to address a <b>diagnostic analysis problem</b>. It utilizes a dataset from an online database containing information about symptoms of <b>heart diseases</b> in patients. <b>The model calculates the probability of a patient having heart diseases</b>.


## How it works

The dataset (<b>heart-die.cvs</b>) was taken from the website <a href="https://archive.ics.uci.edu/ml/datasets/heart+disease">UC Irvine Machine Learning Repository</a>, and it was used in four different scenarios: occurrence of heart disease related to <b>chest pain</b>, <b>heart rate</b>, <b>electrocardiogram peak</b> and <b>resting electrocardiographic result</b>. 

### Dataset

The dataset comprises a total of <b>303 patients</b>, with <b>165 diagnosed with heart disease</b> and 138 without. Columns define as follow:

<ul>
<li>age;</li>
<li>sex;</li>
<li><b>cp</b> (chest pain);</li>
<li>trestbps;</li>
<li>chol;</li>
<li>fbs;</li>
<li><b>restecg</b> (resting electrocardiographic result);</li>
<li><b>thalach</b> (heart rate);</li>
<li>exang;</li>
<li>oldpeak;</li>
<li><b>slope</b> (electrocardiogram peak);</li>
<li>ca;</li>
<li>thal;</li>
<li>doencaCardiaca (bool: has heart disease);</li>
</ul>

## How to use

<b>The "heart-die.cvs" file must remain in the same folder as the program.</b>

### Input

The user needs to select from the menu a <b>type of chest pain </b> (four options), specify a <b>value for heart rate</b> (value between 71 and 202), choose <b>the peak slope of the electrocardiogram</b>, and indicate the <b>result of the resting electrocardiographic</b>.

### Output



### Dependency

The following libraries are required to use the program:

<ul>
<li> <a href="https://pandas.pydata.org/">Pandas</a> (Dataframe creation);</li>
<li><a href="https://pgmpy.org/">Pgmpy</a> (Probabilistic graphical models);</li>
<li><a href="https://numpy.org/">Numpy</a> (Math operations);</li>
</ul>
