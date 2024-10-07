### OLTP vs OLAP
- OLTP (Online Transaction Processing) focus on real-time
- OLAP (Online Analytical Processing) focus on analysis

### Data Warehouse, Database, Data Lake
- Data Lake: any data collected just dump there, minimal processing
- Database: transactions etc real time stuff store here.
- Data Warehouse: any long-term valuable data, ETFed into good shape, put here, for analysis and business decisions.


### Warehouse
1. Data Sources
2. Data Staging: ETL
3. Data Warehouse: relational db and metadata
4. Data Marts: subset of data, for each business departments
5. Data Analytics
6. Presentation

### Dimensional Modeling
- Dimensions: the context of your data (like time and location)
- think of your data like a vector and dimensions are the axis
- Procedure: 
  - Identify business process
  - Identify dimensions & facts (Create a star schema)
  - Get the answer

### Different type of data analysis
- Descriptive: just description (shallow)
- Exploratory: find patterns (deep)
- Inferential: infer from sample to population (generalize)
- Predictive: predict future 
- Causal: cause and effect

### Data measurement scale
- Nominal: no order, like color
- Ordinal: order, like rating
- Interval: order and equal distance, like temperature
- Ratio: order, equal distance, and absolute zero, like weight

### Data mining vs Machine Learning
- Data mining: find patterns in data
- Machine Learning: supervised and unsupervised learning
