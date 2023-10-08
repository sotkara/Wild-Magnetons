import pandas as pd

df_arr = []
df_arr_filtered = []
perc_months = []
avg_month_perc = []
month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
years = 6

#load files as dataframes
print("Loading files . . .")
for i in range(2016,2019):
    df_arr.append(pd.read_csv(f"dscovr_data_{i}.txt", delim_whitespace=True))
for i in range(2016,2019):
    df_arr.append(pd.read_csv(f"wind_data_{i}.txt", delim_whitespace=True))
# cleanup data and filter
print("Cleaning up data and filtering desired values . . .")
for df in df_arr:
    df = df.drop(df[df['field'] == 99999.9].index)
    df_arr_filtered.append(df.loc[df['field'] <= -9])

#Calculate month averages each year
print("Calculating averages . . .")
for i in range(0,years):
    df = df_arr[i]
    df_filtered = df_arr_filtered[i]
    month_perc = []

    for month in range(0,360,30):
        month_count = len(df[(df["doy"]>month) & (df["doy"] <=month+30)]) 
        filtered_month_count = len(df_filtered[(df_filtered["doy"]>month) & (df_filtered["doy"] <=month+30)])
        perc = filtered_month_count/month_count
        month_perc.append(perc)
    perc_months.append(month_perc)

#calculate the average monthly values using the average of the correspoding month of all years
for j in range(0,12):
    sum = 0
    for i in range(0,years):
        sum += perc_months[i][j]
    perc_perc = sum/3
    avg_month_perc.append(perc_perc) 
for i in range(0,12):
    print(f"{month_names[i]}: ", round(avg_month_perc[i]*100,2),"%")