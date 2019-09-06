from cryptanalysis.monoalphabetic import freq_matrix, key
from util import cipher, mapping, file_reader
import copy


class Analyzer:

    def __init__(self, ciphertext):
        self.expected = freq_matrix.FreqMatrix()
        self.expected.load_expected_bigram_file()
        self.distribution = freq_matrix.FreqMatrix()
        self.key = key.Key(mapping.alphabet)
        self.plaintext = None
        self.ciphertext = ciphertext
        self.current_difference = float('inf')
        self.best_difference = float('inf')
        self.distribution.load_freq_from_text(self.ciphertext)

    def break_cipher(self):
        print("Cipher is", self.ciphertext)
        self.best_difference = self.distribution.eval_difference(self.expected, self.key.get_key())
        iteration_best_difference = self.best_difference
        iteration_best_distribution = copy.copy(self.distribution)
        iteration_best_key = copy.copy(self.key)

        a = 0
        print("Starting difference is ", self.best_difference, "key is", self.key.key)
        while True:
            for char in mapping.freq:

                new_key = copy.copy(self.key)
                new_key.swap(a, mapping.alphabet.find(char))
                print(new_key.get_key())
                # a += 1
                # if a+b > 25:
                #     a = 0
                #     b += 1
                #     if b == 25:
                #         print("Done")
                #         break
                new_distribution = copy.copy(self.distribution)
                new_distribution.swap_cols_rows(mapping.alphabet[a], char)
                current_difference = new_distribution.eval_difference(self.expected, new_key.get_key())
                if current_difference < iteration_best_difference:
                    print("Found better key:", new_key.get_key(), ", better difference is", current_difference)
                    iteration_best_difference = copy.copy(current_difference)
                    iteration_best_distribution = copy.copy(new_distribution)
                    iteration_best_key = copy.copy(new_key)
            # iteration done, found best place for character mapping.alphabet[a]
            if iteration_best_difference < self.best_difference:
                self.best_difference = iteration_best_difference
                self.distribution = copy.copy(iteration_best_distribution)
                self.key = copy.copy(iteration_best_key)
                a = -1
            a += 1
            if a == 26:
                break
        print("Best key is:", self.key.get_key())
        print("Best difference is", self.best_difference)
        print("text is", cipher.decrypt_mono(self.ciphertext, self.key.get_key()))

plaintext = "Friendship contrasted solicitude insipidity in introduced literature it. ""He seemed denote except as oppose do spring my. ""Between any may mention evening age shortly can ability regular. He shortly sixteen of colonel colonel ""evening cordial to. Although jointure an my of mistress servants am weddings. Age why the therefore ""education unfeeling for arranging. Above again money own scale maids ham least led. Returned settling"" produced strongly ecstatic use yourself way. Repulsive extremity enjoyment she perceived nor.""Ladyship it daughter securing procured or am moreover mr. Put sir she exercise vicinity c""heerful wondered. Continual say suspicion provision you neglected sir curiosity unwilling. Simplicity ""end themselves increasing led day sympathize yet. General windows effects not are drawing man garrets. ""Common indeed garden you his ladies out yet. Preference imprudence contrasted to remarkably in on. ""Taken now you him trees tears any. Her object giving end sister except oppose. "
# ciphertext1 = file_reader.read_file("ciphertext1.txt")
ciphertext = cipher.encrypt_mono(plaintext, "bcadefghijklmnopqrstuvwxyz")
a = Analyzer(ciphertext)
a.break_cipher()
