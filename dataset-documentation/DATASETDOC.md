***Project Information*** 

* What is the project name?
  * Center for Career Development: Employer Engagement Analysis Project  
* What is the link to your project’s GitHub repository?
  * https://github.com/BU-Spark/ds-employer-engagement
* What is the link to your project’s Google Drive folder?
  *  https://drive.google.com/drive/folders/1J2CJtQSYEuWm8B8Q84Oz6yNCJK8ntR-V?usp=drive_link
* In your own words, what is this project about? What is the goal of this project?
  * The project focused on helping BU’s Center for Career Development (CCD) examine relationships between employer activity on Handshake and student engagement in order to generate insights that could inform how CCD works with employers to better support students. Our work involved cleaning and merging multiple datasets, conducting in-depth exploratory and descriptive analysis, and identifying key trends and takeaways for the CCD. We then translated these findings into a final slide deck featuring visuals and insights, along with interactive Power BI dashboards that allow the CCD to further explore patterns in the data.   
* Who is the client for the project?
  * BU Center for Career Development
* Who are the client contacts for the project?
  * Jimmy Huynh
* What class was this project part of?
  * DS539 

***Dataset Information***

* What data sets did you use in your project? Please provide a link to the data sets, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.
  * https://drive.google.com/drive/folders/10tWOuJmGdCYVl1DOx6Eg2YQmPNQ-muF-?usp=drive_link 
* Please provide a link to any data dictionaries for the datasets in this project. If one does not exist, please create a data dictionary for the datasets used in this project. **(Example of data dictionary)**
  * https://docs.google.com/spreadsheets/d/1wkY-KdXLx2h5ijB_Gmau4IqvmQJwrUwtiCE50SrMuCs/edit?usp=drive_link   
* What keywords or tags would you attach to the data set?  
  * Domain(s) of Application: Data Science, Data Analytics, Exploratory Data Analysis (EDA), Data Visualization, Business Intelligence, Statistical Analysis   
  * Application Areas: Education, Workforce Development, Student Engagement, Employer Engagement, Employment Outcomes, Career Services

*The following questions pertain to the datasets you used in your project.*   
*Motivation* 

* For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.
  *  The main purpose for creating the dataset was to consolidate and clean raw Handshake data so it could be analyzed in a more structured and understandable way. We were also specifically focused on transforming the data into a more accessible format, using Power BI dashboards to make the insights easier for the CCD to explore and understand at a higher level.

*Composition*

* What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? What is the format of the instances (e.g., image data, text data, tabular data, audio data, video data, time series, graph data, geospatial data, multimodal (please specify), etc.)? Please provide a description.
  * The instances (rows) represent employer activity on Handshake, including associated job and event postings, as well as student outcomes after graduation.
  * There are multiple types of instances across the datasets, including students, employers, jobs, events, as well as a joint dataset that combines the latter three instances.
  * Tabular data.   
* How many instances are there in total (of each type, if appropriate)?
  *   ep_base_cleaned: 56089 instances
  *   ep_event_cleaned: 11814 instances
  *   ep_job_cleaned: 886840 instances
  *   ep_joined: 1048575 instances
  *   FDS 2020-2024 Employer Outcomes (Anonymized): 10003
* Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).
  *  Each dataset contains the entire set of instances.
* What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a description.
  *  Each instance includes fields such as employer names, job titles, event names, dates (job creation and event dates), and numerical values like application counts, attendee counts, and salary ranges. The data has been cleaned and processed from the original raw Handshake exports into a tabular format suitable for analysis, save for the FDS data.
* Is there any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include redacted text.
  * Yes, there is missing information in several fields across the dataset. Some instances have missing values for salary data (min and max salary), employer size, application counts, and event attendance. There are also gaps in hiring outcome data and limited student-level information.
This missing information is largely due to incomplete reporting on the Handshake platform, inconsistencies in how employers input data, and limitations in the data available to the CCD (e.g., not all hiring outcomes or student interactions are tracked within the system). 
* Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them
  *  No, there are no predefined training, validation, or testing splits for this dataset. The dataset was created for exploratory data analysis, descriptive insights, and dashboarding rather than for building predictive machine learning models.
* Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a description.
  *  Yes, there are still some sources of noise and potential redundancy in the dataset. While duplicate records in the original job and event datasets were removed during cleaning, the final joined dataset can still contain repeated employer entries due to one-to-many relationships between employers, jobs, and events.
  *  There are also inconsistencies in fields such as salary, where values may be missing, reported in different units, or contain extreme placeholder values. Additionally, some application and attendance counts appear unusually low, which may reflect incomplete tracking rather than true engagement levels.   
* Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? If it links to or relies on external resources,   
  * Are there guarantees that they will exist, and remain constant, over time;  
  * Are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created)?  
  * Are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a dataset consumer? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points as appropriate.
    *  The dataset is not fully self-contained, as it is derived from external data exported from the Handshake platform used by the CCD. It relies on data originally collected through Handshake, including employer activity, job postings, and event participation and will need to be manually updated for recent years.
    *  There are no guarantees that the original data on Handshake will remain constant over time. Data may be updated, modified, or removed on the platform, and future exports may differ from the version used in this project.
    *  There is no publicly available official archival version of the dataset. The version used for this project is a static export provided to the team, but it is not formally archived for external access.
    *  Yes, access to the underlying Handshake data is restricted. It is limited to authorized users, such as CCD staff and affiliated researchers, and may be subject to institutional data policies and platform terms of service. As a result, the dataset cannot be freely redistributed, and external users would need appropriate access permissions to obtain similar data.
* Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals’ non-public communications)? If so, please provide a description.
  *  It does include institutional data from the Handshake platform, such as employer activity, job postings, and aggregated student engagement metrics, which may be considered restricted or internal to the CCD. Additionally, any student-related outcome data used in extended analysis is anonymized and aggregated,  meaning individual identities are not directly included.
* Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.
  *  No it does not.
* Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset? If so, please describe how.
  *  No, personal student data is anonymized. The only identifiable data is at a company-wide level.
* Dataset Snapshot, if there are multiple datasets please include multiple tables for each dataset.
  
  * ep_base_cleaned:

| Size of dataset | 6.4 MB |
| :---- | :---- |
| Number of instances | 56089 |
| Number of fields  | 8 |

  * ep_event_cleaned:

| Size of dataset | 1.2 MB |
| :---- | :---- |
| Number of instances | 11814 |
| Number of fields  | 7 |

  * ep_job_cleaned:

| Size of dataset | 85.6 MB |
| :---- | :---- |
| Number of instances | 886840 |
| Number of fields  | 8 |

  * ep_joined:

| Size of dataset | 784.3 MB |
| :---- | :---- |
| Number of instances | 1048575 |
| Number of fields  | 20 |

  * FDS 2020-2024 Employer Outcomes (Anonymized):

| Size of dataset | 945 KB |
| :---- | :---- |
| Number of instances | 10004 |
| Number of fields  | 22 |

  
*Collection Process*

* What mechanisms or procedures were used to collect the data (e.g., API, artificially generated, crowdsourced \- paid, crowdsourced \- volunteer, scraped or crawled, survey, forms, or polls, taken from other existing datasets, provided by the client, etc)? How were these mechanisms or procedures validated?
  *  The data was collected from Handshake platform exports and provided by the CCD, along with internal outcome data (e.g., FDS). It was originally entered by employers and recorded by the platform. Validation was done through data cleaning steps such as removing duplicates, standardizing fields, and checking for inconsistencies before analysis. 
* If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?
  *  N/A 
* Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created.
  *  The data was collected from 2018 to 2025

*Preprocessing/cleaning/labeling* 

* Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remaining questions in this section.
  *  Yes, significant preprocessing and cleaning were performed. This included standardizing column names and formats, converting date and numeric fields, and removing duplicate records from the original datasets. Missing values in key engagement fields (e.g., applications and attendance) were handled, often by filling with 0 for aggregation purposes.
  *  Additional steps included creating new features such as year fields from dates and bucketing variables like application counts and attendance for analysis. The datasets were then merged using a common employer identifier to create a unified dataset for analysis.  
