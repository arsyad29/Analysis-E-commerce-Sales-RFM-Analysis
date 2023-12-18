# Import library
import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
import datetime as dt
import os


# Load data
tmp_merge_products_df = pd.read_csv('Dashboard/data/main_df.csv')
tmp_customer_locations_df = pd.read_csv('Dashbord/data/customer.csv')
tmp_seller_locations_df = pd.read_csv('Dashboard/data/seller.csv')
rfm = pd.read_csv('Dashboard/data/rfm.csv')

# Create function for call data into visualization

# Apply function

# Side Bar
# with st.sidebar:
#     st.header('Pertanyaan')
#     selected = option_menu(
#         options=["Pertanyaan 1"]
#     )
# if selected == "Pertanyaan 1":
    
    # app_mode = st.sidebar.selectbox( "Pilih Pertanyaan", [
	# 	"Pertanyaan 1",
	# 	"Pertanyaan 2",
	# 	"Pertanyaan 3",
	# 	"Pertanyaan 4",
	# 	"Pertanyaan 5",
	# 	"Pertanyaan 6",
    #     "Pertanyaan 7",
    #     "Pertanyaan 8",
    #     "Pertanyaan 9",
    #     "Pertanyaan 10",
    #     "Pertanyaan 11",
    #     "Pertanyaan 12",
	# ])

# nav
# if app_mode == "Pertanyaan 1": vis1


# Main page
st.title(os.listdir())
# st.title('Proyek Akhir')
st.markdown('##')
st.subheader("Nama: Muhammad Arsyad Ramadhan")
st.subheader("Email: arsyad351@gmail.com")
st.subheader("Id Dicoding: arsyad351")

# Vis 1
st.title('Pertanyaan 1. Bagaimana pendapatan perusahaan dalam setahun terakhir?')

# mid_columns = st.columns(1)
# with mid_columns:
tmp_merge_products_df['order_purchase_timestamp'] = pd.to_datetime(tmp_merge_products_df['order_purchase_timestamp'])
tmp_merge_products_2018_df = tmp_merge_products_df[tmp_merge_products_df['order_purchase_timestamp'].dt.year == 2018]
tmp_merge_products_2018_df['revenue_recent_months_2018'] = tmp_merge_products_2018_df['order_purchase_timestamp'].dt.month
tmp_company_revenue_2018 = tmp_merge_products_2018_df.groupby(['revenue_recent_months_2018']).agg({'product_id': 'count', 'price': 'sum'})

fig,ax = plt.subplots()
tmp_company_revenue_2018['price'].plot.line(ax=ax)

# annotate points in axis
for idx, row in tmp_company_revenue_2018.iterrows():
    ax.annotate(row['price'], (idx, row['price']), fontsize=8)

plt.title('Company revenu in recent months 2018')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
st.pyplot(fig)
st.text('Conclusion pertanyaan 1:\nPada bulan Maret s/d Mei perusahaan memiliki pendapatan yang sangat tinggi, namun \npada bulan Juni s/d Agustus memiliki penurunan yang drastis')
# End vis 1


# Vis 2
st.subheader('Pertanyaan 2: Bagaimana order status dari kategori produk?')

fig,ax = plt.subplots()
splot = tmp_merge_products_df['order_status'].value_counts(ascending=True).plot.bar(ax=ax)
for p in splot.patches:
    splot.annotate(format(p.get_height()/tmp_merge_products_df.shape[0], '.2%'),
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha = 'center',
                    va = 'center',
                    xytext = (0, 10),
                    textcoords = 'offset points')

# Setting Plot
sns.despine(right=True,top = True, left = True)
splot.axes.yaxis.set_visible(False)
plt.tight_layout()
st.pyplot(fig)
st.text('Conclusion pertanyaan 2:\nSebanyak 99.99% produk terkirim ke pelanggan, \ndan hanya 0.01% dari keseluruhan produk yang gagal terkirim')
# End vis 2

# Vis 3 & 4
st.subheader('Pertanyaan 3: Apa saja dan berapa banyak customer melakukan pembayaran berdasarkan tipe pembayaran?')
st.subheader('Pertanyaan 4: Berapa banyak angsuran dengan pembayaran menggunakan credit card?')

