import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 



class datacleaner:
    def _init_(self,numerica_fill='mode', data_columns=None, z_thresh=3):
         self.numeric_fill=numeric_fill
         self.categorical_fill=categorical_fill
         self.date_columns=date_columns or []
         self.z_threshl=z_thresh
    
    

    def clean(self, df:pd.DataFrame) -> pd.DataFrame:
         df = self.numeric_fill(df)
         df = self.convert_dates(df)
         df = self.remove_outliers(df)
         return df
    
    def handle_missing(self, df:pd.DataFrame) -> pd.DataFrame:
         for col in df.select_dtypes(include=np.number).columns:
            if self.numeric_fill == "mean":
                df[col] =df[col].fillna(df[col].mean())
            elif self.numeric_fill == "median":
                df[col] =df[col].fillna(df[col].median())
            elif isinstance(self.numeric_fill, (int,float)):
                df[col]= df[col].fillna(self.numeric_fill)


         for col in df.select_dtypes(include=np.number).columns:
             if self.categorical_fill == "mode":
                 df[col]=df[col].fillna(df[col].mode())

             elif isinstance(self.categorical_fill, str):
                 df[col]= df[col].fillna(self.categorical_fill)

         return df
                 
    def convert_dates(self,df:pd.DataFrame) -> pd.DataFrame:
        for col in self.date_columns:
            if col in df.columns:
                df[col]=pd.to_datetime(df(col),errors ='coerce')
        return df
    def remove_outliers(self,df:pd.DataFrame) -> pd.DataFrame:
        numeric_cols = df.select_dtypes(include=np.number).columns:
        for col in numeric_cols:
            mean, std= df[col].mean(),df[col].std()
            z_score =(df[col]-mean)/std
            df = df[z_score.abs() <= self.z_thresh]
        return df
    

if _name_ = "__main__" :
df =pd.read_csv("")
cleaner = datacleaner(date_columns= ['joindate'])
clean_df =cleaner