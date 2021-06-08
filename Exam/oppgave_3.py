def translate_date(date:str):
    split_date = date.split(".")
    modified_date = split_date[2]+"-"+split_date[1]+"-"+split_date[0]
    return modified_date

print(translate_date("19.05.2021"))