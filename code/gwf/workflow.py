"""Workflow to 



@Author: 
@Date: 

"""

from gwf import Workflow
from read_config import load_config
import templates.preproc as preproc 

gwf = Workflow()
config = load_config()

# First task
input = gwf.glob(config['something']['something'])
gwf.map(preproc.template_template, input, name=preproc.naming_template)