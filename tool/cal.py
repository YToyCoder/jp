
def main():
    max_val_jLong = ((1 << 63) - 1)
    count = 1
    multi = 5
    while multi < max_val_jLong:
        multi *= 5
        count += 1
    print(f"{count} - {multi}")
    print(max_val_jLong)
    print(multi)

    print(1e9 + 1)
    print(max_val_jLong)
    print((20 ** 14) * 4)
    print((20 ** 14) * 5)



if __name__ == "__main__":
    main()
