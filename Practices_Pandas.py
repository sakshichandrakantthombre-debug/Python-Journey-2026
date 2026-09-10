#!/usr/bin/env python
# coding: utf-8

# # Pandas_Operation_Practices

# #  02/09/2026

# # DataFrames

# In[426]:


import pandas as pd


# In[427]:


pd.DataFrame
pd.DataFrame


# In[428]:


emp_data = {
    "ids":[101,102,103,104,105],
    "name":["Suman","Raman","Thaman","Baman","Naman"],
    "salary":[25000,35000,55000,12000,34000],
    "dept":["IT","Sales","Marketting","BPO","IT"]
}


# In[429]:


emp_data


# In[430]:


type(emp_data)


# In[431]:


emp_data.items()


# In[432]:


emp_data.keys()


# In[433]:


df=pd.DataFrame(emp_data)


# In[434]:


df


# In[435]:


stu={"stu_id":[1,2,3,4,5],
    "stu_name":["vijay","raj","raju","aanand","abhi"],
    "dept_name":["DS","CS","IT","Mech","ENTC"]}


# In[436]:


stu


# In[437]:


stu_df=pd.DataFrame(stu)
stu_df


# In[438]:


df


# In[439]:


df.shape


# In[440]:


df.shape[1]


# In[441]:


df.shape[0]


# In[442]:


stu_df.shape


# In[443]:


stu_df.shape[1]


# In[444]:


df.info()


# In[445]:


df.info()


# In[446]:


stu_df.info()


# In[447]:


df.index


# In[448]:


stu_df.index


# In[449]:


df.columns


# In[450]:


stu_df.columns


# In[451]:


df.columns=["id1","name1","salary1","dept1"]


# In[452]:


df


# In[453]:


df.index=[100,101,102,103,104]


# In[454]:


df


# In[455]:


stu_df


# # DataFrame From  a List!!

# In[456]:


ids= [101, 102, 103, 104, 105]
name= ['Suman', 'Raman', 'Thaman', 'Baman', 'Naman']
salary= [25000, 35000, 55000, 12000, 34000]
dept= ['IT', 'Sales', 'Marketting', 'BPO', 'IT']


# In[457]:


type(name)
type(salary)
type(ids)


# In[458]:


df2=pd.DataFrame([ids,name,salary,dept])


# In[459]:


df2


# In[460]:


df2=pd.DataFrame([ids,name,salary,dept]).T
df2


# In[461]:


df2.columns=["ids","name","salary","dept"]


# In[462]:


df2


# In[463]:


df2.columns=["ids","name","salary","dept"]


# In[464]:


df2


# In[465]:


stu_1=[1,2,3]
stu_name=["vj","az","abhi"]
marks=[45,46,47]


# In[466]:


stu_df2=pd.DataFrame([stu_1,stu_name,marks]).T


# In[467]:


stu_df2


# In[468]:


stu_df2.columns=["stu_id","name","marks"]


# In[469]:


stu_df2


# In[470]:


id1 = [101,"suman",35000,"IT"]
id2 = [102,"raman",56000,"Sales"]
id3 = [103,"suman",80000,"marketting"]
id4 = [104,"baman",90000,"bpo"]


# In[471]:


a=pd.DataFrame([id1,id2,id3,id4],columns=["ids","name","salary","dept"])
a


# In[472]:


a.info()


# In[ ]:





# In[473]:


st=pd.read_csv(r"C:\Users\user\Downloads\50_Startups.csv")
st


# In[474]:


st.shape


# In[475]:


st.index


# In[476]:


st.info()


# In[477]:


st.columns


# In[478]:


st.head()


# # Read of CSV file

# In[479]:


import pandas as pd


# In[480]:


pd.read_csv(r"C:\Users\user\Downloads\Cars93.csv")


# In[481]:


car=pd.read_csv(r"C:\Users\user\Downloads\Cars93.csv")


# In[482]:


car


# In[483]:


