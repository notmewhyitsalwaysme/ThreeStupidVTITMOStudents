
def parse_ini(filename: str) -> dict:
    config = {}
    current_section = None
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            
            # skip comments and empty lines
            if not line or line.startswith(';'):
                continue
                
            # section
            if line[0] == '[' and line[-1] == ']':
                current_section = line[1:-1].strip()
                if current_section not in config:
                    config[current_section] = {}
                continue
                
            # key, value
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                # quotes
                if len(value) > 1 and value[0] == value[-1] and value[0] in ('"', "'"):
                    value = value[1:-1]
                
                config[current_section][key] = value
                continue
    
    return config

def dict_to_bin(data: dict, filename: str) -> None:
    with open(filename, "w") as f:
        for section_name, inner_dict in data.items():
            # section
            f.write(' '.join(f'{bin(ord(char))[2:]}' for char in section_name) + "\n")
                
            # body
            for key, value in inner_dict.items():
                key = ' '.join(f'{bin(ord(char))[2:]}' for char in key)
                value = ' '.join(f'{bin(ord(char))[2:]}' for char in value)
                    
                line = key + "  " + value + "\n"
                f.write(line)

def convert(ini_filename: str, bin_filename: str) -> None:
    dict_to_bin(parse_ini(ini_filename), bin_filename)

if __name__ == "__main__":
    convert('mySchedule.ini', "MySchedule.bin")
