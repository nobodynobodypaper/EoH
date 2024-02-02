import sys
import os


from ael import ael
from ael.utils import createFolders


### LLM settings  ###
llm_type = "API2D-GPT" # currently only API2D-GPT
llm_key = "fk198715-4a9tb8giFcMjEkfezQBHUAtSwaHjdXo9" # your key
llm_model  =  "gpt-3.5-turbo-1106" 
#model_LLM = "gpt-4-0613"


### output path ###
output_path = "./" # default for ael outputs
createFolders.create_folders(output_path)

load_data = {
    "is_load" : False,
    "path" : output_path+"/ael_results/pops/population_generation_20.json",
    "n_pop_initial": 20
    }

### Experimental settings ###
pop_size = 10 # popopulation size, i.e., the number of algorithms in population
n_pop = 20 # number of populations 
operators = ['e1','e2','m1','m2','simple']  # evolution operators: ['e1','e2','m1','m2'], default = ['e1','m1']
m = 5  # number of parents for 'e1' and 'e2' operators, default = 2
operator_weights = [1,1,1,1,1] # weights for operators, i.e., the probability of use the operator in each iteration , default = [1,1,1,1]

### Debug model ###
debug_mode = False# if debug


# AEL
print(">>> Start AEL ")
algorithmEvolution = ael.AEL(llm_type,llm_key,llm_model,pop_size,n_pop,operators,m,operator_weights,load_data,output_path,debug_mode)

# run AEL
algorithmEvolution.run()

print("AEL successfully finished !")


