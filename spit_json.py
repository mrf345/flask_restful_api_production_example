import os
import json

config_file = './zappa_settings.json'
zappa_config = json.load(open(config_file))
zappa_config.get('production').get('environment_variables').update({
    'AWS_ACCESS_KEY_ID': os.getenv('AWS_ACCESS_KEY_ID'),
    'AWS_SECRET_ACCESS_KEY': os.getenv('AWS_SECRET_ACCESS_KEY'),
    'AWS_DEFAULT_REGION': os.getenv('AWS_DEFAULT_REGION')
})
json.dump(zappa_config, open(config_file, '+w'))