car.info()


# In[484]:


car.columns


# In[485]:


car.shape


# In[486]:


car.index


# In[487]:


from warnings import filterwarnings
filterwarnings ("ignore")


# In[488]:


st.RND


# In[489]:


st[["RND"]].head()


# In[490]:


st[["RND"]].tail()


# In[491]:


st[["RND","PROFIT"]].head()


# In[492]:


st.head(1)


# # Subsetting

# In[493]:


st[["RND","MKT"]].head()


# In[494]:


st[0:12]


# In[495]:


st[0:-12][["STATE","PROFIT"]]


# In[496]:


st[8:12][["RND","PROFIT","STATE"]]


# In[497]:


st.loc[[2,4],["STATE","PROFIT"]]


# In[498]:


st.loc[[2,4],["STATE","PROFIT"]]


# In[499]:


df.iloc[3:5,2:]


# In[500]:


car.columns


# In[501]:


car.info()


# In[502]:


car.head()


# In[503]:


car.tail()


# In[504]:


car.index


# In[505]:


car.info()


# In[506]:


car.isnull().sum()


# In[507]:


car.isnull().sum()[car.isnull().sum()>0]


# In[508]:


car.columns


# # find out cars with mileage between 10 and 25 on highway

# In[509]:


car["MPG.highway"]


# In[510]:


f1=(car["MPG.highway"]>10) & (car["MPG.highway"]>25)


# In[511]:


car[f1]


# In[512]:


car[f1][["MPG.highway","Manufacturer"]]


# In[513]:


car.head(1)


# # Find out cars whose price is greater than 40

# In[514]:


a=car["Price"]>40


# In[515]:


a


# In[516]:


car[a]


# In[517]:


car["Price"].min()


# In[518]:


car["Price"].max()


# In[519]:


car["Price"].describe()


# # Find out car details whose manufacturer is infiniti

# In[520]:


car["Manufacturer"].unique()


# In[521]:


car[car["Manufacturer"]=="Infiniti"]


# # Find out models whose type belongs to Compact Size.

# In[522]:


car["Type"].unique()


# In[523]:


car[car["Type"]=="Compact"]


# In[524]:


car["Price"].nunique()


# # Find out cars which belong to sport type and are priced more than 25

# In[525]:


car["Type"].unique()


# In[526]:


a=(car["Type"]=="Sporty") & (car["Price"]>25)


# In[527]:


car[a]


# # Finf out cars which provided aribags to driver and passanger. Display manufacture, module anad in output.

# In[528]:


car["AirBags"].unique()


# In[529]:


car[car["AirBags"]=="Driver & Passenger"]


# # Find out cars whose luggage room > 15

# In[530]:


car.columns


# In[531]:


car["Luggage.room"].unique()


# In[532]:


car[car["Luggage.room"]>15][["Luggage.room","Manufacturer","Type"]]


# In[533]:


car.sort_values(by="Price",ascending=False)[["Price","Manufacturer"]]


# In[534]:


st.info()


# In[535]:


st[["RND"]]


# In[536]:


st[["RND"]].head()


# In[537]:


st[["PROFIT"]].tail()


# In[538]:


st[["RND","PROFIT"]].head()


# # Dataframing filtering

# In[539]:


st["PROFIT"].tail().min()


# In[540]:


st["PROFIT"].head().max()


# In[541]:


st["PROFIT"].head(20).max()


# In[542]:


st["PROFIT"].max()


# In[543]:


st["PROFIT"].min()


# In[544]:


a=st["PROFIT"]>150000
a


# In[545]:


st[a]


# # Showcase startups information whose profit >100000 and <175000

# In[546]:


v=(st["PROFIT"]>100000) & (st["PROFIT"]<175000)


# In[547]:


v


# In[548]:


st.head(3)


# # Find out those companies who have PROFIT more than 1.5L and are from Florida
# 

# In[549]:


z=st["PROFIT"]>150000
x=st["STATE"]=="Florida"


