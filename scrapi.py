import json

#####################
### Api level
#####################

def add_api_name(text, file):
    file.write('# ' + text)
    file.write('\n\n')

def add_api_headers(text, file):
    file.write('**Required headers:** \n')
    add_json(str(text), file)

#####################
### Util
#####################

def add_json(text, file):
    file.write("```json \n")
    file.write(text)
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
    add_json(text, file)

if __name__ == "__main__":
    raw = open('api_docs_1.json')

    loaded = json.load(raw)
    out_file = open('output.md', 'w')

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

            if action.get('method') == 'POST':
                out_file.write('**Required fields:** \n')
                add_required_fields(str(action.get('req_fields')), out_file)

            horizontal_line(out_file)








