def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, int) and not object:
        if not isinstance(object, bool):
            print(f"Zero: {object} {type(object)}")
        else:
            print(f"Fake: {object} {type(object)}")
    elif isinstance(object, str) and not object:
        print(f"Empty: {object}{type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0


# print("First Module's name: {}".format(__name__))
