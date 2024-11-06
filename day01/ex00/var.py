#!/usr/bin/python3

def my_var() -> None:
    int_var : int = 42
    print(int_var, "has a type", type(int_var))
    str_var : str = "42"
    print(str_var, "has a type", type(str_var))
    str2_var : str = "quarante-deux "
    print(str2_var, "has a type", type(str2_var))
    float_var : float = 42.0
    print(float_var, "has a type", type(float_var))
    bool_var : bool = True
    print(bool_var, "has a type", type(bool_var))
    list_var : list = [42]
    print(list_var, "has a type", type(list_var))
    dict_var : dict = {42: 42}
    print(dict_var, "has a type", type(dict_var))
    tuple_var : tuple = (42,)
    print(tuple_var, "has a type", type(tuple_var))
    set_var : set = set()
    print(set_var, "has a type", type(set_var))
    
if __name__ == "__main__":
    my_var()