# In[550]:


st[z & x]


# In[551]:


a=(st["PROFIT"]>150000) & (st["STATE"]=="Florida")


# In[552]:


a


# In[553]:


type(st["STATE"])


# In[554]:


type(st)


# # Find out Data for those companies who have PROFIT between 1 to 1.5L and which are from california or florida
# 

# In[555]:


a=(st["PROFIT"]>100000) &(st["PROFIT"]<150000)
b=(st["STATE"]=="California") | (st["STATE"]=="Florida")


# In[556]:


st[a & b]


# In[557]:


car.shape


# In[558]:


car.isnull().sum()


# In[559]:


car.isnull().sum()[car.isnull().sum()>0]


# # Find out cars with mileage between 10 and 25 on highway

# In[560]:


car["MPG.highway"]


# In[561]:


f1=(car["MPG.highway"]>10) & (car["MPG.highway"]<25)


# In[562]:


f1


# In[563]:


car[f1][["MPG.highway","Manufacturer"]]


# In[564]:


car.head(1)


# # Find out cars whose price is greater than 40
# 

# In[565]:


a=car["Price"]>40


# In[566]:


a


# In[567]:


car[a]


# In[568]:


car["Price"].min()


# In[569]:


car["Price"].max()


# In[570]:


car["Price"].describe()


# # Find out car details whose manufacturer is Infiniti
# 

# In[571]:


car["Manufacturer"].unique()


# In[572]:


car[car["Manufacturer"]=="Infiniti"]


# # Find out models whose type belongs to Compact size
# 

# In[573]:


car["Type"].unique()


# In[574]:


car[car["Type"]=="Compact"]


# In[575]:


car["Price"].nunique()


# # FInd out cars which belong to sport type and are priced more than 25

# In[576]:


car["Type"].unique()


# In[577]:


a=(car["Type"]=="Sporty") & (car["Price"]>25)


# In[578]:


a


# # Find out cars which provide aribags to driver and passenger. Display manufacturer,model,airbags in output
# 

# In[579]:


car["AirBags"].unique()


# In[580]:


car["AirBags"].unique()


# # Find out cars whose luggage room >15

# In[581]:


car.columns


# In[582]:


car["Luggage.room"].unique()


# In[583]:


car[car["Luggage.room"]>15][["Luggage.room","Manufacturer","Type"]]


# In[584]:


car.sort_values(by="Price",ascending=False)[["Price","Manufacturer"]]


# In[585]:


car.sort_values(by="Price",ascending=False)[["Price","Manufacturer"]]


# # FInd out cars which belong to sport type and are priced more than 25. Display the data in descending order of price

# In[586]:


car.head(1)


# In[587]:


car['Type'].unique()


# In[588]:


car[(car["Type"]=="Sporty") & (car["Price"]>25 )][["Manufacturer","Model","Type","Price"]].sort_values(by="Price")


# In[589]:


car[(car["Type"]=="Sporty") & (car["Price"]>25 )][["Manufacturer","Model","Type","Price"]].sort_values(by="Price",ascending=False)


# In[590]:


car[(car["Type"]=="Sporty") & (car["Price"]>25 )][["Manufacturer","Model","Type","Price"]].sort_values(by="Price",ascending=False)


# # Find out cars which provide aribags to driver and passenger. Display manufacturer,model,airbags in output. Display the data in descending order of MPG.city

# In[591]:


car[car["AirBags"]=="Driver & Passenger"][["Manufacturer","Model","AirBags","MPG.city"]].sort_values(by="MPG.city")


# In[592]:


car.isnull().sum()[car.isnull().sum()>0]


# # 03/05/2025

# # DataFrame

#  # Missing Values: NA, NAN,null, blank ,None,none,na,nan,NULL
# 

# In[593]:


import pandas as pd


# In[594]:


pd.read_csv(r"C:\Users\user\Downloads\Cars93.csv")

