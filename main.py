def isometric_strings(a, b):
    slovar = {}
    kek = []
    for i in range(len(a)):
        if a[i] not in slovar.keys() and b[i] not in slovar.values():
            slovar[a[i]] = b[i]
        elif b[i] != slovar[a[i]]:
            return False
    return len(slovar.keys()) == len(set(a)) and len(slovar.keys()) == len(set(b))
if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))

  5  and b[i] not in slovar.values()
  9 and len(slovar.keys()) == len(set(b))