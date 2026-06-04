import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder

st.set_page_config(page_title="FinTrack Dashboard", layout="wide")
st.title("Dashboard Analisis Finansial Mahasiswa")
st.write("")

# load data dan data cleaning
@st.cache_data
def load_and_preprocess_data():
    df = pd.read_excel('Student_Spending_Habit.xlsx')
    
    # standardisasi teks
    kolom_teks = ['gender', 'year_in_school', 'major', 'preferred_payment_method']
    for col in kolom_teks:
        df[col] = df[col].astype(str).str.lower().str.strip()
        
    # perbaiki singkatan dan format umur
    df.loc[df['age'] < 15, 'age'] = np.nan
    df['gender'] = df['gender'].replace({'f': 'female', 'm': 'male', 'nb': 'non-binary'})
        
    # hapus duplikat
    df = df.drop_duplicates()
    
    # split data
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    
    # handling missing value dan data minus pada data train
    train_df['age'] = train_df['age'].fillna(train_df['age'].median()).astype(int)
    train_df['monthly_income'] = train_df['monthly_income'].fillna(train_df['monthly_income'].median())
    train_df['major'] = train_df['major'].replace('nan', 'unknown')
    train_df['preferred_payment_method'] = train_df['preferred_payment_method'].replace('nan', 'unknown')
    
    kolom_keuangan = ['monthly_income', 'financial_aid', 'tuition', 'housing', 'food', 
                      'transportation', 'books_supplies', 'entertainment', 'personal_care', 
                      'technology', 'health_wellness', 'miscellaneous']
    for col in kolom_keuangan:
        train_df[col] = train_df[col].abs()
        
    # handling outliers
    def remove_outliers_iqr(data, column):
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        return data[(data[column] >= Q1 - 1.5 * IQR) & (data[column] <= Q3 + 1.5 * IQR)]
        
    train_df = remove_outliers_iqr(train_df, 'monthly_income')
    train_df = remove_outliers_iqr(train_df, 'tuition')
    train_df = remove_outliers_iqr(train_df, 'age')
    
    # feature engineering
    kategori_pengeluaran = ['housing', 'food', 'transportation', 'books_supplies',
                            'entertainment', 'personal_care', 'technology',
                            'health_wellness', 'miscellaneous']
    train_df['total_spending'] = train_df[kategori_pengeluaran].sum(axis=1)
    train_df['saving_ratio'] = np.where(train_df['monthly_income'] > 0, 
                                        (train_df['monthly_income'] - train_df['total_spending']) / train_df['monthly_income'], 
                                        0)
                                        
    train_df['spending_level'] = pd.qcut(train_df['total_spending'], q=3, labels=['low', 'medium', 'high'])
    
    return train_df, kategori_pengeluaran

train_df, kategori_pengeluaran = load_and_preprocess_data()

# membuat sidebar untuk filter data
st.sidebar.header("Filter Data")

gender_display = [g.title() for g in train_df['gender'].unique()]
selected_gender_display = st.sidebar.multiselect("Gender", options=gender_display, default=gender_display)
selected_gender = [g.lower() for g in selected_gender_display]

year_options = train_df['year_in_school'].unique()
selected_year = st.sidebar.multiselect("Tahun Kuliah", options=year_options, default=year_options)

df_filtered = train_df[(train_df['gender'].isin(selected_gender)) & (train_df['year_in_school'].isin(selected_year))]

# visualisasi data
if df_filtered.empty:
    st.error("Data tidak ditemukan berdasarkan filter yang Anda pilih.")