left_columns, right_columns = st.columns(2)
with left_columns:
    fig,ax = plt.subplots()
    # Count
    splot = tmp_merge_products_df['payment_type'].value_counts().plot.bar(ax=ax, figsize=(10, 10))
    for k in splot.patches:
        splot.annotate(format(k.get_height(), ',.0f'), # Getting annotate into thousand using format pacifier ,.0f
                        (k.get_x() + k.get_width() / 2., k.get_height()),
                        ha = 'center',
                        va = 'center',
                        xytext = (0, 10),
                        textcoords = 'offset points')
    # percentage
    for p in splot.patches:
        splot.annotate(format(p.get_height()/tmp_merge_products_df.shape[0], '.2%'),
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha = 'center',
                        va = 'center',
                        xytext = (0, 25),
                        textcoords = 'offset points')
    
    ax.set_title('Payments Type by products')
    plt.xticks(rotation=45)
    sns.despine(top=True, right=True)
    plt.tight_layout()
    st.pyplot(fig)

with right_columns:
    tmp_count_payment_installment_cc_df = tmp_merge_products_df[tmp_merge_products_df['payment_type'] == 'credit_card']

    fig,ax = plt.subplots()
    splot = tmp_count_payment_installment_cc_df['payment_installments'].value_counts().plot.bar(ax=ax, figsize=(10, 10))
    for k in splot.patches:
        splot.annotate(format(k.get_height(), ',.0f'), # Getting annotate into thousand using format pacifier ,.0f
                        (k.get_x() + k.get_width() / 2., k.get_height()),
                        ha = 'center',
                        va = 'center',
                        xytext = (0, 10),
                        textcoords = 'offset points',
                        fontsize=8)
    ax.set_title('Count payments installments credit card')
    plt.xticks(rotation=45)
    sns.despine(top=True, right=True)
    plt.tight_layout()
    st.pyplot(fig)
st.text('Conclusion pertanyaan 3 & 4:\nCustomer memiliki pembayaran terbanyak menggunakan credit card sebanyak 73%\ndan memiliki angsuran terbanyak hingga mencapai 24x pembayaran angsuran yang\nmenggunakan credit card')

# Vis 5
st.subheader('Pertanyaan 5: Kategori produk apa yang memiliki penjualan terbanyak?')

tmp_top5_category_merge_products_df = tmp_merge_products_df.groupby(['product_category_name_english']).agg({
                                                    'product_id': 'count'}).sort_values(by='product_id', ascending=False).head(5)

# Visualisasi
fig,ax = plt.subplots()
splot = tmp_top5_category_merge_products_df.sort_values(by='product_id', ascending=True).plot(kind='barh', figsize=(8, 5), ax=ax)
plt.title('Top 5 Selling by Category')
plt.xlabel('Count')
plt.ylabel('Category')
for c in splot.containers:
    # set the bar label
    splot.bar_label(c, fmt='%.0f', label_type='edge')
sns.despine(top=True, right=True)
plt.tight_layout()
st.pyplot(fig)
st.text('Conclusion pertanyaan 5: Kategori Bed_bath_table memiliki penjualan yang paling banyak \ndiantara semua produk, yaitu hingga 11rb')
# End Vis 5

# Vis 6
st.subheader('Pertanyaan 6: Barang apa yang memiliki biaya pengankutan yang mahal?')

tmp_top5_high_freight_value_df = tmp_merge_products_df.groupby(['product_category_name_english']).agg({
                                                    'freight_value': 'max'}).sort_values(by='freight_value', ascending=False).head(5)
fig,ax = plt.subplots()
splot = tmp_top5_high_freight_value_df.sort_values(by='freight_value', ascending=True).plot(kind='barh', figsize=(8, 5), ax=ax)
plt.title('Top 5 expensive product in Category by freight value')
plt.xlabel('Count')
plt.ylabel('Category')
for c in splot.containers:
    # set the bar label
    splot.bar_label(c, fmt='%.0f', label_type='edge')
sns.despine(top=True, right=True)
plt.tight_layout()
st.pyplot(fig)
st.text('Conclusion pertanyaan 6: Barang dengan kategori baby memiliki biaya pengangkutan yang paling mahal')
# End Vis 6

# Vis 7
st.subheader('Pertanyaan 7: Barang apa saja yang termahal dalam produk?')

tmp_aggr_merge_products= tmp_merge_products_df.groupby(['product_category_name_english']).agg({'price': ['min', 'max', 'mean']})

