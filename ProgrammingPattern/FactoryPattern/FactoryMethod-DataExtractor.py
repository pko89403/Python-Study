import json 
import xml.etree.ElementTree as etree 
"""
    다양한 input 인 XML, JSON file을 parsing하고, client's connection을 centralize 함.
"""
class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)
    
    @property
    def parsed_data(self):
        return self.data 

class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)
    
    @property
    def parsed_data(self):
        return self.tree 

def dataextraction_factory(filepath):
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath))
    
    return extractor(filepath)

def extract_data_from(filepath):
    factory_obj = None 
    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as e:
        print(e)
    
    return factory_obj


def main():
    sqlite_factory = extract_data_from('data/person.sq3')
    print() 

    json_factory = extract_data_from('data/movies.json')
    json_data = json_factory.parsed_data
    print(f'Found: {len(json_data)} movies')
    for movie in json_data:
        print(f"Title : {movie['title']}")
        year = movie['year']
        if year:
            print(f"Year: {year}")
        director = movie['genre']
        if genre:
            print(f"Genre: {genre}")
        print()

    xml_factory = extract_data_from('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(f".//person[lastName='Liar']")
    print(f"found: {len(liars)} persons")
    for liar in liars:
        firstname = liar.find('firstName').text 
        print(f'first name: {firstname}')
        lastname = liar.find('lastname').text 
        print(f'last name: {lastname}')
        [print(f"phone number ({p.attrib['type']}):", p.text)
            for p in liar.find('phoneNumbers')]
        print()
    print()

if __name__ == "__main__":
    main()
