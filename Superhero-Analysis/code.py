# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data= pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
gender_count=data['Gender'].value_counts()
plt.figure(figsize=(10,6))
index = data['Gender'].unique()
plt.bar(index,gender_count)
plt.xlabel('Gender', fontsize=15)
plt.ylabel('Number of superheros', fontsize=15)
plt.xticks(index,fontsize=15, rotation=30)
plt.title('Gender variation in superheros')
plt.show()
#Code starts here 




# --------------
#Code starts here
plt.figure(figsize=(10,6))
alignment=data['Alignment'].value_counts()
indexs=['good', 'bad', 'neutral']
plt.bar(indexs,alignment)
plt.title('Character Alignment')
plt.show()


# --------------
sc_df=data[['Strength','Combat']]
sc_covariance=617.49
sc_strength=data['Strength'].std()
sc_combat=data['Combat'].std()
sc_pearsonr=sc_covariance/(sc_strength*sc_combat)
sc_pearson=np.around(sc_pearsonr,decimals=2)
ic_df=data[['Intelligence','Combat']]
ic_covariance=853.42
ic_combat=data['Combat'].std()
ic_intelligence=data['Intelligence'].std()
ic_pearsonr=ic_covariance/(ic_intelligence*sc_combat)
ic_pearson=np.around(ic_pearsonr,decimals=2)


# --------------
#Code starts here
total_high=data['Total'].quantile(q=0.99)
super_best=pd.DataFrame(data['Total'][data['Total']>total_high])        
super_best_names=list(data['Name'][data['Total'] > total_high]) 
print(super_best_names)


# --------------
ax_1=plt.boxplot(data['Speed'])
plt.title('Speed')
ax_2=plt.boxplot(data['Intelligence'])
plt.title('Intelligence')
ax_3=plt.boxplot(data['Power'])
plt.title('Power')


