def replace_values(df, columns):
    for col in columns:
        df[col].replace({2: 0, 97: np.nan, 98: np.nan, 99: np.nan}, inplace=True)
        
replace_values(df,['RENAL_CHRONIC','TOBACCO','INTUBED','PNEUMONIA','DIABETES','COPD','ASTHMA','INMSUPR','HIPERTENSION','OTHER_DISEASE', 'CARDIOVASCULAR', 'OBESITY',
       'RENAL_CHRONIC', 'TOBACCO','ICU'])
df['SEX'].replace({1:'Female',2:"Male"},inplace=True)
df.loc[df["PREGNANT"].isin([97, 98, 99]) & (df["SEX"] == "Male"), "PREGNANT"] = 0
df["PREGNANT"].replace({2: 0, 97: np.nan, 98: np.nan,99: np.nan}, inplace=True)
df["CLASIFFICATION_FINAL"].replace({2:1,3:1,4:0,5:0,6:0,7:0},inplace=True)
df.rename(columns={'CLASIFFICATION_FINAL':'ANTIGEN_TEST'},inplace=True)
df = df.rename(columns={"PATIENT_TYPE":"HOSPITALIZED"})
df["HOSPITALIZED"].replace({1:0,2:1},inplace=True)
df = df.rename(columns={"DATE_DIED":"DIED"})
df["DIED"] = df["DIED"].replace("9999-99-99",0).replace([value for value in df["DIED"].unique() if value !=0],1)
df.drop("INTUBED",axis=1,inplace=True)
df.drop("ICU",axis=1,inplace=True)
df.dropna(inplace=True)
numeric_features = [feature for feature in df.columns if df[feature].dtype != 'O']
categorical_features = [feature for feature in df.columns if df[feature].dtype == 'O']
df = df[~(df["AGE"]>100)]