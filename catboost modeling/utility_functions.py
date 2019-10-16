#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def find_column_names(df,regex):
    list_of_column_names = []
    for i in df.columns.str.findall(regex):
        if(len(i)>0):
            list_of_column_names.append(i[0])
    return list_of_column_names


# In[ ]:


#py_name_list = find_column_names(status,'py_[a-z]')


# In[ ]:


def sum_some_columns(sum_name,df,columns):
    df[sum_name] = df[columns].sum(axis=1)
    return df


# In[ ]:


#processed_status['py_total'] = sum_some_columns('py_total',status,py_name_list)['py_total']


# In[ ]:


def drop_y(df):
    to_drop = [x for x in df if x.endswith('_y')]
    df.drop(to_drop, axis=1, inplace=True)


# In[ ]:


def strip_right(df, suffix='_x'):
    df.columns = df.columns.str.rstrip(suffix)


# In[ ]:




