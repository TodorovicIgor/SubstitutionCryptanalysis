from cryptanalysis.monoalphabetic import freq_matrix, key
from util import cipher, mapping, file_reader
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
        self.best_difference = self.distribution.eval_difference(self.expected, self.key.key)
        a = b = 0

        while True:
            new_key = self.key
            print(a, b, a+b)
            new_key.swap(a, a+b)
            a += 1
            if a+b > 25:
                a = 0
                b += 1
                if b == 25:
                    break

            new_distribution = self.distribution
            new_distribution.swap_cols_rows(mapping.freq[a], mapping.freq[b])
            current_difference = new_distribution.eval_difference(self.expected, new_key.get_key())
            if current_difference < self.best_difference:
                a = b = 0
                print("Found better key: ", new_key.get_key())
                self.best_difference = current_difference
                self.distribution = new_distribution
                self.key = new_key
        print(cipher.decrypt_mono(self.ciphertext, self.key.get_key()))
        print(self.key.get_key())
        print(self.best_difference)

plaintext = "Friendship contrasted solicitude insipidity in introduced literature it. ""He seemed denote except as oppose do spring my. ""Between any may mention evening age shortly can ability regular. He shortly sixteen of colonel colonel ""evening cordial to. Although jointure an my of mistress servants am weddings. Age why the therefore ""education unfeeling for arranging. Above again money own scale maids ham least led. Returned settling"" produced strongly ecstatic use yourself way. Repulsive extremity enjoyment she perceived nor.""Ladyship it daughter securing procured or am moreover mr. Put sir she exercise vicinity c""heerful wondered. Continual say suspicion provision you neglected sir curiosity unwilling. Simplicity ""end themselves increasing led day sympathize yet. General windows effects not are drawing man garrets. ""Common indeed garden you his ladies out yet. Preference imprudence contrasted to remarkably in on. ""Taken now you him trees tears any. Her object giving end sister except oppose. "
plaintext2 = file_reader.read_file("ciphertext1.txt")
ciphertext = cipher.encrypt_mono(plaintext2, "zyxwvutsrqponmlkjihgfedc")
a = Analyzer(ciphertext)
a.break_cipher()
