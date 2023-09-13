import re


# 1
def full_name(str_arg: str) -> str:
    """_summary_

    Args:
        str_arg (str): _description_

    Returns:
        str: _description_
    """
    res = str_arg.split(" ")
    return res[0].upper() + " " + res[1].capitalize()


print(full_name("thiry stéphane"))


# 2
def is_mail(str_arg: str) -> (int, int):
    """_summary_

    Args:
        str_arg (str): _description_
        int (_type_): _description_
    """
    res = (0, 0)
    if re.match(r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", str_arg):
        res = (1, 1)
    elif re.match(r"\A@", str_arg):
        res = (0, 1)
    elif re.match(r"^[a-zA-Z0-9._-]+[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", str_arg):
        res = (0, 2)
    elif re.match(r"^[a-zA-Z0-9._-]+@+\.[a-zA-Z]{2,}$", str_arg):
        res = (0, 3)
    elif re.match(r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+[a-zA-Z]{2,}$", str_arg):
        res = (0, 4)

    return res


print("mail valide 'stethiry9@gmail.com' : ", is_mail("stethiry9@gmail.com"))
print("corp du mail invalide '@gmail.com' : ", is_mail("@gmail.com"))
print("mail invalide, manque @ 'stethiry9gmail.com' : ", is_mail("stethiry9gmail.com"))
print("mail invalide, domaine invalide 'stethiry9@.com' : ", is_mail("stethiry9@.com"))
print(
    "mail invalide, manque le point 'stethiry9@gmail.com' : ",
    is_mail("stethiry9@gmailcom"),
)
