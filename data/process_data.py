import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    ''' 
    Load the data from the input files
    Args:
        messages_filepath  message file
        categories_filepath  categories file
    Return:
        dataframe containing the raw data
    '''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on='id')
    
    return df

def clean_data(df):
    '''
    clean the dataframe
    
    Args:
        df dataframe to be cleaned
    
    Return:
        cleaned data frame
    '''
    categories = df["categories"].str.split(pat=';', expand=True)
    row = categories.iloc[1]
    category_colnames = [ row_value.split('-')[0] for row_value in row.values ]
    categories.columns = category_colnames
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1:]
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
        
    df.drop(["categories"], axis=1, inplace=True)
    df = pd.concat([df,categories], join='inner', axis=1 )
    df.drop_duplicates(inplace=True)
    
    return df
    
def save_data(df, database_filename):
    '''
    Save the dataframe to the sqlite database
    Args:
        df cleaned dataframe
        database_filename filename to save the data
    
    '''
    engine = create_engine('sqlite:///'+database_filename)
    df.to_sql('cleaned_table', engine, index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()