car=pd.read_csv(r"C:\Users\user\Downloads\Cars93.csv")
# In[595]:


car


# In[596]:


car.head()


# In[597]:


car.head()


# In[598]:


car.columns


# # Missing values

# In[599]:


car.isna().sum()


# In[600]:


car.isnull().sum()[car.isnull().sum()>0]


# In[601]:


car.shape


# # Handling Missing values

# In[602]:


car.head()


# In[603]:


car.info()


# In[604]:


car.isnull().sum()[car.isnull().sum()>0]


# In[605]:


car["AirBags"].unique()


# In[606]:


a


# In[607]:


car["AirBags"]=car["AirBags"].fillna(a)


# In[608]:


car


# In[609]:


car.AirBags.fillna("Driver only",inplace=True)


# In[610]:


car


# In[611]:


car.isnull().sum()[car.isnull().sum()>0]


# In[612]:


car.AirBags.fillna(car.AirBags.mode(),inplace=True)


# In[613]:


car


# In[614]:


car["Rear.seat.room"].unique()


# In[615]:


c1=car["Rear.seat.room"].mean()


# In[616]:


c1


# In[617]:


car["Rear.seat.room"].fillna(c1,inplace=True)


# In[618]:


car


# In[619]:


car.isnull().sum()[car.isnull().sum()>0]


# In[620]:


car["Luggage.room"].unique()


# In[621]:


c2=car["Luggage.room"].median()


# In[622]:


c2


# In[623]:


car["Luggage.room"].fillna(c2,inplace=True)


# In[624]:


car


# In[625]:


car.head(20)


# In[626]:


car1=pd.read_csv(r"C:\Users\user\Downloads\Cars93.csv")


# In[627]:


car1


# In[628]:


car1.isnull().sum()[car1.isnull().sum()>0]


# In[629]:


car1.dropna(subset=["AirBags"],inplace=True)

car1.shape
# In[630]:


car1.describe().T


# In[631]:


cat=list(car1.columns[car1.dtypes=="object"])


# In[632]:


cat


# In[633]:


cat=list(car1.columns[car1.dtypes=="object"])
cat


# In[634]:


car1.info()


# In[635]:


con=list(car1.columns[car1.dtypes!="object"])


# In[636]:


con


# In[637]:


car1[cat].describe().T


# In[638]:


car1[con].describe().T


# In[639]:


car1.drop(columns="id",inplace=True)


# In[640]:


car1


# In[641]:


car1.head(1)


# In[642]:


car1.duplicated().sum()


# In[643]:


car1.drop_duplicates(keep="first",inplace=True)


# In[644]:


car1


# In[645]:


pd.read_csv(r"C:\Users\user\Downloads\Property_Price_Train.csv")


# In[646]:


ppt=pd.read_csv(r"C:\Users\user\Downloads\Property_Price_Train.csv")
ppt


# In[647]:


ppt.shape


# In[648]:


ppt.isnull().sum()[ppt.isnull().sum()>0]


# In[649]:


ppt["Zoning_Class"].unique()


# In[650]:


con


# # Aggregation

# In[651]:


import pandas as pd


# In[652]:


car.head()


# In[653]:


car.dtypes


# In[654]:


car.info()


# In[655]:


car.count()


# In[656]:


car.min(numeric_only=True)


# In[657]:


car.max(numeric_only=True)


# In[658]:


car["Price"].min()


# In[659]:


car["Price"].max()


# In[660]:


car[["Price","Passengers"]].std()


# In[661]:


car["Turn.circle"].min()


# In[662]:


car[["Price","Passengers"]].mean()


# In[663]:


car.agg({"Price":"sum"})


# In[664]:


car.agg({"Price":["sum","max","min","std"]})


# In[665]:


car.agg({"Price":["sum","max","min","std"],
        "Passengers":["sum","max","min"]})


# # Group by

# In[666]:


car.columns


# In[667]:


car["AirBags"].unique()


# In[668]:


