#!/usr/bin/python3

def list_to_dict(arr: list) -> None:
    result_dict: dict = {}
    for elem in arr:
        result_dict[elem[1]] = elem[0]
    # look up how dict oder/ don't order the elements
    for key, val in result_dict.items():
        print(key ,":", val)
    

if __name__ == "__main__":
    d = [
('Hendrix' , '1942'),
('Allman' , '1946'),
('King' , '1925'),
('Clapton' , '1945'),
('Johnson' , '1911'),
('Berry' , '1926'),
('Vaughan' , '1954'),
('Cooder' , '1947'),
('Page' , '1944'),
('Richards' , '1943'),
('Hammett' , '1962'),
('Cobain' , '1967'),
('Garcia' , '1942'),
('Beck' , '1944'),
('Santana' , '1947'),
('Ramone' , '1948'),
('White' , '1975'),
('Frusciante', '1970'),
('Thompson' , '1949'),
('Burton' , '1939')]
    list_to_dict(d)