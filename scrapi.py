import json
import argparse
import pprint

#####################
### Api level
#####################

def add_api_name(text, file):
    file.write('# ' + text)
    file.write('\n\n')

def add_api_headers(text, file):
    file.write('**Required headers:** \n')
    add_json(text, file)

#####################
### Util
#####################

def add_json(text, file):
    formatted = pprint.pformat(text, width=1)
    file.write("```python \n")
    file.write(formatted)
    file.write("\n```")
    file.write('\n\n')

def horizontal_line(file):
    file.write('---')
    file.write('\n\n')

#####################
### Resource level
#####################

def add_resource_name(text, file):
    file.write('## ' + text)
    file.write('\n\n')

#####################
### Action level
#####################

def add_action_name(text, file):
    file.write('#### ' + text)
    file.write('\n\n')

def add_descr(text, file):
    file.write(text)
    file.write('\n\n')

def add_url(text, file):
    file.write("**URL:** `%s`" % text)
    file.write('\n\n')

def add_method(text, file):
    file.write("**Method:** `%s`" % text)
    file.write('\n\n')

def add_required_fields(text, file):
    out_file.write('**Required fields:** \n')
    add_json(text, file)

def add_required_args(text, file):
    out_file.write('**Required QS arguments:** \n')
    add_json(text, file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()

    raw = open(args.input_file)

    loaded = json.load(raw)
    out_file = open(args.output_file, 'w')

    #add api name
    add_api_name(loaded.get('api_name'), out_file)

    #add api version

    #add required headers
    add_api_headers(loaded.get('headers'), out_file)

    #add resource table of contents

    #add resources
    for resource in loaded.get('resources'):
        add_resource_name(resource.get('name'), out_file)

        for action in resource.get('actions'):
            add_action_name(action.get('name'), out_file)
            add_descr(action.get('descr'), out_file)
            add_url(action.get('url'), out_file)
            add_method(action.get('method'), out_file)

            if action.get('req_args'):
                add_required_args(str(action.get('req_args')), out_file)

            if action.get('method') == 'POST':
                add_required_fields(action.get('req_fields'), out_file)

            horizontal_line(out_file)








