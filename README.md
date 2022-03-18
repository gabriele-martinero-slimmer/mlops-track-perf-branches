#TOOLS I USED IN THIS REPO
[dvc](https://dvc.org/doc/use-cases/versioning-data-and-model-files)
 

# WHY DVC 
I think it is important to keep track of data and models over time in order to:

1.  reproduce runs/models whenever needed
2. compare model metrics among experiments

# STEPS I TOOK ALONG THE REPOSITORY

Initialize dvc 
> dvc init 

Defining the worklow in dvc:
> dvc run -n get_data -d x1_get_data.py -o train.csv -o test.csv --no-exec python x1_get_data.py
we create a yaml file by defining by:
1. defining dependencies, recorded in deps
2. defininng the output as outs

After running this command, we will get a dvc yaml file

Note that by using *dvc run* multiple times, we can define DAGs.

- we define the second stge for preprocessing the extracted data
> dvc run -n process -d x2_process_data.py -d test.csv -d train.csv -o data_processed.csv --no-exec python x2_process_data.py

> dvc run --force -n train -d x3_train.py -d data_processed.csv -o ROC.png -m metrics.json -M  --no-exec python x3_train.py 





