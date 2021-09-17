from flask import Flask, render_template, request, redirect, url_for
from flask import request
import pandas as pd
import numpy as np
from app_utils import *

app = Flask("Test")

df = pd.read_csv('data/dataset_18-21_.csv',index_col=0)

df_pop = pd.read_csv("data/pop.csv", index_col=0)

# 1. 교육,의료시설 분야
df_park = pd.read_csv("data/park.csv", index_col=0)
df_edu = pd.read_csv("data/education.csv", index_col=0)
# df_doc = pd.read_csv("data/doc.csv", index_col=0)

# 2. 편의시설 분야
df_metro = pd.read_csv("data/metro.csv", index_col=0)
df_mac = pd.read_csv("data/mac.csv", index_col=0)
df_bucks = pd.read_csv("data/bucks.csv", index_col=0)
df_bank = pd.read_csv("data/bank.csv", index_col=0)

# 3. 범죄율 분야
df_cctv = pd.read_csv("data/cctv.csv", index_col=0)
df_crime = pd.read_csv("data/crime.csv", index_col=0)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detail/<city>')
def city_detail(city):
    datas, labels = find_average_detail(df, city)
    pop_datas = df_pop[df_pop['구별'] == city]
    park_datas = df_park[df_park['구별'] == city]
    crime_datas = df_crime[df_crime['구별'] == city]
    edu_datas = df_edu[df_edu["구별"] == city]
    total_datas,result_point= total_point(city)
    return render_template('detail.html', data=datas, labels=labels, title=city, pop_datas=pop_datas, park_datas=park_datas, crime_datas=crime_datas, edu_datas=edu_datas,total_datas=total_datas,result_point=result_point)


@app.route('/map')
def map():
    print(url_for("home"))
    return render_template('map.html')


@app.route('/chart')
def chart():
    data, labels = find_average(df)
    return render_template('chart.html', data=data, labels=labels)


if __name__ == "__main__":
    app.run(debug=True)
