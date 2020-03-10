def encode(message):
    count = 1
    value = ""
    value_2 = []
    for i in range(0, len(message)):
        if i != len(message) - 1:
            if (message[i]) == message[i + 1]:
                count = count + 1
                value = str(count) + message[i]
                print(value)
            else:
                count = 1
                value_2.append(value)
                value = ""
        else:
            value_2.append(value)

    return ("".join(value_2))

message=input("Enter the message:");
list_a=encode(message);
print("The Message after encoding:"+list_a)
