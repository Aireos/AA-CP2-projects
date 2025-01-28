name = input("Real life name: ")
charecter_name = input("Charecter name: ")
race = input("Race (elf, human, outworlder, ): ")
while True:
    type = input("Type (glass cannon, healer, tank, bruiser, speedster, generalist, debuffer, buffer): ")
    if type == "glass cannon" or "healer" or "tank" or "bruiser" or "speedster" or "generalist" or "debuffer" or "buffer":
        break
    else:
        print("invalid type")
        print()
