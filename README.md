# Pipelines Project | Food Production & Greenhouse gas emissions

Bootcamp Data Analytics Ironhack


Over the last years, we have started to hear that population growth and the rise of meat and dairy consumption might be having an important enviromental impact. This project makes an attempt to explore the relation between food production and Greenhouse gas emissions within the most relevant countries in the European Union. 

From a kaggle.com dataset with precise information about food production throughout the past decades, I complemented it with data of Greenhouse gas emissions per year and country from the Organisation for Economic Co-operation and Development. I did so by extracting the information from the OECD website via scrapping techniques. 

The main file gives a choice to the user of selecting a country in the EU and returns information about the maximum levels of these variables and downloads two graphics with their evolution since 1990.

---- 

The project has different folders an files:
• Input: containing the original database.
• Src: container of the scripts with the pipelines for all the processes.
    - cleanning_fooddf.py
    - scrapping.py
    - cleanning_pollutiondf.py
    - analysis.py
    - god.py: concentrates all the previous steps in a mayor pipeline.
    - main.py: defines the argparse and executes the program importing god.py.
• Output: keeps the final datasets and graphics.
• Tests: includes the test in Jupyter Notebook.