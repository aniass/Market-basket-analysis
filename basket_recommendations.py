import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

MIN_SUPPORT_THRESHOLD = 0.07
MIN_ASSOCIATION_THRESHOLD = 1


def clean_data(df):
    '''Data preprocessing: delete missing data, fill missing values and feature engineering'''
    df['InvoiceNo'] = df['InvoiceNo'].astype('str')
    df = df[~df['InvoiceNo'].str.contains('C', na=False)]
    df = df.assign(
       CustomerID=df.CustomerID.fillna('00000'),
       Description=df.Description.fillna("Unkown"),
       Income=round(df['Quantity'] * df['UnitPrice'],2),
    )
    return df


def read_data(path):
    '''Read and preprocess data'''
    try:
        data = pd.read_csv(path, encoding='unicode_escape')
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return None
    df = clean_data(data)
    return df


def get_recommendations(df):
    '''Get product recommendations'''
    # Filter data for a specific country (Netherlands in this case)
    data = df[df['Country'] == 'Netherlands']
    
    # Prepare data for association rules
    basket = data.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().fillna(0)
    basket_model = basket.applymap(lambda x: 1 if x>0 else 0)
    
    # Compute frequent items using the Apriori algorithm
    popular_sets = apriori(basket_model, min_support=MIN_SUPPORT_THRESHOLD, use_colnames=True)
    
    # Compute association rules for frequent itemsets
    rules = association_rules(popular_sets,metric='lift',min_threshold=MIN_ASSOCIATION_THRESHOLD)
    
    # Extract product recommendations based on the "lift" measure
    products = rules.sort_values('lift', ascending=False)
    prod_rec = products[['antecedents', 'consequents']]
    
    #  Rename columns for better readability
    prod_rec = prod_rec.rename(columns={"antecedents": "Products", "consequents": "Recommendation"})
    
    # Save recommendations to a CSV file
    #prod_rec.to_csv('list_of_products.csv', index=False)
    print(prod_rec.head())
    
    # Print example recommendations
    prod_1 = products['antecedents'].iloc[1]
    prod_2 = products['consequents'].iloc[1]
    print(f'For product {prod_1} you can recommend product {prod_2}.')


def main():
    URL = r'Datasets\online_retail.csv'
    df = read_data(URL)
    get_recommendations(df)
    
    
if __name__ == '__main__':
    main()
