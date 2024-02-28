import pandas as pd

def clean_data():
    df = pd.read_csv('streamlit_dashboard/archive/all/spotify-2023.csv')

    df.dropna(subset=['in_shazam_charts'], inplace=True)
    df['in_shazam_charts'] = df['in_shazam_charts'].str.replace(',', '')
    df['in_shazam_charts'] = df['in_shazam_charts'].astype(int)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    return df