car.groupby("AirBags").Price.min()


# In[669]:


car.groupby("AirBags").Price.mean()


# In[670]:


a=car.groupby(by="AirBags").sum(numeric_only=True)[["Passengers","Price","MPG.city"]]


# In[671]:


a


# In[672]:


a.plot(kind="barh")


# In[673]:


a


# In[674]:


car.columns


# In[675]:


car["Type"].unique()


# In[676]:


car.groupby(by=["AirBags","Type"]).max(numeric_only=True)[["Price","Horsepower","Passengers"]]


# In[677]:


car.groupby(by=["AirBags","Type"]).max(numeric_only=True)[["Price","Horsepower","Passengers"]]


# # Find out cars which provide highest MPG.highway.
# 

# In[678]:


car["MPG.highway"].unique()


# In[679]:


car.sort_values(by="MPG.highway",ascending=False).head(1)


# In[680]:


car["MPG.highway"].unique()


# In[681]:


car.sort_values(by="MPG.highway",ascending=False).head(1)


# # Find out cars types with average price less than 20
# 

# In[682]:


avg=car["Price"].mean()


# In[683]:


avg


# In[684]:


f1=car["Price"]<avg


# In[685]:


f1


# In[686]:


car[f1].sort_values(by="Price")[["Type","Price"]]


# In[687]:


b1=car.groupby(by="Type").mean(numeric_only=True)[["Price"]]


# In[688]:


b1


# In[689]:


car.columns


# In[690]:


car["Type"].unique()


# In[691]:


car.groupby(by=["AirBags","Type"]).max(numeric_only=True)[["Price","Horsepower","Passengers"]]


# In[692]:


car.groupby(by=["Type","AirBags"]).max(numeric_only=True)[["Price","Horsepower","Passengers"]]


# # Find out cars which provide highest MPG.highway.
# 

# In[693]:


car["MPG.highway"].unique()


# In[694]:


car.sort_values(by="MPG.highway",ascending=False).head(1)


# # Find out cars types with average price less than 20
# 

# In[695]:


avg=car["Price"].mean()
avg


# In[696]:


f1=car["Price"]<avg


# In[697]:


f1


# In[698]:


car[f1].sort_values(by="Price")[["Type","Price"]]


# In[699]:


b1=car.groupby(by="Type").mean(numeric_only=True)[["Price"]]
b1


# In[700]:


b1[b1["Price"]<avg]


# # Find out cars having AirBags with max price
# 

# In[701]:


car.groupby(by="AirBags").max(numeric_only=True)[["Price"]]


# In[702]:


car.columns


# # Find out the average horsepower of diff cars types having diff airbags
# 

# In[703]:


car.groupby(by=["AirBags","Type"]).mean(numeric_only=True)[["Horsepower"]]


# In[704]:


car.groupby(by=["Type","AirBags"]).mean(numeric_only=True)[["Horsepower"]]


# # Find out avg horsepower based on cylinders
# 

# In[705]:


car["Cylinders"].unique()


# In[706]:


car.groupby(by="Cylinders").Horsepower.mean()


# In[707]:


car.groupby(by="Cylinders").mean(numeric_only=True)[["Horsepower"]]


# In[708]:


car.columns


# # Creating new columns in existing dataframes

# # Create price column showing price in USD. Price of cars is in 1 Lakhs INR. Check current usd price
# 

# In[709]:


car["Price"]/89


# In[710]:


car["usd_prce"]=car["Price"]/89


# In[711]:


car.columns


# In[712]:


car.head()


# # Create a column based on conditions
# 

# In[713]:


car["Price"]


# In[714]:


price_tag=[]

for i in car["Price"]:
    if i>0 and i<=17:
        price_tag.append("low price")
    elif i>17 and i<=22:
        price_tag.append("Moderate")
    elif i>22:
        price_tag.append("Expensive")
    else:
        price_tag.append("other")



# In[715]:


price_tag


# In[716]:


