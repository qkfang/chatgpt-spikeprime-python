import json
from bs4 import BeautifulSoup

with open("lego-doc-api.html",  encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

for br in soup.find_all("br"):
    br.replace_with("\n")
    

    
apiSpec = []
for moduleNode_h3 in soup.findAll("h3"):
    print('--------------------')

    module = {}
    apiSpec.append(module)

    module['Module_Name'] = moduleNode_h3.text.strip() # h3
    module['Module_Description'] = moduleNode_h3.find_next_sibling('div').text.strip()
    module['SubModules'] = []
    module['Code_Import'] = []




with open("lego-api-sp.json", "w") as text_file:
    text_file.write(json.dumps(apiSpec, indent=2))

# print(soup)