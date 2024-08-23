amount_due=50
while amount_due>0:
    print(f"amount_due:{amount_due}")
    insert_coin=input("insert coin:")
    if insert_coin in ["5","10","25"]:
        insert_coin=int(insert_coin)
    else:
        insert_coin=0
    amount_due-=insert_coin

change_owed=-amount_due
print(f"change_owed:{change_owed}")

