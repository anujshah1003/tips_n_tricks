import yaml
from dotdict import dotdict

config_file='config.yaml'


with open(config_file) as f:
    cfg = yaml.safe_load(f)

# converting the cfg to an object for dot notation access
print(cfg['num_classes'])
cfg2=dotdict(cfg)
print(cfg2.num_classes)


# function to return the yaml file as object or dict 
# in the argumnet pass config_type as 'dict' or 'object'

def load_yaml(config_file,config_type='dict'):
    with open(config_file) as f:
        cfg = yaml.safe_load(f)
        #params = yaml.load(f,Loader=yaml.FullLoader)
        
    if config_type=='object':
        cfg = dotdict(cfg)
    return cfg
    
def save_yaml(config,save_path='config_new.yaml'):
    if type(config)!=dict:
        config=dict(config)
    with open(save_path, 'w') as file:
        yaml.dump(config, file)

cfg=load_yaml(config_file,config_type='object')
cfg.new_var=25
cfg.new_var_2='new'
print(cfg)

save_yaml(cfg)