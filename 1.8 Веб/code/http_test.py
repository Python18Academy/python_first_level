from http import HTTPStatus, IntEnum

for codes in HTTPStatus:
    print(codes.value, codes, codes.description )

