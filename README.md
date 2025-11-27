# GWF Template Repository

Template for standard project folder structure (from ```birc-project```) containing the following folders:

  ```code:``` stores scripts and notebooks that produces intermediate and final results. Contains: 

  - ```gwf:``` stores the workflow file and all templates 
      - ```templates:``` contains the templates for the workflow
      - ```utils:``` contains helper functions, such as modpath
      - ```workflow.py```
  - ```notebooks:``` stores Jupyter Notebooks
  - ```scripts:``` stores scripts that are used in the templates of the workflow 

  ```config:``` stores a yaml file with all input paths, names, etc for the workflow
  ```data:``` stores data files. \
  ```docs:``` stores text files explaining how the project and the analyzes are set up. \
  ```sandbox:``` stores experiments that are not yet part of the project workflow. \
  ```steps:``` stores intermediary files ("steps" on the way to final results). \
  ```plots:``` stores result plots and figures. \
  ```results:``` stores the small result files of the project. 
