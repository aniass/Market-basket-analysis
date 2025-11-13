# Market Basket Analysis

## Market Basket Analysis and Product Recommendation

### General info
The aim of the project was market basket analysis and data-driven product recommendations. The project includes EDA analysis and Apriori algorithm was used to detect associations between products which is commonly used in associative analysis. Based on the results the most common product are frequently purchased together were identified. Finally the  recommendation model was built that can support marketing and sales decisions.

#### Dataset
The dataset comes from UCI data collection 'Online Retail' and can be found at [Kaggle](https://www.kaggle.com/puneetbhaya/online-retail). The data contain all the transactions occurring between 01/12/2010 and 09/12/2011 for a store online retail. The company mainly sells unique all-occasion gifts an many customers of the company are wholesalers.

### Motivation
Market basket analysis is a technique that allow to discover the relatonships between products. It is based on searching for the most common combination of products in each transaction.  Each transaction consist from n number of products and it is called as basket. There are looking for of such transactions that occurs frequently with each other. The basket analysis would allow the company to better target its promotional offers and personalize product recommendations for customers.

### Project contains:
- Market basket analysis by using the Apriori algorithm  - **Basket_analysis.ipynb** 
- Python script with basket recommendations - **basket_recommendations.py**
- data - data used in the project.

### Technologies
The project is created with:
- Python 3.6
- libraries: MLxtend, pandas, numpy, matplotlib.

To run this project use Jupyter Notebook or Google Colab.
You can run the script in the terminal:

    basket_recommendations.py