car["price_tag"]=price_tag
price_tag


# In[717]:


car.columns


# In[718]:


car.head(1)


# In[719]:


car.groupby("Manufacturer").Price.mean()


# # Combining 2 columns with merge

# In[720]:


import pandas as pd


# In[721]:


dp=pd.read_csv(r"C:\Users\user\Downloads\customer_shopping_data.csv")


# In[722]:


dp


# In[723]:


dp.head()


# # inner join

# In[724]:


emp=pd.read_csv(r"C:\Users\user\Downloads\emp_21.csv")
emp


# In[725]:


dept=pd.read_csv(r"C:\Users\user\Downloads\dept_21.csv")


# In[726]:


dept


# In[727]:


emp.head()


# In[728]:


dept.head()


# In[729]:


emp.info()


# In[730]:


dept.info()


#  ## Inner join

# In[731]:


inner=pd.merge(emp,dept,how="inner",left_on="did",right_on="dept_id")


# In[732]:


inner


# In[733]:


pd.merge(dept,emp,how="inner",left_on="dept_id",right_on="did")


# In[734]:


inner.info()


# In[735]:


left=pd.merge(emp,dept,how="left",left_on="did",right_on="dept_id")


# In[736]:


left


# In[737]:


left.info()


# In[738]:


left=pd.merge(emp,dept,how="left",left_on="did",right_on="dept_id")


# In[739]:


left


#  ## Right join

# In[740]:


right=pd.merge(emp,dept,how="right",left_on="did",right_on="dept_id")


# In[741]:


right


# In[742]:


a=right[right["dname"]=="ADM"]


# In[743]:


a


# In[744]:


a["fn"]="sakshi"
a


# ## Full Outer Join

# In[745]:


outer=pd.merge(emp,dept,how="outer",left_on="did",right_on="dept_id")


# In[746]:


outer


# # Retrieve department details of Madhu Reddy

#  # inner

# In[747]:


inner[ (inner["fn"]=="Madhu") & (inner["ln"]=="Reddy")]


# # Find out the department name providing max salary to employees
# 

# # inner

# In[748]:


a=inner["sal"].max()


# In[749]:


f1=inner["sal"]==a


# In[750]:


f1


# In[751]:


inner[f1][["dname"]]


# In[752]:


f2=inner["sal"]==inner["sal"].max()


# In[753]:


f2


# In[754]:


inner[f2][["dname"]]


# In[755]:


inner.nlargest(2,columns="sal")[["dname"]]


# In[756]:


inner.nsmallest(1,columns="sal")


# In[757]:


inner.max()[["sal","dname"]]


# #  #Updating data in a dataframe

# # Update fn and ln for employee working in ADM department.
# 

# In[758]:


outer[outer["dname"]=="ADM"]


# In[759]:


outer.loc[6,"fn"]="sakshi"


# In[760]:


outer.iloc[6,2,]="thombre"


# # Update dname with BH for employee working in department whose id is 113
# 

#  # outer

# In[761]:


outer[outer["did"]==113]


# In[762]:


outer.iloc[9,6]="BH"


# # Update salary details for employee in 1 with 8500
# 

# # outer

# # SampleStore

# In[763]:


pip install xlrd


# In[764]:


pd.read_excel=(r"C:\Users\user\Downloads\50_Startups(1).csv")
pd


# In[765]:


outer=pd.merge(emp,dept,"outer",left_on="did",right_on="dept_id")


# In[766]:


outer


# In[767]:


mean_amount=outer["sal"].mean()


# In[768]:


mean_amount


# # Statistics Overview

# # EDA - Exploratory Data Analysis
# 

#  ## Step1: Data Ingestion-

# Read the dataset

# In[769]:


import pandas as pd


# In[770]:


pd.read_csv(r"C:\Users\user\Downloads\laptopPrice.csv")


# In[771]:


lp=pd.read_csv(r"C:\Users\user\Downloads\laptopPrice.csv")
lp


