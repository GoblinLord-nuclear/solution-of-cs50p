import plates
assert plates.is_valid("da123")==True
assert plates.is_valid("12xxt")==False
assert plates.is_valid("1")==False
assert plates.is_valid("da012")==False
assert plates.is_valid("d1234")==False
assert plates.is_valid("ddd1234")==False
assert plates.is_valid("dd123!")==False