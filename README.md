# Dataset
The dataset contains ~2.7k customer quotation data for a life insurance product. An example of the customer quotation is given below. 

| QuoteRef| Channel | Product| Smoker| Joint?| Person1| Age | Term| TotalPremium|	GrossCommission|	Sale|	JF (Score)| WGB |X| EF|NOB|URB|LSB|BB|ND|
| --- |---| --- |---|--- |---|--- |---|--- |---|--- |---|--- |---|--- |---|--- |---|--- |---|
| QPCW-43 | CTM |Level|  Y |Y|38.0|20|36.22|1116.22|N|477|NaN|-999997.0|-999997.0| 17|7|5.0|-999997.0|NaN|

If the product is sold then `Sale` is Y otherwise it's N. Other variables are:


# Data cleaning

Initial inspection reveals the number of missing data are the same across some features . It's possible that some customers didn't provide these information when they requested quotation. Special characters and some odd numbers such as '-999997' and '9999' are also treated as missing values.
Summary of the missing values indicates they exist in nearly half of the features and takes up a large amount of data( 65.3% in 'X (Months same person on ER at current address)', 97.5% in 'ND (Months since last CCJ)'!). It's important to find appropriate ways to deal with these missing values so that the impact they have on the model can be minimized.

<img src="https://github.com/markyhu/Insurance_Sale_Prediction/blob/master/images/missing_data.png" width="300" />



# Exploratory data analysis

Initial inspection 


| QuoteRef| Channel | Product| Smoker| Joint?| Person1| Age | Term| TotalPremium|	GrossCommission|	Sale|	JF (Score)| WGB |X| EF|NOB|URB|LSB|BB|ND|
| --- |---| --- |---|--- |---|--- |---|--- |---|--- |---|--- |---|--- |---|--- |---|--- |---|
| QPCW-43 | CTM |Level|  Y |Y|38.0|20|36.22|1116.22|N|477|NaN|-999997.0|-999997.0| 17|7|5.0|-999997.0|NaN|





# Key findings