fig,ax = plt.subplots()
splot2 = tmp_aggr_merge_products[('price', 'max')].sort_values(ascending=False).head().plot.bar(color='#ff7675', figsize=(5,5), ax=ax)
for k in splot2.patches:
  splot2.annotate(format(k.get_height(), ',.0f'), # Getting annotate into thousand using format pacifier ,.0f
                  (k.get_x() + k.get_width() / 2., k.get_height()),
                  ha = 'center',
                  va = 'center',
                  xytext = (0, 10),
                  textcoords = 'offset points')
# plt.legend(['Average Income'])
plt.title('Top 5 Price Maximum By Categories')
plt.xticks(rotation=45)
sns.despine(top=True, right=True)
plt.tight_layout()
st.pyplot(fig)
st.text('Conclusion pertanyaan 7: Barang dengan kategori housewares merupakan barang dengan harga tertinggi')
# End Vis 7

# Vis 8
st.subheader('Pertanyaan 8: Bagaimana persentase review score dari masing-masing produk?')

fig,ax = plt.subplots()
days = tmp_merge_products_df.groupby('review_score').size()
sns.set()
days.plot(kind='pie', title='Count review score', figsize=[5,5],
          autopct=lambda p: '{:.2f}%({:.0f})'.format(p,(p/100)*days.sum()), fontsize=8, textprops={'color':"black"}, ax=ax)
st.pyplot(fig)
st.text('Conclusion pertanyaan 8: Rating 5 merupakan rating terbanyak diantar keseluruhan, yaitu hingga 57%')
# End Vis 8

# Vis 9
st.subheader('Pertanyaan 9: Bagaimana pengeluaran customer yang melakukan pembayaran dari masing-masing tipe pembayaran?')

fig,ax = plt.subplots()

tmp_aggr_payments_products= tmp_merge_products_df.groupby(['payment_type']).agg({'payment_value': ['min', 'max', 'mean']})
splot2 = tmp_aggr_payments_products[('payment_value', 'max')].sort_values(ascending=False).plot.bar(color='#ff7675', figsize=(5,5), ax =ax)
for k in splot2.patches:
  splot2.annotate(format(k.get_height(), ',.0f'), # Getting annotate into thousand using format pacifier ,.0f
                  (k.get_x() + k.get_width() / 2., k.get_height()),
                  ha = 'center',
                  va = 'center',
                  xytext = (0, 10),
                  textcoords = 'offset points')
# plt.legend(['Average Income'])
plt.title('Max payment value of payment type')
plt.xticks(rotation=45)
sns.despine(top=True, right=True)
plt.tight_layout()
st.pyplot(fig)

st.text('Conclusion pertanyaan 9: Credit card merupakan tipe pembayaran dengan \nangsuran pembayaran paling tinggi')
# End Vis 9

# Vis 10
st.subheader('Pertanyaan 10: Bagaimana pengeluaran rata-rata customer berdasarkan kota customer?')
top5_customer_byprice_df = tmp_customer_locations_df.groupby(['customer_city']).agg({
    'price': 'mean'}).sort_values(by='price', ascending=False).head()

fig, ax = plt.subplots()
splot2 = top5_customer_byprice_df.sort_values(by='price', ascending=True).plot.bar(color='#ff7675', ax=ax)
for k in splot2.patches:
  splot2.annotate(format(k.get_height(), ',.0f'), # Getting annotate into thousand using format pacifier ,.0f
                  (k.get_x() + k.get_width() / 2., k.get_height()),
                  ha = 'center',
                  va = 'center',
                  xytext = (0, 10),
                  textcoords = 'offset points')
# plt.legend(['Average Income'])
plt.title('Top 5 average price by Customer City')
plt.xticks(rotation=45)
sns.despine(top=True, right=True)
plt.tight_layout()
st.pyplot(fig)

st.text('Conclusion pertanyaan 10: Customer dengan kota pianco merupakan customer \ndengan melakukan pembelian dengan rata-rata tertinggi, yaitu hingga 2.200 USD')
# End Vis 10

# Vis 11
st.subheader('Pertanyaan 11: Dari kota dan negara mana customer dengan pembelian terbanyak?')
tmp_top5_product_bycustomers_df = tmp_customer_locations_df.groupby(['customer_city']).agg({
                                  'product_id':'count'}).sort_values(by='product_id', ascending=False).head()

