from dotdict import dotdict
import json

config_file='config.json'
f = open (config_file, "r") 
cfg = json.load(f)

# converting the cfg to an object for dot notation access
    
cfg2=dotdict(cfg)


# function to return the yaml file as object or dict 
# in the argumnet pass config_type as 'dict' or 'object'

def load_json(config_file,config_type='dict'):
    with open(config_file,'r') as f:
        cfg = json.load(f)        
    if config_type=='object':
        cfg = dotdict(cfg)
    return cfg
    
def save_json(config,save_path='config_new.json'):
    if type(config)!=dict:
        config=dict(config)
    with open(save_path, 'w') as file:
        json.dump(config, file)


cfg=load_json(config_file,config_type='object')
cfg.batch_size=25
cfg.new_var='new'
print(cfg)

save_json(cfg)
