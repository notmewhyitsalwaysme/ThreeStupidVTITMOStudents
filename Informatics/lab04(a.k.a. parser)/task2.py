
def serialize_bin(filename: str) -> dict:
    data: dict = {}
    current_section: str = ""
    
    with open(filename, "r") as f:
        for line in f.readlines():
        
            # section 
            if "  " not in line:
                current_section = ''.join([chr(int(char, 2)) for char in line.split(" ")])
                data[current_section] = {}
                continue
            
            # body 
            key, value = line.split("  ")
            key = ''.join([chr(int(char, 2)) for char in key.split(" ")])
            value = ''.join([chr(int(char, 2)) for char in value.split(" ")])
            
            # absolute magic
            try:
                # 'cause 1 or 0 is boolean in INI
                if value in ('1', '0'):
                    raise ValueError
                
                # integer
                data[current_section][key] = int(value)
                
            except ValueError:
                # boolean 
                if value.lower() in ('true', 'on', '1', 'yes'):
                    data[current_section][key] = True
                    
                elif value.lower() in ('false', 'off', '0', 'no'):
                    data[current_section][key] = False
            
                # string
                else:
                    data[current_section][key] = value
        
    return data  

def dict_to_hcl(data: dict, indent:int = 4, is_root: bool=False) -> str:
    spaces = '  ' * indent
    lines = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            # dict
            if isinstance(value, dict):
                if is_root and key.startswith('lesson'):
                    # root objects
                    lines.append(f'{key} = {{')
                    lines.append(dict_to_hcl(value, indent + 1))
                    lines.append(f'{spaces}}}')
                    lines.append('')  # for beauty reasons 
                else:
                    # nested objects
                    lines.append(f'{spaces}{key} = {{')
                    lines.append(dict_to_hcl(value, indent + 1))
                    lines.append(f'{spaces}}}')
                    
            # list
            elif isinstance(value, list):
                lines.append(f'{spaces}{key} = [')
                for item in value:
                    if isinstance(item, dict):
                        lines.append(f'{spaces}  {{')
                        lines.append(dict_to_hcl(item, indent + 2))
                        lines.append(f'{spaces}  }}')
                    else:
                        lines.append(f'{spaces}  {format_value(item)}')
                lines.append(f'{spaces}]')
                
            else:
                # key = value 
                lines.append(f'{spaces}{key} = {format_value(value)}')
    
    return '\n'.join(lines)

def format_value(value: str | bool | None) -> str:
        if isinstance(value, str):
            # wrap in double quotes
            escaped = value.replace('"', '\\"')
            return f'"{escaped}"'
    
        elif isinstance(value, bool):
            return str(value).lower()
    
        elif value is None:
            return 'null'
    
        else:
            # escaping quotes
            s = str(value)
            s = s.replace('"', '\\"')
            s = s.replace('\n', '\\n').replace('\t', '\\t')
            return f"\"{s}\""

def save_hcl(data: dict, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(dict_to_hcl(data, indent=0))

def convert(bin_filename: str, hcl_filename: str) -> None:
    save_hcl(serialize_bin(bin_filename), hcl_filename)

if __name__ == "__main__":
    convert("mySchedule.bin", "mySchedule.hcl")
