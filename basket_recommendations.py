import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


URL = 'C:\Python Scripts\Datasets\online_retail.csv'


def clean_data(df):
    df['InvoiceNo'] = df['InvoiceNo'].astype('str')
    df = df[~df['InvoiceNo'].str.contains('C',na=False)]
    df = df.assign(CustomerID = df.CustomerID.fillna('00000'),
                   Description = df.Description.fillna("Unkown"),
                   Income = round(df['Quantity'] * df['UnitPrice'],2),)
    return df


def read_data(path):
    data = pd.read_csv(path, encoding = 'unicode_escape')
    df = clean_data(data)
    return df


def get_recommendations(df):
    data = df[df['Country'] == 'Netherlands']
    # preparing data
    basket = data.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().fillna(0)
    basket_model = basket.applymap(lambda x: 1 if x>0 else 0)
    # computing frequent items using the Apriori algorithm
    popular_sets = apriori(basket_model, min_support=0.07, use_colnames=True)
    # computing all association rules for popular sets
    rules = association_rules(popular_sets,metric='lift',min_threshold=1)
    # list of recommended products according to the “lift” measure
    products = rules.sort_values('lift', ascending=False)
    prod_rec = products[['antecedents', 'consequents']]
    # final Data Frame with products and recommendation columns
    prod_rec = prod_rec.rename(columns={"antecedents": "Products", "consequents": "Recommendation"})
    # save to csv
    prod_rec.to_csv('list_of_products.csv')
    print(prod_rec.head())
    
    # print example recommendations
    prod_1 = products['antecedents']
    prod_2 = products['consequents']
    print(f'For product {prod_1[1]} you can recommend product {prod_2[1]}.')


if __name__ == '__main__':
    df = read_data(URL)
    get_recommendations(df)
