# Linear Regression
This is a small example of linear regression usingScipy library

Sources - [Source 1](https://www.dezyre.com/data-science-in-r-programming-tutorial/linear-regression-tutorial), [Source 2](https://en.wikipedia.org/wiki/Linear_regression), [Source 3](https://machinelearningmastery.com/linear-regression-for-machine-learning/), [Source 3](https://analyticstraining.com/popular-applications-of-linear-regression-for-businesses/).

### 1.1. What is regression?
- Regression is a statistical way to establish a relationship between a dependent variable and a set of independent variable(s). 
- e.g., if we say that Age = 5 + Height * 10 + Weight * 13
- Here we are establishing a relationship between Height & Weight of a person with his/ Her Age. 
     
### 1.2. What is linear regression?
 - Linear regression is a linear approach to modelling the relationship between a scalar response (or dependent variable) and one or more explanatory variables (or independent variables).  
 - Linear regression is a linear model, e.g. a model that assumes a linear relationship between the input variables (x) and the single output variable (y).
 
 #### 1.2.1 What is simple linear regression?
 - In a simple regression problem (a single x and a single y), the form of the model would be y = B0 + B1*x


### 2. Usual I/O Data types:
- Inputs: Numerical data in terms of one dependent and other independent variable.
- Outputs: A line thet tries to fit the data and associated average error in prediction.


### 3. Few use cases:
- Assess risk in financial services or insurance domain
- Generate insights on consumer behaviour
- Analyze the marketing effectiveness, pricing and promotions on sales of a product


### 4. Shotcomings:
- It assumes that your input and output variables are not noisy.
- Very sensitive to Outliers
- Suffers from multicollinearity, autocorrelation, heteroskedasticity.
  - Multi-collinearity: a state of very high intercorrelations or inter-associations among the independent variables. It is therefore a type of disturbance in the data, and if present in the data the statistical inferences made about the data may not be reliable.
  - Auto-correlation: a characteristic of data in which the correlation between the values of the same variables is based on related objects. If the change in the income of a person A affects the savings of person B (a person other than person A), then autocorrelation is present. 
  - Heteroskedasticity: A phenomenon when the standard deviations of a variable, monitored over a specific amount of time, are nonconstant.

### 5. Example - Implementation details:
- Data is spread like a sine curve for better visualization
- The linear model return 
  - slope of line
  - intercept of regression line
  - correlation coefficient
  - standard error of estimated gradient.