else:
    sns.set_theme(style="whitegrid")
    
    # baris 1
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Kategori Pengeluaran Tertinggi**")
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        rata_pengeluaran = df_filtered[kategori_pengeluaran].mean().sort_values(ascending=False)
        sns.barplot(x=rata_pengeluaran.values, y=rata_pengeluaran.index, hue=rata_pengeluaran.index, palette='magma', legend=False, ax=ax1)
        ax1.set_xlabel('Rata-rata Nominal ($)')
        st.pyplot(fig1)
        st.info("**Insight:** Kategori pengeluaran terbesar mahasiswa berada pada housing, kemudian diikuti oleh food, technology, dan books_supplies. Hal ini menunjukkan bahwa kebutuhan tempat tinggal dan kebutuhan akademik masih menjadi prioritas utama pengeluaran mahasiswa.")

    with col2:
        st.markdown("**Metode Pembayaran Pilihan Mahasiswa**")
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.countplot(data=df_filtered, x='preferred_payment_method', hue='preferred_payment_method', palette='Set2', legend=False, order=df_filtered['preferred_payment_method'].value_counts().index, ax=ax2)
        ax2.set_xlabel('Metode Pembayaran')
        ax2.set_ylabel('Jumlah Mahasiswa')
        plt.xticks(rotation=15)
        st.pyplot(fig2)
        st.info("**Insight:** Metode pembayaran yang paling banyak digunakan mahasiswa adalah mobile payment app, diikuti oleh credit/debit card dan cash. Hal ini menunjukkan bahwa sebagian besar mahasiswa sudah terbiasa menggunakan transaksi digital dibanding pembayaran tunai.")

    st.write("") 

    # baris 2
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("**Pola Pengeluaran via Metode Pembayaran**")
        fig3, ax3 = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=df_filtered, x='preferred_payment_method', y='total_spending', hue='preferred_payment_method', palette='Set2', legend=False, ax=ax3)
        ax3.set_xlabel('Metode Pembayaran')
        ax3.set_ylabel('Total Pengeluaran ($)')
        plt.xticks(rotation=15)
        st.pyplot(fig3)
        st.info("**Insight:** Boxplot pola pengeluaran berdasarkan metode pembayaran menunjukkan bahwa seluruh metode pembayaran memiliki median pengeluaran yang relatif mirip. Namun, pengguna credit/debit card dan mobile payment app cenderung memiliki variasi pengeluaran yang sedikit lebih besar dibanding pengguna cash.")

    with col4:
        st.markdown("**Korelasi Pemasukan vs Total Pengeluaran**")
        fig4, ax4 = plt.subplots(figsize=(8, 5))
        sns.scatterplot(data=df_filtered, x='monthly_income', y='total_spending', alpha=0.6, color='teal', ax=ax4)
        ax4.set_xlabel('Pemasukan Bulanan ($)')
        ax4.set_ylabel('Total Pengeluaran ($)')
        st.pyplot(fig4)
        st.info("**Insight:** Scatterplot antara monthly_income dan total_spending menunjukkan bahwa tidak terdapat hubungan linear yang terlalu kuat antara pemasukan dan total pengeluaran. Mahasiswa dengan pemasukan tinggi tidak selalu memiliki pengeluaran yang lebih besar karena pola pengeluaran tiap mahasiswa cukup beragam. Sebaran titik pada scatterplot terlihat cukup menyebar pada seluruh rentang pemasukan. Hal ini menunjukkan adanya variasi perilaku finansial mahasiswa dalam mengelola pendapatan dan pengeluaran mereka.")

    st.write("") 

    # baris 3
    col5, col6 = st.columns(2)
    
    with col5:
        st.markdown("**Distribusi Biaya Kuliah (Tuition)**")
        fig5, ax5 = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=df_filtered, x='tuition', color='lightcoral', ax=ax5)
        ax5.set_xlabel('Biaya Kuliah ($)')
        st.pyplot(fig5)
        st.info("**Insight:** Visualisasi distribusi tuition menunjukkan bahwa biaya kuliah mahasiswa berada pada rentang sekitar 3000 hingga 6000 dengan median berada di sekitar 4500. Sebaran data terlihat cukup stabil tanpa adanya outlier yang signifikan setelah proses preprocessing dilakukan.")
        
   