import pandas as pd
from langchain_core.documents import Document

class data_converter:
    def __init__(self):
        print("Data transformation class has initialized")
        
        self.product_data = pd.read_csv(r"data/flipkart_product_review.csv")
        #print(self.product_data.head())

    def data_transformation(self):
        requried_columns = self.product_data.columns
        requried_columns = list(requried_columns[1:])
        # print(requried_columns)

        product_list = []

        for index,row in self.product_data.iterrows():
            obj = {
                "product_name" : row['product_title'],
                "product_rating" : row['rating'],
                "product_summary" : row['summary'],
                "product_review" : row['review'] 
            }
            product_list.append(obj)

        # print("*****************Below is product list******************")
        # print(product_list[0])

        docs = []
        for entry in product_list:
            metadata = {
                "product_name" : entry["product_name"],
                "product_rating" : entry["product_rating"],
                "product_summary" : entry["product_summary"]
                }
            doc = Document(page_content=entry["product_review"], metadata=metadata)
            docs.append(doc)
        # print(docs[0])
        return docs


if __name__ == '__main__':
    data_convert = data_convert()
    data_convert.data_transformation()