fig,ax = plt.subplots(1,2)
splot = tmp_top5_product_bycustomers_df.sort_values(by='product_id', ascending=True).plot(kind='barh', ax=ax[0], figsize=(10,5))
ax[0].set_title('Top 5 City by customer buying products')
plt.xlabel('Count')
plt.ylabel('Category')
for c in splot.containers:
    # set the bar label
    splot.bar_label(c, fmt='%.0f', label_type='edge')
sns.despine(top=True, right=True)

tmp_top5_product_bycustomers_df = tmp_customer_locations_df.groupby(['customer_state']).agg({
                                  'product_id':'count'}).sort_values(by='product_id', ascending=False).head()

splot = tmp_top5_product_bycustomers_df.sort_values(by='product_id', ascending=True).plot(kind='barh', ax=ax[1], figsize=(10,5))
ax[1].set_title('Top 5 State by customer buying products')
plt.xlabel('Count')
plt.ylabel('Category')
for c in splot.containers:
    # set the bar label
    splot.bar_label(c, fmt='%.0f', label_type='edge')
sns.despine(top=True, right=True)
plt.tight_layout()
st.pyplot(fig)

st.text('Conclusion pertanyaan 11: Kota Sao paulo dan negara SP \nmerupakan customer terbanyak yang melakukan pembelian pada perusahaan ini')
# End Vis 11

# Vis 12
st.subheader('Pertanyaan 12: Dari kota dan negara mana seller melakukan penjualan terbanyak?')
# dari mana seller dengan penjualan terbanyak?
fig,ax = plt.subplots(1,2)
tmp_top5_product_bycustomers_df = tmp_seller_locations_df.groupby(['seller_city']).agg({
                                  'product_id':'count'}).sort_values(by='product_id', ascending=False).head()

splot = tmp_top5_product_bycustomers_df.sort_values(by='product_id', ascending=True).plot(kind='barh', ax=ax[0], figsize=(10,5))
ax[0].set_title('Top 5 City by Seller selling products')
plt.xlabel('Count')
plt.ylabel('Category')
for c in splot.containers:
    # set the bar label
    splot.bar_label(c, fmt='%.0f', label_type='edge')
sns.despine(top=True, right=True)
# plt.tight_layout()
# plt.show()

tmp_top5_product_bycustomers_df = tmp_seller_locations_df.groupby(['seller_state']).agg({
                                  'product_id':'count'}).sort_values(by='product_id', ascending=False).head()

splot = tmp_top5_product_bycustomers_df.sort_values(by='product_id', ascending=True).plot(kind='barh', ax=ax[1], figsize=(10,5))
ax[1].set_title('Top 5 State by seller selling products')
plt.xlabel('Count')
plt.ylabel('Category')
for c in splot.containers:
    # set the bar label
    splot.bar_label(c, fmt='%.0f', label_type='edge')
sns.despine(top=True, right=True)
plt.tight_layout()
st.pyplot(fig)

st.text('Conclusion pertanyaan 12: Kota Sao paulo dan negara SP \nmerupakan seller terbanyak yang melakukan penjualan produk dari perusahaan ini')
# End Vis 12


# Vis RFM

st.subheader('Best RFM Customer Parameters')

# Find aggregation
Best_of_customers = rfm[rfm['Cluster'] == 1]
average_recency = round(Best_of_customers['Recency'].mean(),2)
average_frequency = round(Best_of_customers['Frequency'].mean(),2)
average_monetary = round(Best_of_customers['Monetary'].mean(),2)

left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.metric('Average of Recency: ', value=average_recency)
with middle_column:
    st.metric('Average of Frequency: ', value=average_frequency)
with right_column:
    st.metric('Average of Monetary: ', value=average_monetary)

cluster_1 = rfm[rfm['Cluster'] == 1]
cluster_1['Customer_id'] = cluster_1.index
fig,ax = plt.subplots(1,3)
cluster_1.groupby(['Customer_id']).agg({'Recency':'max'}).head().sort_values(by='Recency', ascending=False).plot.bar(ax=ax[0])
cluster_1.groupby(['Customer_id']).agg({'Frequency':'max'}).head().sort_values(by='Frequency', ascending=False).plot.bar(ax=ax[1])
cluster_1.groupby(['Customer_id']).agg({'Monetary':'max'}).head().sort_values(by='Monetary', ascending=False).plot.bar(ax=ax[2])
plt.tight_layout()
st.pyplot(fig)
