import pandas as pd
import numpy as np

# 1. 교육,의료 분야
df_park = pd.read_csv("data/park.csv", index_col=0)
df_edu = pd.read_csv("data/eduPoint.csv", index_col=0)
df_doc = pd.read_csv("data/docPerPop.csv", index_col=0)

# 2. 편의시설 분야
df_metro = pd.read_csv("data/metro.csv", index_col=0)
df_bucks = pd.read_csv("data/bucks.csv", index_col=0)
df_mac = pd.read_csv("data/mac.csv", index_col=0)
df_bank = pd.read_csv("data/bank.csv", index_col=0)

# 3. 범죄율 분야
df_crime = pd.read_csv("data/crimePoint.csv",index_col=0)
df_cctv = pd.read_csv("data/cctvPoint.csv",index_col=0)

# 4. 집값 
df_price = pd.read_csv("data/priceLand.csv",index_col=0)


def find_average(df):
    datas = []
    labels = []
    depo_list = df['구별'].unique()
    for i in depo_list:
        data = round(df[df['구별'] == i]['면적당가격'].sum() /
                     df[df['구별'] == i].shape[0])
        label = i
        datas.append(data)
        labels.append(label)
    return datas, labels


def find_average_detail(df, city):
    df_no = df[df['구별'].str.contains(city)].reset_index()
    df_no = df_no.drop('index', axis=1)
    datas = []
    labels = []
    df_list = df['계약년월'].unique()
    for i in df_list:

        tar = df_no[df_no['계약년월'] == i]
        data = round(tar['면적당가격'].sum()/tar.shape[0])
        labels.append(i)
        datas.append(data)
    return datas, labels


def sum_content(df, city):
    data = df[df['구별'] == city].shape[0]
    return data


def pop_content(df, city):
    datas = list(df[df['구별'] == city]['인구'].str.replace(
        ",", "").astype(int).values)
    labels = df[df['구별'] == city]['기간']
    return datas, labels


def doc_per_pop(doc, pop, city):
    # return [City,Value]  ===> Matrix list
    doc['기간'] = doc['기간'].astype(str)
    years = np.sort(doc['기간'].unique())
    # cities = np.sort(doc['구별'].unique()) --> 데이터를 로드시에 처리해서 관리 or 함수로 관리 정해야함
    li = []
    for year in years:
        df_doc = doc[doc['구별'] == city]
        doc_value = df_doc[df_doc['기간'] == str(year)]["계"].values
        te = pop[pop["기간"].str.contains(str(year))]
        pop_value = te[te['구별'] == str(city)]['인구'].mean()
        result = round((doc_value[0]/pop_value) * 100, 2)
        li.append([city, result])

    li = pd.DataFrame(li)
    ta = li[2].max()
    re = []
    for city, x in zip(li[1].values, li[2].values):
        result = (x/ta)*10
        re.append([city, round(result, 2)])
    r = pd.DataFrame(re)
    return r


def total_point(city):
    park = df_park[df_park['구별'] == city]['총점'].mean()
    kin,ele,mid,hei = df_edu[df_edu['구별']==city]['유아'].values,df_edu[df_edu['구별']==city]['초등'].values,df_edu[df_edu['구별']==city]['중등'].values,df_edu[df_edu['구별']==city]['고등'].values
    doc = df_doc[df_doc['구별']==city]['합계'].mean()
    edu_doc = np.round(park+kin+ele+mid+hei+doc,2)

    metro = df_metro[df_metro['구별']==city]['총점'].values
    bucks = df_bucks[df_bucks['구별']==city]['총점'].values
    mac = df_mac[df_mac['구별']==city]['총점'].values
    bank = df_bank[df_bank['구별']==city]['총점'].values
    conven = np.round(metro+bucks+mac+bank,2)

    crime = df_crime[df_crime['구별']==city]['총점'].values
    cctv = df_cctv[df_cctv['구별']==city]['총점'].values
    cri = np.round(crime+cctv,2)

    price = np.round(df_price[df_price['구별']==city]['총점'].values,2)

    result_point = np.round(edu_doc[0]+conven[0]+cri[0]+price[0],2)
    return [edu_doc[0],conven[0],cri[0],price[0]],result_point

# <script src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.5.0/chart.min.js'></script>