# In[772]:


lp.info()


# # Basic Data quality checks-

# In[773]:


lp.columns


# In[774]:


lp.head()


# # Step3: Data Cleaning and Data Transformation:

# In[775]:


lp.isnull().sum()[lp.isnull().sum()>0]


# In[776]:


lp.duplicated().sum()


# In[777]:


lp.duplicated().sum()


# In[778]:


lp.drop_duplicates(keep="first",inplace=True)


# In[779]:


lp.duplicated().sum()


# ## # Step4: Separate Categorical and Continuous data
# 

# In[780]:


lp.columns


# In[781]:


lp.info()


# In[782]:


f1=lp.dtypes=="object"


# In[783]:


f1


# In[784]:


f1=lp.dtypes=="object"


# In[785]:


f1


# In[786]:


f2=lp.dtypes!="object"


# In[787]:


f2


# In[788]:


lp.columns[f2]


# In[789]:


lp.columns[f1]


# In[790]:


list(lp.columns[lp.dtypes=="object"])


# In[791]:


cat


# In[792]:


con


# # Step5: Descriptive Statistics

# In[793]:


lp.describe().T


# In[794]:


lp


# # Univariate Analysis

# #categorical: countlplot, barplots
# # Continuous: Histogram

# In[795]:


import matplotlib.pyplot as plt


# In[796]:


import seaborn as sns


# # Categorical Data

# In[797]:


lp.columns


# In[798]:


con


# In[799]:


cat


# In[800]:


sns.countplot(data=lp,x="brand")


# In[801]:


plt.figure(figsize=(10,7))
sns.countplot(data=lp,x="brand")
plt.title("countplot of brand")
plt.show()


# In[802]:


plt.figure(figsize=(6,8))
sns.countplot(data=lp,x="brand",color="purple")
plt.title("count_plot of brand")
plt.show()


# In[803]:


plt.figure(figsize=(9,8))
sns.countplot(data=lp, x="brand",hue="brand")
plt.title("count_plot of brand")
plt.show()


# In[804]:


plt.figure(figsize=(9,8))
sns.countplot(data=lp,x="brand",hue="ram_gb")
plt.title("count_plot of brand")
plt.show()


# In[805]:


cat


# In[806]:


con


# In[807]:


con


# In[808]:


plt.figure(figsize=(6,6))
sns.histplot(data=lp,x="Price")
plt.show()


# In[809]:


plt.figure(figsize=(8,8))
sns.histplot(data=lp,x="Price",bins=7)
plt.show()


# In[810]:


con


# In[811]:


sns.histplot(data=lp,x="Number of Ratings",bins=70)
plt.title("histgram of 'Number of Ratings")
plt.show()


# In[812]:


con


# In[813]:


sns.histplot(data=lp,x="Number of Reviews",bins=30)


# In[814]:


sns.histplot(data=lp,x="Price",kde=True,color="red")


# In[815]:


con


# In[816]:


sns.histplot(data=lp,x="Price",kde=True,hue="brand")


# In[817]:


cat


# In[818]:


sns.histplot(data=lp,x="Price",kde=True,hue="ram_gb")


# # Find out avg price of laptops by brand
# 

# In[819]:


a=lp.groupby(by="brand").mean(numeric_only=True).sort_values(by="Price",ascending=False).round(2)[["Price"]]


# In[820]:


lp["brand"].unique()


# In[821]:


lp[lp["brand"]=="APPLE"].mean(numeric_only=True)


# In[822]:


a


# In[823]:


a.to_csv("avgprice by brand.csv",index=False)


# In[824]:


a.plot(kind="bar")


# In[825]:


sns.barplot(data=a,x="brand",y="Price",hue="brand")


# In[826]:


cat


# # Bivariate Analysis

# # Continuous vs Continuous data

# In[827]:


sns.scatterplot(data=lp,x="Price",y="Number of Ratings")
plt.show()


# In[828]:


con


# In[829]:


