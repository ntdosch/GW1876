import os

os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=1800 --inplace setup_pest_interface.ipynb")
os.system("jupyter nbconvert --to pdf setup_pest_interface.ipynb")
os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=1800 --inplace prior_montecarlo.ipynb")
os.system("jupyter nbconvert --to pdf prior_montecarlo.ipynb")
os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=1800 --inplace pestpp-glm.ipynb")
os.system("jupyter nbconvert --to pdf pestpp-glm.ipynb")
os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=1800 --inplace pestpp-ies.ipynb")
os.system("jupyter nbconvert --to pdf pestpp-ies.ipynb")
os.system("jupyter nbconvert --execute --ExecutePreprocessor.timeout=1800 --inplace pestpp-opt.ipynb")
os.system("jupyter nbconvert --to pdf pestpp-opt.ipynb")
