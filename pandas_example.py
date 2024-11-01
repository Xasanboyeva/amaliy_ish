import pandas as pd
data ={
    'Ism': ['Sarvinoz','Xushnoza','Shahzoda'],
    'Yosh': [19, 18, 20],
    'Shahar': ['Farg\'ona','Andijon','Namangan'],
}
df =pd.DataFrame(data)
print(df)

young_people =df[df['Yosh']<20]
print("\n20 yoshdan kichiklar :\n" , young_people)

df['Yosh'] += 1
print("\nYangilangan DataFrame:\n" , df)

df.to_excel('541.xlsx', index=True, sheet_name="541")