* Were any transformations applied to the data (e.g., cleaning mismatched values, cleaning missing values, converting data types, data aggregation, dimensionality reduction, joining input sources, redaction or anonymization, etc.)? If so, please provide a description.
  *  Transformations included converting data types (e.g., dates and numeric fields), cleaning mismatched values, aggregating data at the employer level, and creating derived metrics such as application yield and event scores. The datasets were also joined using a common employer identifier to integrate employer, job, and event data into a single dataset.    
* Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data, this could be a link to a folder in your GitHub Repo, Spark\! owned Google Drive Folder for this project, or a path on the SCC, etc.
  *  https://drive.google.com/file/d/1cMYPqEBhehpngt3jGi3NjSvoUf-2eNmB/view?usp=drive_link
  *  https://drive.google.com/file/d/1deIBV-F40g3MKjLvFJfbjb9j67GBQHa_/view?usp=drive_link
  *  https://drive.google.com/file/d/1MwtrH_E3BTs_-3ZYJR96oiR0OVfnLwGD/view?usp=drive_link
  *  https://docs.google.com/spreadsheets/d/1d7kVvOUcr7ts809rlSvwCnJagX28I9jT/edit?usp=drive_link&ouid=108092223685205518441&rtpof=true&sd=true
* Is the code that was used to preprocess/clean the data available? If so, please provide a link to it (e.g., EDA notebook/EDA script in the GitHub repository).
  *  https://github.com/BU-Spark/ds-employer-engagement/blob/a86c7f5c7ffa625ca2792ac890287300ba235d36/milestone_1_clean%26join_v2.ipynb
  *  https://github.com/BU-Spark/ds-employer-engagement/blob/a86c7f5c7ffa625ca2792ac890287300ba235d36/milestone_1_cleaned_EDA_v3.ipynb
  *  https://github.com/BU-Spark/ds-employer-engagement/blob/a86c7f5c7ffa625ca2792ac890287300ba235d36/ms2_employer_analysis_v2.ipynb
  *  https://github.com/BU-Spark/ds-employer-engagement/blob/a86c7f5c7ffa625ca2792ac890287300ba235d36/ms2_employer_analysis_v3.ipynb
  *  https://github.com/BU-Spark/ds-employer-engagement/blob/a86c7f5c7ffa625ca2792ac890287300ba235d36/ms3_outcome_analysis_v1.ipynb

*Uses* 

* What tasks has the dataset been used for so far? Please provide a description.
  *  The dataset has been used for exploratory data analysis, trend analysis of employer and student engagement, KPI development, and analyzing hiring outcomes. It was also used to create visualizations, a final slide deck, and interactive Power BI dashboards.
* What (other) tasks could the dataset be used for?
  *   The dataset could be used for predictive modeling (e.g., predicting hiring outcomes or student engagement), employer segmentation, and recommendation systems (e.g., suggesting employers or events to students). It could also support longitudinal trend analysis, resource allocation decisions, and optimizing employer outreach strategies.
* Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?
  *   Yes. Missing/inconsistent fields, limited student-level data, and incomplete outcome tracking may affect analyses. The joined structure can also introduce duplication, and Handshake data does not capture off-platform interactions, which may bias results.
* Are there tasks for which the dataset should not be used? If so, please provide a description.
  *   Yes. The dataset should not be used for causal inference about employer effectiveness or student outcomes, as it is observational and lacks key control variables. It is also not suitable for individual-level predictions or decision-making, since it contains limited and aggregated student data. Additionally, it should not be used for analyses requiring complete or fully accurate hiring outcomes, as the data may be incomplete and does not capture off-platform interactions.

*Distribution*

* Based on discussions with the client, what access type should this dataset be given (eg., Internal (Restricted), External Open Access, Other)?
  *  Internal (Restricted)

*Maintenance* 

* If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description.
  *  It can be extended internally by accessing updated Handshake exports or additional CCD data (e.g., student outcomes) and applying the same cleaning and merging pipeline.

*Other*

* Is there any other additional information that you would like to provide that has not already been covered in other sections?
  *  No
