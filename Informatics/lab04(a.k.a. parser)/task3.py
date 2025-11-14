import pickle        # BIN
import configparser  # INI
import hcl2          # HCL


def parse_value(value: str) -> int | bool | str:
    # absolute magic 2
    try:
        # 'cause 1 or 0 is boolean in INI
        if value in ('1', '0'):
            raise ValueError
        
        # integer
        return int(value)
        
    except ValueError:
        # boolean 
        if value.lower() in ('true', 'on', '1', 'yes'):
            return True
            
        elif value.lower() in ('false', 'off', '0', 'no'):
            return False
    
        # string
        else:
            return value

def ini_to_dict(filename: str) -> dict:
    cfg = configparser.ConfigParser()
    cfg.read(filename)
    
    data = {}
    for section in cfg.sections():
        data[section] = {}
        for key, value in cfg.items(section):
            
            if value[0] in ('"', "'") and value[-1] in ('"', "'"):
                value = value[1:-1]
                
            data[section][key] = parse_value(value)
            
    return data

def write_bin(data: dict, filename: str) -> None:
    with open(filename, "wb") as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

def read_bin(filename: str) -> None:
    with open(filename, "rb") as f:
        return pickle.load(f)

def dict_to_hcl(data: dict, filename: str) -> None:
    with open(filename, "w") as f:
        d = hcl2.writes(hcl2.reverse_transform(data))
        f.write(d)

def convert(ini_filename: str, bin_filename: str, hcl_filename: str) -> None:
    write_bin(ini_to_dict(ini_filename), bin_filename)
    dict_to_hcl(read_bin(bin_filename), hcl_filename)

if __name__ == "__main__":
    convert("MySchedule.ini", "MyScheduleWithLibs.bin", "MyScheduleWithLibs.hcl")
    