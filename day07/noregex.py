#!/usr/bin/python3
import re

def contains_abba(substring):
    #if len(substring) < 4  # doesn't happen in expected input data
    #    return False
    for i in range(len(substring) - 3):
        a = substring[i]
        b = substring[i+1]
        if a != b and a == substring[i+3] and b == substring[i+2]:
            return True
    return False

def get_num_tls_support(data):
    num_ip = 0
    for line in data.splitlines():
        parts = re.split(r'\[|\]', line)
        # at least one in even numbered and none in odd numbered ones
        even_contains_abba = False
        odd_contains_abba = False
        for idx, part in enumerate(parts):
            if idx % 2 == 0:
                even_contains_abba = even_contains_abba or contains_abba(part)
            else:
                odd_contains_abba = odd_contains_abba or contains_abba(part)
        if even_contains_abba and not odd_contains_abba:
            #print(line)
            num_ip += 1
    return num_ip

def extract_aba(substring, out_list):
    #if len(substring) < 3  # doesn't happen in expected input data
    #    return False
    for i in range(len(substring) - 2):
        a = substring[i]
        b = substring[i+1]
        if a != b and a == substring[i+2]:
            out_list.append(substring[i:(i+2)])

def get_num_ssl_support(data):
    num_ip = 0
    for line in data.splitlines():
        parts = re.split(r'\[|\]', line)
        # at least aba must have at least one corresponsing bab
        supernet_sequences = parts[::2]
        hypernet_sequences = parts[1::2]

        abas = []
        for seq in supernet_sequences:
            extract_aba(seq, abas)
        babs = []
        for seq in hypernet_sequences:
            extract_aba(seq, babs)
        babs = [bab[::-1] for bab in babs]

        for bab in babs:
            if bab in abas:
                #print(line)
                num_ip += 1
                break

    return num_ip


def main():
    # test input
    #data = '''abba[mnop]qrst
    #abcd[bddb]xyyx
    #aaaa[qwer]tyui
    #ioxxoj[asdfgh]zxcvbn'''
    #data = '''aba[bab]xyz
    #xyx[xyx]xyx
    #aaa[kek]eke
    #zazbz[bzb]cdb'''

    # file input
    with open('input.txt', 'r') as f:
        data = f.read()

    print("Number of IPs supporting TLS", get_num_tls_support(data))
    print("Number of IPs supporting SSL", get_num_ssl_support(data))

if __name__ == "__main__":
    main()