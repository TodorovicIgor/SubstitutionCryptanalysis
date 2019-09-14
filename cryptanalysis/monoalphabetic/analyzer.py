from cryptanalysis.monoalphabetic import freq_matrix, key
from util import cipher, mapping, file_reader
import copy


class Analyzer:

    def __init__(self, ciphertext):
        self.expected = freq_matrix.FreqMatrix()
        self.expected.load_expected_bigram_file()
        self.distribution = freq_matrix.FreqMatrix()
        self.key = key.Key(mapping.freq)  # step 1
        self.plaintext = None
        self.ciphertext = ciphertext
        self.current_difference = float('inf')
        self.best_difference = float('inf')
        self.distribution.load_freq_from_text(cipher.decrypt_mono(self.ciphertext, self.key.get_key()))  # step 2

    def break_cipher(self):
        print("Cipher is", self.ciphertext)
        self.best_difference = self.distribution.eval_difference(self.expected, self.key.get_key())  # step 3
        # a = b = 0  # step 0
        print("Starting function value is ", self.best_difference, "key is", self.key.key)
        new_iteration = True
        while new_iteration:
            for a in range(26):
                for b in range(26):

                    new_iteration = False
                    print("\nCurrent key is \t", self.key.get_key())
                    new_key = copy.copy(self.key)  # step 4
                    new_distribution = copy.copy(self.distribution)  # step 5

                    # new_key.swap(a, a+b)    # step 6a
                    # a = a + 1               # step 6b
                    # if a+b >= 26:           # step 6c
                    #     a = 1               # step 6d
                    #     b = b + 1           # step 6e
                    #     if b == 25: break   # step 6f

                    # print(a, b)
                    print("New key is \t\t", new_key.get_key(), "swapped", mapping.freq[a], "and", mapping.freq[b])
                    new_distribution.swap_cols_rows(mapping.freq[a], mapping.freq[b])  # step 7
                    current_difference = new_distribution.eval_difference(self.expected, new_key.get_key())  # step 8
                    print("New function value is", current_difference, "with net", self.best_difference-current_difference)
                    if current_difference < self.best_difference:  # step 9
                        # a = b = 0  # step 9a
                        new_iteration = True
                        print("Found better key:", new_key.get_key(), ", better function value is", current_difference, "************************************")
                        self.best_difference = copy.copy(current_difference)    # step 10
                        self.key = copy.copy(new_key)                           # step 11
                        self.distribution = copy.copy(new_distribution)         # step 12
        # step 13

        print("Best key is:", self.key.get_key())
        print("Best difference is", self.best_difference)
        print("text is", cipher.decrypt_mono(self.ciphertext, self.key.get_key()))

plaintext = "Friendship contrasted solicitude insipidity in introduced literature it. ""He seemed denote except as oppose do spring my. ""Between any may mention evening age shortly can ability regular. He shortly sixteen of colonel colonel ""evening cordial to. Although jointure an my of mistress servants am weddings. Age why the therefore ""education unfeeling for arranging. Above again money own scale maids ham least led. Returned settling"" produced strongly ecstatic use yourself way. Repulsive extremity enjoyment she perceived nor.""Ladyship it daughter securing procured or am moreover mr. Put sir she exercise vicinity c""heerful wondered. Continual say suspicion provision you neglected sir curiosity unwilling. Simplicity ""end themselves increasing led day sympathize yet. General windows effects not are drawing man garrets. ""Common indeed garden you his ladies out yet. Preference imprudence contrasted to remarkably in on. ""Taken now you him trees tears any. Her object giving end sister except oppose. "
ciphertext1 = file_reader.read_file("ciphertext1.txt")
ciphertext = cipher.encrypt_mono(plaintext, "bcadefghijklmnopqrstuvwxyz")
# a = Analyzer(cipher.transform(plaintext))
a = Analyzer(ciphertext)
a.break_cipher()
