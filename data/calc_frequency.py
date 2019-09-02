import json as json

onegram = open("one_gram_count.txt", "r")
input_hash = {}
frequency_hash = {}
sum = 0
line = onegram.readline()
while line:
    tokens = line.split(" ")
    print(tokens)
    input_hash.update({tokens[0].lower(): int(tokens[1])})
    sum += int(tokens[1])
    print(sum)
    line = onegram.readline()
for entry in input_hash:
    temp_val = input_hash[entry]
    temp_key = entry
    print(temp_key, temp_val/sum)
    frequency_hash.update({temp_key: temp_val/sum})
one_gram_freq = open("one_gram_rel_freq.txt", "w")
one_gram_freq.write(json.dumps(frequency_hash))
print(frequency_hash)

twogram = open("two_gram_count.txt", "r")
input_hash = {}
frequency_hash = {}
sum = 0
line = twogram.readline()
while line:
    tokens = line.split(" ")
    print(tokens)
    input_hash.update({tokens[0].lower(): int(tokens[1])})
    sum += int(tokens[1])
    print(sum)
    line = twogram.readline()
for entry in input_hash:
    temp_val = input_hash[entry]
    temp_key = entry
    print(temp_key, temp_val/sum)
    frequency_hash.update({temp_key: temp_val/sum})
two_gram_freq = open("two_gram_rel_freq.txt", "w")
two_gram_freq.write(json.dumps(frequency_hash))
print(frequency_hash)
