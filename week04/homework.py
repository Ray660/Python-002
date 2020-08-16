import pandas as pd 
import numpy as np 
data = pd.DataFrame({'id':np.random.randint(990,1100,50),
                    'age':np.random.randint(0,100,50)
                    })
# 1. SELECT * FROM data;
print(data)
print('='*40)

# 2. SELECT * FROM data LIMIT 10;
print(data.loc[0:9])
print('='*40)

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
print(data['id'])
print('='*40)

# 4. SELECT COUNT(id) FROM data;
print(data['id'].count())
print('='*40)

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data[ (data['id']<1000) & (data['age']>30) ])
print('='*40)

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
table1 = pd.DataFrame({'id':np.random.randint(990,1100,50),
                    'age':np.random.randint(0,100,50),
                    'order_id':np.random.randint(1,5,50)
                    })
table1.drop_duplicates('order_id')
table = table1.drop_duplicates('order_id').groupby('id').groups
for i in table:
    print(i)
print('='*40)

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
table2 = pd.DataFrame({'id':np.random.randint(990,1100,50),
                    'age':np.random.randint(0,100,50),
                    'order_id':np.random.randint(1,5,50)
                    })

print(pd.merge(left=table1,right=table2,on=['order_id'],how='inner'))
print('='*40)

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
table3 = pd.concat([table1,table2]).drop_duplicates('id')
print(table3.reset_index())
print('='*40)

# 9. DELETE FROM table1 WHERE id=10;
t = table1[table1['order_id'] == 1]
table4 = table1.drop(t.index)
print(table4)
print('='*40)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
print(table1.drop('id',axis=1))