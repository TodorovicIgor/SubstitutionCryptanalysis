from cryptanalysis.monoalphabetic import freq_matrix, key
from util import cipher, mapping, file_reader
import copy
import random


class Analyzer:

    def __init__(self, ciphertext):
        self.expected = freq_matrix.FreqMatrix()
        self.expected.load_expected_bigram_file()
        self.distribution = freq_matrix.FreqMatrix()
        self.key = key.Key()
        self.best_difference = float('inf')
        self.plaintext = None
        self.ciphertext = ciphertext
        self.current_difference = float('inf')

    def break_cipher(self):
        self.distribution.load_freq_from_text(self.ciphertext)
        self.best_difference = self.distribution.eval_difference(self.expected, self.key.get_key())
        iteration_best_difference = self.best_difference
        a = 0
        print("Starting difference is ", self.best_difference, "key is", self.key.key)

        while True:
            # print("Current key is ", self.key.get_key())
            # print(new_key.get_key(), ", ", self.key.get_key())
            for char in mapping.freq:
                new_key = self.key.swap(a, mapping.alphabet.find(char))
                # if a == 26:
                #     b += 1
                #     a = 0
                #     if b == 26:
                #         break
                # ********************
                # a += 1
                # if a+b > 25:
                #     a = 0
                #     b += 1
                #     if b == 25:
                #         print("Done")
                #         break
                new_distribution = copy.copy(self.distribution)
                new_distribution.swap_cols_rows(mapping.alphabet[a], char)  # ***************************
                current_difference = new_distribution.eval_difference(self.expected, new_key.get_key())
                if current_difference < iteration_best_difference:
                    b = a
                    print("Found better key:", new_key.get_key(), ", better difference is", current_difference)
                    iteration_best_difference = copy.copy(current_difference)
                    iteration_best_distribution = copy.copy(new_distribution)
                    iteration_best_key = copy.copy(new_key)
            # iteration done
            if (iteration_best_difference < self.best_difference):
                pass
                # TODO u self stavi najbolji rezultat
            a += 1
        # print(cipher.decrypt_mono(self.ciphertext, self.key.get_key()))
        print("Best key is:", self.key.get_key())
        print("Best difference is", self.best_difference)
        print("text is",cipher.decrypt_mono(self.ciphertext, self.key.get_key()))

plaintext = "Friendship contrasted solicitude insipidity in introduced literature it. ""He seemed denote except as oppose do spring my. ""Between any may mention evening age shortly can ability regular. He shortly sixteen of colonel colonel ""evening cordial to. Although jointure an my of mistress servants am weddings. Age why the therefore ""education unfeeling for arranging. Above again money own scale maids ham least led. Returned settling"" produced strongly ecstatic use yourself way. Repulsive extremity enjoyment she perceived nor.""Ladyship it daughter securing procured or am moreover mr. Put sir she exercise vicinity c""heerful wondered. Continual say suspicion provision you neglected sir curiosity unwilling. Simplicity ""end themselves increasing led day sympathize yet. General windows effects not are drawing man garrets. ""Common indeed garden you his ladies out yet. Preference imprudence contrasted to remarkably in on. ""Taken now you him trees tears any. Her object giving end sister except oppose. "
plaintext2 = file_reader.read_file("ciphertext1.txt")
# ciphertext = cipher.encrypt_mono(plaintext, mapping.alp)
a = Analyzer(cipher.transform(plaintext))
# print(test.distribution.eval_difference(test.expected, test.key.get_key()))
a.break_cipher()
