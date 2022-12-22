# Dataset
The dataset contains ~2.7k customer quotation data for a life insurance product. An example of the customer quotation is given below. 

| QuoteRef| Channel | Product| Smoker| Joint?| Person1| Age | Term| TotalPremium|	GrossCommission|	Sale|	JF (Score)| WGB |X| EF|NOB|URB|LSB|BB|ND|
| --- |---| --- |---|--- |---|--- |---|--- |---|--- |---|--- |---|--- |---|--- |---|--- |---|
| QPCW-43 | CTM |Level|  Y |Y|38.0|20|36.22|1116.22|N|477|NaN|-999997.0|-999997.0| 17|7|5.0|-999997.0|NaN|

If the product is sold then `Sale` is Y otherwise it's N. Other variables are:


# Data cleaning

Initial inspection reveals the number of missing data are the same across some features . It's possible that some customers didn't provide these information when they requested quotation.

QuoteRef                                                    0
Channel                                                     0
Product                                                     0
Smoker                                                      1
Joint?                                                      0
Person1 Age                                                 1
Term                                                        0
TotalPremium                                                0
GrossCommission                                             0
Sale                                                        0
JF (Score)                                                  0
WGB (No. of other addresses held)                         825
X (Months same person on ER at current address)           715
EF (No. of people not same surname at current address)    715
NOB (Property group)                                      715
URB (Income group)                                        715
LSB (Regional banded house price band)                    715
BB (Number of CCJs)                                       715
ND (Months since last CCJ)                                825
dtype: int64




# Exploratory data analysis

Initial inspection 


| QuoteRef| Channel | Product| Smoker| Joint?| Person1| Age | Term| TotalPremium|	GrossCommission|	Sale|	JF (Score)| WGB |X| EF|NOB|URB|LSB|BB|ND|
| --- |---| --- |---|--- |---|--- |---|--- |---|--- |---|--- |---|--- |---|--- |---|--- |---|
| QPCW-43 | CTM |Level|  Y |Y|38.0|20|36.22|1116.22|N|477|NaN|-999997.0|-999997.0| 17|7|5.0|-999997.0|NaN|

