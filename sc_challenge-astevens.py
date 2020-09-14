#!/usr/bin/env python
# coding: utf-8

# # Imports & reading

# In[1]:


import pandas as pd
import pandas_profiling as pdp


# In[2]:


df_train = pd.read_csv('marketing_training.csv')
df_test = pd.read_csv('marketing_test.csv')
display("train size", df_train.shape, "test size", df_test.shape)
print('\n\nView training data')

display(df_train)
display(df_train.dtypes)


# # EDA

# In[3]:


profile = pdp.ProfileReport(df_train, title='Pandas Profiling Report', explorative=True)
# profile.to_file("your_report.html")
profile.to_notebook_iframe()


# # clean data

# In[4]:


dummies_train = df_train.dropna()
dummies_train = pd.get_dummies(dummies_train, columns=['profession','marital','schooling','default',
                                                  'housing','loan','contact','month','day_of_week','poutcome'])
dummies_train.responded = dummies_train.responded.replace({'yes':1,"no":0})

trainy = pd.np.array(dummies_train['responded'], dtype='int')
dummies_train=dummies_train.drop(['responded', 'default_yes', 'schooling_illiterate'], axis=1)
trainX=dummies_train.values


# In[5]:


dummies_train.info(verbose=True)

# filling empties degraded performance
dummies_train = df_train.copy()
dummies_train['custAge'] = dummies_train['custAge'].fillna(dummies_train['custAge'].mean())
dummies_train.schooling = dummies_train.schooling.fillna("Unknown")
dummies_train.day_of_week = dummies_train.day_of_week.fillna("Unknown")
dummies_train = pd.get_dummies(dummies_train, columns=['profession','marital','schooling','default',
                                                  'housing','loan','contact','month','day_of_week','poutcome'])
dummies_train.responded = dummies_train.responded.replace({'yes':1,"no":0})

trainy = pd.np.array(dummies_train['responded'], dtype='int')
dummies_train=dummies_train.drop(['responded', 'default_yes', 'schooling_illiterate'], axis=1)
trainX=dummies_train.values
# In[6]:


dummies_test = pd.get_dummies(df_test, columns=['profession','marital','schooling','default',
                                                  'housing','loan','contact','month','day_of_week','poutcome'])
dummies_test = dummies_test.drop(['Unnamed: 0'], axis=1)
testX = dummies_test.values


# In[20]:


def Diff(li1, li2): 
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

display("column diff: ", Diff(dummies_train.columns, dummies_test.columns))
display(trainX.shape)
display(trainy.shape)
display(testX.shape)


# # test model

# In[8]:


import sklearn.metrics
from sklearn.model_selection import train_test_split
import autosklearn.classification

X_train, X_test, y_train, y_test = train_test_split(trainX, trainy, test_size=0.25, random_state=42)
cls = autosklearn.classification.AutoSklearnClassifier(metric=autosklearn.metrics.f1, n_jobs=4, ml_memory_limit=6144)
cls.fit(trainX, trainy)
y_hat = cls.predict(X_test)
print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_hat))
# Accuracy score 0.9415538132573058
print("Balanced Accuracy score", sklearn.metrics.balanced_accuracy_score(y_test, y_hat))
# Balanced Accuracy score 0.8896719770433406


# In[9]:


from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
cm = confusion_matrix(y_test, y_hat)
disp = ConfusionMatrixDisplay(cm, display_labels=['yes','no'])
disp = disp.plot(values_format='.0f')


# In[10]:


print(cls.sprint_statistics())


# In[11]:


cls.show_models()


# In[12]:


cls.cv_results_


# In[13]:


import PipelineProfiler
profiler_data = PipelineProfiler.import_autosklearn(cls)
PipelineProfiler.plot_pipeline_matrix(profiler_data)


# # Retrain model using full set

# In[14]:


automl = autosklearn.classification.AutoSklearnClassifier(metric=autosklearn.metrics.f1, n_jobs=4, ml_memory_limit=6144)
automl.fit(trainX, trainy)


# In[15]:


predictions = automl.predict(testX)


# In[16]:


predictions


# In[17]:


df_test['responded'] = predictions


# In[18]:


df_test.to_csv('test_results_astevens.csv')

