from task2 import serialize_bin

def escape_xml(text: str) -> str:
    if not isinstance(text, str):
        text = str(text)
        
    escapes = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&apos;'
    }
    return ''.join(escapes.get(c, c) for c in text)     # .get(c,c) returns c if no escapes were found

def dict_to_xml(data: dict, root_tag: str='schedule') -> str:
    def build_element(tag: str, inner_data: dict, indent: int=2) -> str:
        spaces = '  ' * indent
        inner_elements = []
        
        for key, value in inner_data.items():
            inner_elements.append(f"{spaces}  <{key}>{escape_xml(value)}</{key}>")
        
        inner_xml = '\n'.join(inner_elements)
        tag = escape_xml(tag)
        return f"{spaces}<{tag}>\n{inner_xml}\n{spaces}</{tag}>"

    elements = []
    for key, value in data.items():
        elements.append(build_element(key, value))
    
    body = '\n'.join(elements)
    return f'<{root_tag}>\n{body}\n</{root_tag}>'

def convert(bin_filename: str, xml_filename: str) -> None:
    with open(xml_filename, "w") as f:
        f.write(dict_to_xml(serialize_bin(bin_filename)))

if __name__ == "__main__":
    convert("mySchedule.bin", "mySchedule.xml")
    