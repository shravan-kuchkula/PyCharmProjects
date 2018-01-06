
def findDuplicate(a):
    print("findDuplicate")
    noDups = []

    for item in a:
        if item in noDups:
            print(item)
        else:
            noDups.append(item)

    return(noDups)

def main():
    print("main")
    a = [10, 5, 6, 6, 2, 1, 5]
    noDups = findDuplicate(a)
    print(noDups)


if __name__ == "__main__":
    main()