con


# In[830]:


sns.regplot(data=lp,x="Price",y="Number of Ratings",line_kws={"color":"red"})


# In[831]:


sns.regplot(data=lp,x="Number of Ratings",y="Number of Reviews",line_kws={"color":"red"})


# In[832]:


con


# In[833]:


lp.corr(numeric_only=True)


# In[834]:


sns.scatterplot(data=lp,x="Price",y="Number of Ratings",hue="brand")


# In[835]:


sns.scatterplot(data=lp,x="Number of Ratings", y="Number of Reviews",hue="brand")


# In[836]:


a1=lp.corr(numeric_only=True)


# In[837]:


a1


# In[838]:


sns.heatmap(data=a1,annot=True,cmap="coolwarm")


# In[839]:


plt.hist(lp["Price"],bins=30,edgecolor="black")


# In[840]:


sns.histplot(data=lp,x="Number of Reviews",bins=30)


# # 10/09/2026

# # Categorical vs Categorical

# In[845]:


ctab=pd.crosstab(lp["brand"],lp["processor_brand"])


# In[846]:


ctab


# In[847]:


sns.heatmap(ctab,annot=True,cmap="coolwarm")


# In[848]:


lp["ram_type"].unique()


# In[849]:


lp["ram_gb"].unique()


# In[852]:


ctab1=pd.crosstab(lp["ram_gb"],lp["ram_type"])


# In[853]:


ctab


# In[854]:


sns.heatmap(ctab1,annot=True,fmt="d")


# # --- heatmap -- > cmap="coolworm"
# 
# Red=Strong positive correlatiion (+1)
# White=NO correlation(0)
# blue=Strong negative correlation (-1)
# 
# ###Red=hot
# white=Neutral/Moderate
# Blue=Cold

# ## Categorical vs Continous

# In[857]:


print(cat)


# In[858]:


print(con)


# In[859]:


sns.boxplot(data=lp,x="brand",y="Price")
plt.show()


# In[860]:


import numpy as np


# In[861]:


q1=np.percentile(lp["Price"],25,method="midpoint")


# In[862]:


q1


# In[863]:


q2=np.percentile(lp["Price"],50,method="midpoint")
q2


# In[864]:


q3=np.percentile(lp["Price"],75,method="midpoint")
q3


# In[865]:


IQR=q3-q1
IQR


# In[866]:


min_outlier=q1-1.5*IQR
min_outlier


# In[868]:


max_outlier=q3+1.5*IQR
max_outlier


# In[869]:


q1=np.percentile(lp["Price"],25,method="midpoint")
q3=np.percentile(lp["Price"],75,method="midpoint")
IQR=q3-q1

lower_bound=q1-1.5*IQR
upper_bound=q3+1.5*IQR

outlier=[x for x in lp["Price"] if x < lower_bound or x > upper_bound]
print(outlier)


# In[870]:


outliers_df=lp[lp["Price"] > max_outlier]
sns.countplot(data=outliers_df,x="brand")


# In[871]:


outliers_df=lp[lp["Price"] > min_outlier]
sns.countplot(data=outliers_df,x="brand")


# # Multivariate Analysis

# In[872]:


sns.pairplot(lp,hue="os_bit")


# In[873]:


sns.pairplot(lp,hue="brand")


# In[874]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[875]:


GDP           = (19.4, 11.8 ,  4.8,   3.4,   2.5,     2.4)

countries    = ('United states of america' ,'CHINA','JAPAN','GERM','United kingdom','INDIA')


# In[876]:


plt.pie(GDP,labels=countries,);


# In[877]:


plt.pie(GDP,labels=countries,autopct="%1.1f%%",explode=(0,0,0,0,0,0.7))
plt.title("GDP in USD Trillions")


# In[879]:


plt.pie(GDP,labels=countries,autopct="%2.1f%%",wedgeprops=dict(width=.5))
plt.title("GDP in USD Trillions")


# In[ ]:




