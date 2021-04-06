response = int(input("How long till the party's started? "))

if (response<1):
    print("party NoOoW ")
else:
    for response in range(response, 0,-1):
        print(response)
    print("It appears to be party time!")