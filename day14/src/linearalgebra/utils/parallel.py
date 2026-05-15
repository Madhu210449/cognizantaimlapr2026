#create tax calculator function for products in products.csv using parallel processing
from multiprocessing import Pool
from time import time

import pandas as pd
from linearalgebra.configurations.conf import Config

def sequential_tax_calculator(product_path):
    #read products.csv
    products = pd.read_csv(product_path)
    start_time = time.time()
    products['tax'] = products['cost'] * 0.1
    end_time = time.time()
    print(f"Time taken for sequential tax calculation: {end_time - start_time} seconds")
    return products
def parallel_tax_calculator(product_path):
    #read products.csv
    #with pool of 8 processes, calculate tax for each product in products.csv and add it as a new column to the dataframe
    products = pd.read_csv(product_path)
    start_time = time.time()
    with Pool(8) as p:
        products['tax'] = p.map(lambda x: x * 0.1, products['cost'])
    end_time = time.time()
    print(f"Time taken for parallel tax calculation: {end_time - start_time} seconds")
    return products


if __name__ == "__main__":
    #read products.csv
    product_path=Config.product_path
    products = sequential_tax_calculator(product_path)
    print(products)